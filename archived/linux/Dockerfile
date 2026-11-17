# The Linux research host in a container (2026-09-30: the owner's NAS as pooled compute -- TrueNAS, docker, an
# Intel Arc A310). The image carries only the toolchain and the Vulkan drivers; the sources, the builds and the
# scratch live in a volume, so the image can be rebuilt without losing a build. BUILDANDUSAGE.md's Linux section,
# as packages:
#   libshaderc-dev  -- libplacebo's runtime GLSL compiler; without it every custom hook silently fails to load
#   python3-jinja2  -- libplacebo's shader templates
#   mesa-vulkan-drivers -- ANV for the Arc (DG2) and lavapipe, the CPU witness, in one package
#   zlib1g-dev      -- without it ffmpeg's configure drops the PNG encoder, and the field reads are PNGs
#   python3-numpy   -- the harness's analysis
#
#   docker build -t nframe-build - < Dockerfile
FROM debian:trixie
RUN apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates git build-essential meson ninja-build pkg-config nasm \
      libvulkan-dev libshaderc-dev glslang-tools vulkan-tools mesa-vulkan-drivers \
      python3 python3-jinja2 python3-numpy \
      zlib1g-dev libdrm-dev cmake \
    && rm -rf /var/lib/apt/lists/*
# Vulkan headers NEWER than trixie's 1.4.309: libplacebo master (c42968d, 2026-09-23) uses the KHR names of the
# surface/swapchain maintenance1 extensions, which 1.4.309 only has as EXT, and fails to compile. Pinned to the
# version the Macs build against (Homebrew's vulkan-headers 1.4.357, 2026-09-30); into /usr/local, which gcc
# searches before /usr/include, with its own vk.xml for libplacebo's generator (build-linux.sh passes it).
ARG VKH=v1.4.357
RUN git clone --depth 1 -b "$VKH" https://github.com/KhronosGroup/Vulkan-Headers.git /tmp/vkh \
    && cmake -S /tmp/vkh -B /tmp/vkh/build -DCMAKE_INSTALL_PREFIX=/usr/local \
    && cmake --install /tmp/vkh/build && rm -rf /tmp/vkh
WORKDIR /work
