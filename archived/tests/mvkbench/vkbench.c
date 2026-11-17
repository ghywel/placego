// Vulkan compute micro-harness for the MoltenVK-vs-Metal comparison.
// Usage: vkbench <alu|sad|tiny> [batches]
// Prints one CSV line per timed batch: mode,api,batch_ms,per_dispatch_ms
// Dispatch counts, grid sizes and barrier policy mirror metalbench.swift
// exactly; the kernels are the .spv twins of the MSL embedded there.
#include <vulkan/vulkan.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define CHK(x) do { VkResult r_ = (x); if (r_ != VK_SUCCESS) { \
    fprintf(stderr, "FAIL %s = %d at line %d\n", #x, r_, __LINE__); exit(1); } } while (0)

#define IMG_W 2048
#define IMG_H 1024

static double now_ms(void) {
    struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec * 1e3 + ts.tv_nsec / 1e6;
}

static void *read_file(const char *path, size_t *len) {
    FILE *f = fopen(path, "rb");
    if (!f) { fprintf(stderr, "cannot open %s\n", path); exit(1); }
    fseek(f, 0, SEEK_END); *len = ftell(f); fseek(f, 0, SEEK_SET);
    void *buf = malloc(*len);
    if (fread(buf, 1, *len, f) != *len) { fprintf(stderr, "short read %s\n", path); exit(1); }
    fclose(f);
    return buf;
}

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: vkbench <alu|sad|tiny> [batches]\n"); return 1; }
    const char *mode = argv[1];
    int batches = argc > 2 ? atoi(argv[2]) : 3;

    // Per-batch dispatch count and grid, matched in metalbench.swift.
    int ndisp, gw, gh;
    if      (!strcmp(mode, "alu"))  { ndisp = 20;   gw = 1024; gh = 1024; }
    else if (!strcmp(mode, "sad"))  { ndisp = 20;   gw = 1280; gh = 720;  }
    else if (!strcmp(mode, "tiny")) { ndisp = 2000; gw = 16;   gh = 16;   }
    else { fprintf(stderr, "unknown mode %s\n", mode); return 1; }

    // Instance. MoltenVK is a portability implementation: the loader hides it
    // unless the portability-enumeration bit and extension are passed. Both
    // are conditional on the extension existing, so the same source measures
    // delivered FLOPS on Linux/Windows drivers too (the Metal twin is the
    // macOS-only half; this half is the cross-platform ledger tool).
    const char *iexts[] = { "VK_KHR_portability_enumeration" };
    uint32_t niext = 0;
    vkEnumerateInstanceExtensionProperties(NULL, &niext, NULL);
    VkExtensionProperties *ieps = malloc(niext * sizeof *ieps);
    vkEnumerateInstanceExtensionProperties(NULL, &niext, ieps);
    int portability = 0;
    for (uint32_t i = 0; i < niext; i++)
        if (!strcmp(ieps[i].extensionName, "VK_KHR_portability_enumeration"))
            portability = 1;
    VkApplicationInfo ai = { .sType = VK_STRUCTURE_TYPE_APPLICATION_INFO,
        .apiVersion = VK_API_VERSION_1_1 };
    VkInstanceCreateInfo ici = { .sType = VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO,
        .pApplicationInfo = &ai,
        .flags = portability ? 0x00000001u : 0, /* ..._ENUMERATE_PORTABILITY_BIT_KHR */
        .enabledExtensionCount = portability ? 1u : 0, .ppEnabledExtensionNames = iexts };
    VkInstance inst;
    CHK(vkCreateInstance(&ici, NULL, &inst));

    uint32_t ndev = 1; VkPhysicalDevice pdev;
    VkResult er = vkEnumeratePhysicalDevices(inst, &ndev, &pdev);
    if (er != VK_SUCCESS && er != VK_INCOMPLETE) { fprintf(stderr, "no device\n"); return 1; }
    VkPhysicalDeviceProperties props;
    vkGetPhysicalDeviceProperties(pdev, &props);
    fprintf(stderr, "# device: %s\n", props.deviceName);

    uint32_t nqf = 0;
    vkGetPhysicalDeviceQueueFamilyProperties(pdev, &nqf, NULL);
    VkQueueFamilyProperties qfp[16];
    if (nqf > 16) nqf = 16;
    vkGetPhysicalDeviceQueueFamilyProperties(pdev, &nqf, qfp);
    uint32_t qf = 0;
    for (uint32_t i = 0; i < nqf; i++)
        if (qfp[i].queueFlags & VK_QUEUE_COMPUTE_BIT) { qf = i; break; }

    // portability_subset must be enabled when advertised.
    uint32_t next = 0;
    vkEnumerateDeviceExtensionProperties(pdev, NULL, &next, NULL);
    VkExtensionProperties *eps = malloc(next * sizeof *eps);
    vkEnumerateDeviceExtensionProperties(pdev, NULL, &next, eps);
    const char *dexts[1]; uint32_t ndexts = 0;
    for (uint32_t i = 0; i < next; i++)
        if (!strcmp(eps[i].extensionName, "VK_KHR_portability_subset"))
            { dexts[0] = "VK_KHR_portability_subset"; ndexts = 1; }

    float prio = 1.0f;
    VkDeviceQueueCreateInfo qci = { .sType = VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO,
        .queueFamilyIndex = qf, .queueCount = 1, .pQueuePriorities = &prio };
    VkDeviceCreateInfo dci = { .sType = VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO,
        .queueCreateInfoCount = 1, .pQueueCreateInfos = &qci,
        .enabledExtensionCount = ndexts, .ppEnabledExtensionNames = dexts };
    VkDevice dev; CHK(vkCreateDevice(pdev, &dci, NULL, &dev));
    VkQueue queue; vkGetDeviceQueue(dev, qf, 0, &queue);

    // Three r32f storage images.
    VkImage imgs[3]; VkDeviceMemory mems[3]; VkImageView views[3];
    VkPhysicalDeviceMemoryProperties mp;
    vkGetPhysicalDeviceMemoryProperties(pdev, &mp);
    for (int k = 0; k < 3; k++) {
        VkImageCreateInfo ic = { .sType = VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO,
            .imageType = VK_IMAGE_TYPE_2D, .format = VK_FORMAT_R32_SFLOAT,
            .extent = { IMG_W, IMG_H, 1 }, .mipLevels = 1, .arrayLayers = 1,
            .samples = VK_SAMPLE_COUNT_1_BIT, .tiling = VK_IMAGE_TILING_OPTIMAL,
            .usage = VK_IMAGE_USAGE_STORAGE_BIT,
            .initialLayout = VK_IMAGE_LAYOUT_UNDEFINED };
        CHK(vkCreateImage(dev, &ic, NULL, &imgs[k]));
        VkMemoryRequirements mr; vkGetImageMemoryRequirements(dev, imgs[k], &mr);
        uint32_t mti = 0;
        for (uint32_t i = 0; i < mp.memoryTypeCount; i++)
            if ((mr.memoryTypeBits & (1u << i)) &&
                (mp.memoryTypes[i].propertyFlags & VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT))
                { mti = i; break; }
        VkMemoryAllocateInfo ma = { .sType = VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO,
            .allocationSize = mr.size, .memoryTypeIndex = mti };
        CHK(vkAllocateMemory(dev, &ma, NULL, &mems[k]));
        CHK(vkBindImageMemory(dev, imgs[k], mems[k], 0));
        VkImageViewCreateInfo vc = { .sType = VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO,
            .image = imgs[k], .viewType = VK_IMAGE_VIEW_TYPE_2D,
            .format = VK_FORMAT_R32_SFLOAT,
            .subresourceRange = { VK_IMAGE_ASPECT_COLOR_BIT, 0, 1, 0, 1 } };
        CHK(vkCreateImageView(dev, &vc, NULL, &views[k]));
    }

    // Descriptors: one set, three storage images.
    VkDescriptorSetLayoutBinding binds[3];
    for (int k = 0; k < 3; k++)
        binds[k] = (VkDescriptorSetLayoutBinding){ .binding = (uint32_t)k,
            .descriptorType = VK_DESCRIPTOR_TYPE_STORAGE_IMAGE, .descriptorCount = 1,
            .stageFlags = VK_SHADER_STAGE_COMPUTE_BIT };
    VkDescriptorSetLayoutCreateInfo slci = { .sType = VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_CREATE_INFO,
        .bindingCount = 3, .pBindings = binds };
    VkDescriptorSetLayout dsl; CHK(vkCreateDescriptorSetLayout(dev, &slci, NULL, &dsl));
    VkDescriptorPoolSize ps = { VK_DESCRIPTOR_TYPE_STORAGE_IMAGE, 3 };
    VkDescriptorPoolCreateInfo pci = { .sType = VK_STRUCTURE_TYPE_DESCRIPTOR_POOL_CREATE_INFO,
        .maxSets = 1, .poolSizeCount = 1, .pPoolSizes = &ps };
    VkDescriptorPool pool; CHK(vkCreateDescriptorPool(dev, &pci, NULL, &pool));
    VkDescriptorSetAllocateInfo dsa = { .sType = VK_STRUCTURE_TYPE_DESCRIPTOR_SET_ALLOCATE_INFO,
        .descriptorPool = pool, .descriptorSetCount = 1, .pSetLayouts = &dsl };
    VkDescriptorSet set; CHK(vkAllocateDescriptorSets(dev, &dsa, &set));
    VkDescriptorImageInfo dii[3]; VkWriteDescriptorSet wds[3];
    for (int k = 0; k < 3; k++) {
        dii[k] = (VkDescriptorImageInfo){ .imageView = views[k],
            .imageLayout = VK_IMAGE_LAYOUT_GENERAL };
        wds[k] = (VkWriteDescriptorSet){ .sType = VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET,
            .dstSet = set, .dstBinding = (uint32_t)k, .descriptorCount = 1,
            .descriptorType = VK_DESCRIPTOR_TYPE_STORAGE_IMAGE, .pImageInfo = &dii[k] };
    }
    vkUpdateDescriptorSets(dev, 3, wds, 0, NULL);

    VkPipelineLayoutCreateInfo plci = { .sType = VK_STRUCTURE_TYPE_PIPELINE_LAYOUT_CREATE_INFO,
        .setLayoutCount = 1, .pSetLayouts = &dsl };
    VkPipelineLayout pl; CHK(vkCreatePipelineLayout(dev, &plci, NULL, &pl));

    VkPipeline pipes[2]; const char *files[2] = { "init.spv", NULL };
    char kern[64]; snprintf(kern, sizeof kern, "%s.spv", mode); files[1] = kern;
    for (int k = 0; k < 2; k++) {
        size_t len; void *code = read_file(files[k], &len);
        VkShaderModuleCreateInfo smci = { .sType = VK_STRUCTURE_TYPE_SHADER_MODULE_CREATE_INFO,
            .codeSize = len, .pCode = code };
        VkShaderModule sm; CHK(vkCreateShaderModule(dev, &smci, NULL, &sm));
        VkComputePipelineCreateInfo cpci = { .sType = VK_STRUCTURE_TYPE_COMPUTE_PIPELINE_CREATE_INFO,
            .stage = { .sType = VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_CREATE_INFO,
                .stage = VK_SHADER_STAGE_COMPUTE_BIT, .module = sm, .pName = "main" },
            .layout = pl };
        CHK(vkCreateComputePipelines(dev, VK_NULL_HANDLE, 1, &cpci, NULL, &pipes[k]));
        vkDestroyShaderModule(dev, sm, NULL);
        free(code);
    }

    VkCommandPoolCreateInfo cpc = { .sType = VK_STRUCTURE_TYPE_COMMAND_POOL_CREATE_INFO,
        .flags = VK_COMMAND_POOL_CREATE_RESET_COMMAND_BUFFER_BIT, .queueFamilyIndex = qf };
    VkCommandPool cmdpool; CHK(vkCreateCommandPool(dev, &cpc, NULL, &cmdpool));
    VkCommandBufferAllocateInfo cba = { .sType = VK_STRUCTURE_TYPE_COMMAND_BUFFER_ALLOCATE_INFO,
        .commandPool = cmdpool, .level = VK_COMMAND_BUFFER_LEVEL_PRIMARY, .commandBufferCount = 1 };
    VkCommandBuffer cb; CHK(vkAllocateCommandBuffers(dev, &cba, &cb));

    VkMemoryBarrier membar = { .sType = VK_STRUCTURE_TYPE_MEMORY_BARRIER,
        .srcAccessMask = VK_ACCESS_SHADER_WRITE_BIT,
        .dstAccessMask = VK_ACCESS_SHADER_READ_BIT | VK_ACCESS_SHADER_WRITE_BIT };

    // Setup submission: layouts to GENERAL, run init once.
    VkCommandBufferBeginInfo cbb = { .sType = VK_STRUCTURE_TYPE_COMMAND_BUFFER_BEGIN_INFO };
    CHK(vkBeginCommandBuffer(cb, &cbb));
    VkImageMemoryBarrier lbs[3];
    for (int k = 0; k < 3; k++)
        lbs[k] = (VkImageMemoryBarrier){ .sType = VK_STRUCTURE_TYPE_IMAGE_MEMORY_BARRIER,
            .srcAccessMask = 0, .dstAccessMask = VK_ACCESS_SHADER_WRITE_BIT,
            .oldLayout = VK_IMAGE_LAYOUT_UNDEFINED, .newLayout = VK_IMAGE_LAYOUT_GENERAL,
            .srcQueueFamilyIndex = VK_QUEUE_FAMILY_IGNORED,
            .dstQueueFamilyIndex = VK_QUEUE_FAMILY_IGNORED,
            .image = imgs[k],
            .subresourceRange = { VK_IMAGE_ASPECT_COLOR_BIT, 0, 1, 0, 1 } };
    vkCmdPipelineBarrier(cb, VK_PIPELINE_STAGE_TOP_OF_PIPE_BIT,
        VK_PIPELINE_STAGE_COMPUTE_SHADER_BIT, 0, 0, NULL, 0, NULL, 3, lbs);
    vkCmdBindPipeline(cb, VK_PIPELINE_BIND_POINT_COMPUTE, pipes[0]);
    vkCmdBindDescriptorSets(cb, VK_PIPELINE_BIND_POINT_COMPUTE, pl, 0, 1, &set, 0, NULL);
    vkCmdDispatch(cb, IMG_W / 16, IMG_H / 16, 1);
    vkCmdPipelineBarrier(cb, VK_PIPELINE_STAGE_COMPUTE_SHADER_BIT,
        VK_PIPELINE_STAGE_COMPUTE_SHADER_BIT, 0, 1, &membar, 0, NULL, 0, NULL);
    CHK(vkEndCommandBuffer(cb));
    VkSubmitInfo si = { .sType = VK_STRUCTURE_TYPE_SUBMIT_INFO,
        .commandBufferCount = 1, .pCommandBuffers = &cb };
    CHK(vkQueueSubmit(queue, 1, &si, VK_NULL_HANDLE));
    CHK(vkQueueWaitIdle(queue));

    // One batch = ndisp dispatches of the mode kernel with barriers between,
    // one submit, wall-clocked around submit+wait. Batch 0 is warm-up.
    for (int b = 0; b <= batches; b++) {
        CHK(vkBeginCommandBuffer(cb, &cbb));
        vkCmdBindPipeline(cb, VK_PIPELINE_BIND_POINT_COMPUTE, pipes[1]);
        vkCmdBindDescriptorSets(cb, VK_PIPELINE_BIND_POINT_COMPUTE, pl, 0, 1, &set, 0, NULL);
        for (int d = 0; d < ndisp; d++) {
            vkCmdDispatch(cb, (gw + 15) / 16, (gh + 15) / 16, 1);
            vkCmdPipelineBarrier(cb, VK_PIPELINE_STAGE_COMPUTE_SHADER_BIT,
                VK_PIPELINE_STAGE_COMPUTE_SHADER_BIT, 0, 1, &membar, 0, NULL, 0, NULL);
        }
        CHK(vkEndCommandBuffer(cb));
        double t0 = now_ms();
        CHK(vkQueueSubmit(queue, 1, &si, VK_NULL_HANDLE));
        CHK(vkQueueWaitIdle(queue));
        double t1 = now_ms();
        if (b > 0)
            printf("%s,vulkan,%.3f,%.4f\n", mode, t1 - t0, (t1 - t0) / ndisp);
    }
    return 0;
}
