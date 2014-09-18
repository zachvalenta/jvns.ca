---
layout: post
title: "You can be a kernel hacker!"
date: 2014-09-18 14:20:56 -0400
comments: true
categories: kernel
---

When I started [Hacker School](https://hackerschool.com), I wanted to
learn how the Linux kernel works. I'd been using Linux for ten years,
but I still didn't understand very well what my kernel did. While
there, I found out that:

* the Linux kernel source code isn't all totally impossible to
  understand
* kernel programming is not just for wizards, it can also be for me!
* systems programming is REALLY INTERESTING
* I could write toy kernel modules, for fun!
* and, most surprisingly of all, all of this stuff was *useful*

I hadn't been doing low level programming at all -- I'd written a
little bit of C in university, and otherwise had been doing web
development and machine learning. But it turned out that my newfound
operating systems knowledge helped me solve regular programming tasks
more easily.

I also now feel like if I were to be put on *Survivor: fix a bug in my
kernel's USB driver*, I'd stand a chance of not being immediately
kicked off the island.

<!-- more -->

This is all going to be about Linux, but a lot of the same concepts
apply to OS X. We'll talk about

* what even is a kernel?
* why bother learning about this stuff?
* A few strategies for understanding the Linux kernel better, on your own
  terms:
    * strace all the things!
    * Read some kernel code!
    * Write a fun kernel module!
    * Do the Eudalypta challenge

### What even is a kernel?

When I started Hacker School I did not understand very well what a
kernel did. In a few words:

**A kernel is a program that knows how to interact with your hardware**.

Linux is mostly written in C, with bit of assembly. Let's say you go
to http://google.com in your browser. That requires typing, sending
data over a network, allocating some memory, and maybe writing some
cache files. The kernel has code that

* interprets your keypresses every time you press a key
* speaks the TCP/IP protocol, for sending information over the network
  to Google
* communicates with your hard drive to write bytes to it
* understands how your filesystem is implemented (what do the bytes on
  the hard drive even mean?!)
* gives CPU time to all the different processes that might be running
* speaks to your graphics card to display the page
* keeps track of all the memory that's been allocated
 
and much, much more. All of that code is running all the time you're
using your computer!

This is a lot to handle all at once! The only concept I want to you to
understand for the rest of this post is **system calls*. System calls
are your kernel's API -- regular programs that you write can interact
with your computer's hardware using system calls. A few example system
calls:

* `open` opens files
* `sendto` and `recvfrom` send and receive network data
* `write` writes to disk
* `chmod` changes the permissions of a file
* `brk` and `sbrk` allocate memory

So when you call the `open()` function in Python, somewhere down the
stack that eventually uses the `open` system call.

That's all you need to know about the kernel for now! It's a big
program, and you interact with it using system calls.

### Why learn about the Linux kernel, anyway?

There are some obvious reasons: it's really fun! Not everyone knows
about it! Saying you wrote a kernel module for fun is cool!

But there's a more serious reason: learning about the interface
between your operating system and your programs will **make you a
better programmer**. Let's see how!

#### Reason 1: strace

Imagine that you're writing a Python program, and it's meant to be
reading some data from a file `/user/bork/awesome.txt`. But it's not
working!

A pretty basic question is: is your program even opening the right
file? You could start using your regular debugging techniques to
investigate (print some things out! use a debugger!). But one amazing
thing is that on Linux, the *only way* to open a file is with the
`open` system call. You can get a list of all of these calls to `open`
(and therefore every file your program has opened) with a tool called
strace.

Let's do a quick example! Let's imagine I want to know what files
Chrome has opened!

```
$ strace -e open google-chrome
[... lots of output omitted ...]
open("/home/bork/.config/google-chrome/Consent To Send Stats", O_RDONLY) = 36
open("/proc/meminfo", O_RDONLY|O_CLOEXEC) = 36
open("/etc/opt/chrome/policies/managed/lastpass_policy.json", O_RDONLY) = 36
```

This is a really powerful tool for observing the *behavior* for a
program that we wouldn't have if we didn't understand some basics
about system calls. I use strace to:

* see if the file I *think* my program is opening is what it's
  *really* opening (system call: `read`)
* find out what log file my misbehaving poorly documented program is
  writing to (though I could also use `lsof`) (system call: `write`)
* spy on what data my program is sending over the network (system
  calls: `sendto` and `recvfrom`)
* find out every time my program opens a network connection (system
  call: `socket`)

I love strace so much I gave a lightning talk about just strace:
[Spying on your programs with strace](https://www.youtube.com/watch?v=4pEHfGKB-OE).

#### Reason 2: `/proc`

`/proc` lets you **recover your deleted files**, and is a great
example of how understanding your operating system a little better is
an amazing programming tool.

How does it do that? Let's imagine that we've written a program
[smile.c](TODO), and we're in the middle of running it. But then we
accidentally delete the binary!

The PID of that process right now is `8604`. I can find the
executable for that process at `/proc/8604/exe`:

```
 /proc/8604/exe -> /home/bork/work/talks/2014-09-strangeloop/smile (deleted)
```

It's `(deleted)`, but we can still look at it!
`cat /proc/8604/exe > recovered_smile` will recover our executable. Wow.

There's also a ton of other really useful information about processes
in `/proc`. Alex Clemmer has a wonderful post about
[how to detect what page your browser is on](TODO) by looking at `/proc`
to spy how its memory footprint is changing. How cool (and scary!)
is that?!

You can find out more with `man proc`. So fun!

#### Reason 3: ftrace

ftrace is totally different from strace. strace traces **system
calls** and ftrace traces **kernel functions**. Want to know 

TODO TODO TODO

#### Reason 4: perf

Your CPU has a whole bunch of different levels of caching (L1! L2!)
that can have really significant impacts on performance. `perf` is a
great tool that will tell you 
* how often the different caches are being used
* how many CPU cycles your program used (!!)

and a whole bunch of other performance information

#### Convinced yet?

Understanding your operating system better is *super useful* and will
make you a better programmer, even if you write Python. The most
useful tools for high-level programmers are `strace` and `/proc`. As
far as I can tell ftrace and perf are mostly useful for lower-level
programming.

Now you're hopefully convinced that learning more about Linux is worth
your time. Let's go over some strategies for understanding Linux
better!

### Strategy 1: strace all the things!

I mentioned `strace` before briefly. `strace` is literally my favorite
program in the universe. A great way to get a better sense for what
your kernel is doing is -- take a simple program that you understand
well (like `ls`), and run `strace` on it.

This will show you at what points the program is communicating with
your kernel. I took a 13 hour train ride from Montreal to New York
once and [straced killall](TODO) and it was REALLY FUN. Let's try
`ls`!

I ran `strace ls -o out` to save the output to a file. strace wlll
output a WHOLE BUNCH OF CRAP (todo: link to the crap). It turns out
that starting up a program is pretty complicated, and in this case
most of the system calls have to do with that. There's a lot of

* opening libraries: `open("/lib/x86_64-linux-gnu/libc.so.6",
  O_RDONLY|O_CLOEXEC)`
* putting those libraries into memory: `mmap(NULL, 2126312,
PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7faf507fc000
`

and a bunch of other things I don't really understand. My main
strategy when stracing for fun is to ignore all the crap at the
beginning, and just focus on what I understand. It turns out that `ls`
doesn't need to do a lot!

```
openat(AT_FDCWD, ".", O_RDONLY|O_NONBLOCK|O_DIRECTORY|O_CLOEXEC) = 3
getdents(3, /* 5 entries */, 32768)     = 136
getdents(3, /* 0 entries */, 32768)     = 0
close(3)                                = 0
fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 12), ...}) = 0
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7faf5104a000
write(1, "giraffe  out  penguin\n", 22) = 22
close(1)                                = 0
munmap(0x7faf5104a000, 4096)            = 0
close(2)                                = 0
exit_group(0)                           = ?
```

This is awesome! Here's what it needed to do:

1. Open the current directory: `openat(AT_FDCWD, ".",
   O_RDONLY|O_NONBLOCK|O_DIRECTORY|O_CLOEXEC)`
2. Get the contents of that directory: `getdents(3, /* 5 entries */,
   32768) = 136`. Looks like it was 136 bytes of stuff!
3. Close the directory: `close(3)`
4. Write the files to standard out: `write(1, "giraffe out penguin\n",
   22) = 22`
5. Close a bunch of things to clean up.

That was really simple, and we already learned a new system call! That
mmap in the middle there? No idea what that does. But it's totally
fine! STRACE IS THE BEST.

So! Running strace on random processes and looking up the
documentation for system calls you don't recognize is an easy way to
learn a ton!

**<span style='color:red'>Warning</span>**: **Don't** strace processes
that you actually need to run efficiently! strace is like putting a
huge stopsign in front of your process every time you use a system
call, which is **all the time**. TODO: link to Brendan Gregg's post.

todo: **strace is also a great debugging tool**

### Strategy 2: Read some kernel code!

Okay, let's imagine that we've gotten interested in `getdents`, and we
want to understand better what it actually does. There's this
fantastic tool called [livegrep](http://livegrep.com) that lets you
search through kernel code. It's by
[Nelson Elhage](http://twitter.com/nelhage) who is pretty great.

So let's use it to find the source for `getdents`!

### Strategy 3: Write a fun kernel module!

Kernel modules sound intimidating but they're actually really
approachable! All a kernel module is fundamentally is

1. An `init` function to run when the module is loaded
2. A `cleanup` function to run when the module is unloaded

You load kernel modules with `insmod` and unload them with `rmmod`.
Here's a working kernel module!

```
#include <linux/module.h>    // included for all kernel modules
#include <linux/kernel.h>    // included for KERN_INFO
#include <linux/init.h>      // included for __init and __exit macros

static int __init hello_init(void)
{
    printk(KERN_INFO "WOW I AM A KERNEL HACKERl!!!\n");
    return 0;    // Non-zero return means that the module couldn't be loaded.
}

static void __exit hello_cleanup(void)
{
  printk(KERN_INFO "I am dead.\n");
}

module_init(hello_init);
module_exit(hello_cleanup);
```

That's it! `printk` writes to the system log, and if you run `dmesg`,
you'll see what it printed!

Let's look at another fun kernel module! I gave a talk about kernel
hacing at [CUSEC](http://2014.cusec.net) in January, and I needed a
fun example. My friend [Tavish](https://twitter.com/tavarm) suggested
"hey julia! What if you made a kernel module that rick rolls you every
time you open a file?" And my awesome partner
[Kamal](https://twitter.com/kamalmarhubi) said "that sounds like fun!"
and inside a weekend he'd totally done it!

You can see the *extremely* well-commented source here:
[rickroll.c](https://github.com/jvns/blob/master/rickroll.c).
Basically what it needs to do when loaded is

* find the system call table (it turns out this is not trivial!)
* Disable write protection so that we're actually allowed to modify it
  (!!)
* Save the old `open` so we can put it back
* Replace the `open` system call with our own `rickroll_open` system
  call

That's it!

Here's the relevant code:

```
sys_call_table = find_sys_call_table();
DISABLE_WRITE_PROTECTION;
original_sys_open = (void *) sys_call_table[__NR_open];
sys_call_table[__NR_open] = (unsigned long *) rickroll_open;
ENABLE_WRITE_PROTECTION;
printk(KERN_INFO "Never gonna give you up!\n");
```

The `rickroll_open` function is also pretty understandable. Here's a
sketch of it, though I've left out some important implementation
details that you should totally read: [rickroll.c](TODO)

```
static char *rickroll_filename = "/home/bork/media/music/Rick Astley - Never Gonna Give You Up.mp3";
asmlinkage long rickroll_open(const char __user *filename, int flags, umode_t mode) {
    if(strcmp(filename + len - 4, ".mp3")) {
        /* Just pass through to the real sys_open if the extension isn't .mp3 */
        return (*original_sys_open)(filename, flags, mode);
    } else {
        /* Otherwise we're going to hijack the open */ fd =
        (*original_sys_open)(rickroll_filename, flags, mode); return
        fd; } }
```

SO FUN RIGHT. The source is super well documented and interesting and
you should [go read it](TODO). And if you think "but Kamal must be a
kernel hacking wizard! I could never do that!", it is not so! Kamal is
pretty great, but he had never written kernel code before that
weekend. I understand that he googled things like "how to hijack
system call table linux". You could do the same!

Kernel modules are an especially nice way to start because writing toy
kernel modules plays nicely into writing real kernel modules like
hardware drivers. Or you could start out writing drivers right away!
Whatever floats your boat :) The reference for learning about writing
drivers is called [Linux Device Drivers](TODO) or "LDD3". The fabulous
Jessica McKellar is writing the new version, LDD4. TODO

### Strategy 5: Read linux.org

TODO: find some baller articles by Valerie Aurora

### Strategy 5: Do the Eudalypta challenge

If you don't have an infinite number of ideas for hilarious kernel
module pranks to play on your friends (I don't!), there's a challenge
specifically built to help you get started with kernel programming,
with progressively harder steps. The first one is to just write a
"hello world" kernel module, and we already know how to do that!

They're pretty strict about the way you send email (helping you
practice for the linux kernel mailing list, maybe!). I haven't tried
it myself yet, but [Alex Clemmer](http://nullspace.io) tells me that
it is hard but possible.



### Strategy 6: Do an internship

If you're really serious about all this, there are a couple pf
programs I know of where you can do

* Google Summer of Code, for students
* The GNOME outreach program for women

OPW is a 

### Resources

To recap, here are the super useful resources for learning that I've
mentioned:

* LDD3/4
* the kernel newbies website
* A few fun kernel modules I wrote
* the eudalypta challenge
* the OPW website
* Linux Weekly News
  ([here's an index](http://lwn.net/Archives/GuestIndex/))

### You can be a kernel hacker

I'm not a kernel hacker, really. But now when I look at awesome actual
kernel hackers like [Valerie Aurora]() or [Sarah Sharp](), I no longer
think that they're wizards. I now think those are people who worked
really hard on becoming better at kernel programming, and did it for a
long time! And if I spent a lot of time working on learning more, I
could be a kernel hacker too.

And so could you.
