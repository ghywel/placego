This gist is it gives scientists a completely new way to 'look at' or 'see' the results of experimental data that simply wasn't possible before. Or if it was possible, it took ages and needed a lot of very expensive equipment. A 'shader' is a computer program that runs on your GPU, just as a computer program runs on your CPU. The difference is that a CPU does a lot of general purpose tasks (somewhat threaded - meaning doing more than one thing at the same time) whilst a GPU does a lot of highly specialist math tasks, massively in parallel, practically all at once.

"CPU code" is most of everything that the computer you are reading this on does today. It is the general purpose work-horse that turns on your computer, figures out what hardware you have got, shuffles some data around in memory, gives the user a way to interact with the system (GUI - point and click / Terminal - write commands), run 'programs' from some 'disk' storage, run lots of 'programs' at the same time called processes, and let each process have it's turn on the CPU so no one process hogs it and prevents the other ones running. This is the operating system.

CPU source code is all over and everywhere, especially "Open Source" projects - People who work together on code in public to make something cool that anybody can use - The greatest example being Linus Torvalds who made an entire operating system, Linux from scratch. Source code is (usually) obvious what it does, especially if you are reading from modern script languages such as Python. The language is a human-abstraction that makes it possible for a human to read and write it. Computer's themselves only 'read' binary, 1's and 0's which is meaningless to a human. Assembly was the first language to start to abstract binary to make it more readable.
```
    MOV AL, 61h
```
MOV for move, AL is a bit of memory, 61(hexidecimal) is just a number. Put number in memory. All other languages build on this abstraction to make it more obvious to a human what the code does, which makes it easier to write. Higher level languages are closer to human language - and working with Claude Code is the highest abstraction possible. The prompt "Make me an app that does XYZ" itself is code.

GPU source code - 'shaders' - are what makes your graphics card work. It is mostly responsible for generating the image on your screen and working with graphics - from the content inside a web browser to playing Minecraft. The problem is shaders only run extremely complicated matrix math which is near incomprehensible to a human and not obvious what it does. There is no way to simplify a shader because that is not how shaders work.
```
    //!HOOK LUMA
    //!HOOK RGB
    //!BIND HOOKED
    
    vec4 hook()
    {
    vec4 color = HOOKED\_texOff(0);
    color.rgb = vec3(1.0) - color.rgb;
    
    return color;
    }
```
This is an extremely simple example of a shader - which inverts all the colours. Unlike python, you can stare at this, read it backwards and forwards and upside down and still not understand what it does. I will explain.

HOOK means 'When should i run this program'

BIND means 'What is my pixel input' - note: a running piece of shader code does not see the whole image - it is given it's own specific pixel from the image to work with.

vec4 means a matrix, a mathematical object which places related numbers together (r, g, b, a) / (0.34 , 0.67, 0.11, 1)

color = my original color

make a new matrix (1, 1, 1), subtract my current colour from it (1-0.34, 1-0.67, 1-0.11, 1), and set my output pixel to the new color

Do you see the problem. This is the simplest example of shader source code we could possibly make and it's already extremely confusing.

There are lot's of online communities (such as https://www.shadertoy.com) where people write shaders for fun and you can see more complicated working examples. They are extremely cool, extremely powerful, and very fun to look at. Shaders don't actually care if you are working with an image. The massively parallel matrix math can be applied to absolutely anything and is also what makes all AI systems work today. Let us say you have a massive data set and you need to crunch some numbers. You could submit the work to the CPU, which is usually fast and current generations have large numbers of threaded cores, making it somewhat parallel. However, it is practically always more efficient to do the work in a shader, especially when the number crunch is not sequential and doesn't require the previous number to do it's work. Ie if all you are running is (a-b, c-d, e-f .... ∞) you submit the whole job to the GPU in one go and let at massively parallelly compute.

Where this all fit's in here is I discovered that Claude Code Opus 5 / Fable 5 is extremely good at writing them.

Human languages are messy. They weren't "made" they evolve naturally over time. Words come and go, meanings change, people make up new words, there are many languages. All human language are filled with exceptions, logical inconsistencies, deviations from the rule, slang, memes and esoteric idioms that don't make any sense to anybody not in-the-know or out-of-the-loop.

Computer languages are mathematical, logical and wholly and completely consistent (except when they break down) because we intentionally designed them that way. Nature gets evolution which works but is messy. Computers get raw math. All a CPU/GPU really is, is a machine that counts very quickly, remembers what it has already calculated, and can be 'programmed' to do something useful with the math it is working on.

It is natural therefore that AI is extremely, ridiculously good at reading and writing them. And for the first time we can prove it can write the GPU programs as well as CPU programs all by itself. This is Claude Code. There are other vendor products on the market, but Claude is the one that worked for me. It does all the detail of the coding for me so I don't have to, which allows me to construct experiments in 5 minutes, and invent an entirely new subclass of scientific inquiry in one week, called n-frame.

Any further questions let me know, I am happy to answer if i can, this exercise I am deliberately doing this in public on reddit, because i think real people should get to experience science live, and not just hear about it on the news.