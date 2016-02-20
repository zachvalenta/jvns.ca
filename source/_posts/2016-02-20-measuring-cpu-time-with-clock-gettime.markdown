---
layout: post
title: "A better way to measure CPU time: clock_gettime"
date: 2016-02-20 10:13:31 -0500
comments: true
categories: 
---

At work yesterday, someone sent an email saying "Hey we're measuring how much CPU time every HTTP request takes now!". I am [very interested in measuring CPU time](http://jvns.ca/blog/2016/02/07/cpu-load-averages/). But I didn't know how to accomplish what they said they'd just done. So I asked "hey how does that work?". Here's the answer.

It turns out that if you want to know exactly how much CPU time your HTTP requests are taking, you can just ask the Linux kernel!

On Linux, there's a system call (and corresponding libc function) called [`clock_gettime`](http://linux.die.net/man/3/clock_gettime). I'd seen this system call before, but I thought it was only for getting the time, like 5:03pm. Not so! Here are the flags you can send to `clock_gettime` on my system. (from `man clock_gettime`).

```
       CLOCK_REALTIME
              System-wide  real-time  clock.    Setting   this   clock
              requires appropriate privileges.

       CLOCK_MONOTONIC
              Clock  that  cannot be set and represents monotonic time
              since some unspecified starting point.

       CLOCK_MONOTONIC_RAW (since Linux 2.6.28; Linux-specific)
              Similar to CLOCK_MONOTONIC, but provides access to a raw
              hardware-based  time  that is not subject to NTP adjust‐
              ments.

       CLOCK_PROCESS_CPUTIME_ID
              High-resolution per-process timer from the CPU.
    
       CLOCK_THREAD_CPUTIME_ID
              Thread-specific CPU-time clock.
```

So if you ask your kernel for `CLOCK_PROCESS_CPUTIME_ID`, it will tell you how much CPU time has passed since your program started. This is awesome, because you can run

```
start_time = clock_gettime(CLOCK_PROCESS_CPUTIME_ID)
do_maybe_expensive_thing
end_time = clock_gettime(CLOCK_PROCESS_CPUTIME_ID)
print "elapsed CPU time:", end_time - start_time
```

And you can [call clock_gettime from Ruby to understand your Ruby performance!](http://tmm1.net/ruby21-process-clock_gettime/). System calls aren't just for C hackers, they're for everyone.

In hindsight, it makes sense to me that Linux keeps track of the CPU time spent
per process. `ps aux` reports how much CPU time every program on your system has
used (in the `TIME` column), and if you time a program with `time`, it reports
the total time, userspace CPU time, and kernel CPU time separately.

It's also interesting that this system call lets you get a monotonic time -- that seems useful if you want a notion of time that doesn't [go back in time](http://jvns.ca/blog/2016/02/09/til-clock-skew-exists/).