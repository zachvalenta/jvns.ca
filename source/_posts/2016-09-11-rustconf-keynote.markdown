---
layout: post
title: "rustconf keynote"
date: 2016-09-11 10:45:47 -0400
comments: true
categories: 
---
<style>

.container {
	display: flex;
}
.slide {
	width: 50%;
}
.content {
	width: 50%;
	align-items: center;
	padding: 20px;
}

@media (max-width: 480px) { /*breakpoint*/
    .container {
        display: block;
    }
    .slide {
    	width: 100%;
    }
}

</style>




<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_01.png"><img src="/images/rust-talk/slide_01_small.png"></a>
</div>
<div class="content">

Who learned something awesome today at RustConf? Everyone? AMAZING.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_02.png"><img src="/images/rust-talk/slide_02_small.png"></a>
</div>
<div class="content">

These are the 4 themes I want to talk about in this talk! Let's go.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_03.png"><img src="/images/rust-talk/slide_03_small.png"></a>
</div>
<div class="content">

A lot of people love Rust for these 3 reasons. And more! memory safety without garbage collection! These are great reasons to love Rust.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_04.png"><img src="/images/rust-talk/slide_04_small.png"></a>
</div>
<div class="content">
But that's not why I love Rust. I'm kind of a beginner Rust programmer, my understanding of the borrow checker is flaky, I've written maybe 1000 lines of Rust code, and I'm not writing any production Rust code.

<br><br>
I spend a lot of my time on a comet very far away from Rust. So why am I talking to you right now?
</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_05.png"><img src="/images/rust-talk/slide_05_small.png"></a>
</div>
<div class="content">


I care a lot about learning about systems, and I've spent a lot of my time doing that. I love doing experiments with programming, and I think Rust is a super good platform for experiments. And the community has helped me out!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_06.png"><img src="/images/rust-talk/slide_06_small.png"></a>
</div>
<div class="content">

When Aaron invited me to give this talk (which was, like, the best day ever), he wrote

<p>
"We see the language as empowering for a wide variety of people who
might not otherwise consider themselves systems programmers."
</p>

And the person who doesn't consider themselves as a systems programmer! That has TOTALLY BEEN ME. So let's talk about experiments and empowement.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_07.png"><img src="/images/rust-talk/slide_07_small.png"></a>
</div>
<div class="content">

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_08.png"><img src="/images/rust-talk/slide_08_small.png"></a>
</div>
<div class="content">

I do a lot of programming experiments to learn more about programming. My goal with these experiments usually isn't to produce anything of value. Instead I just want to learn something!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_09.png"><img src="/images/rust-talk/slide_09_small.png"></a>
</div>
<div class="content">

In 2013, I'd been working as a programmer for 2 years, I had 2 CS degrees, and I knew all kinds of things about computer science. But there was still SO MUCH I didn't know.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_10.png"><img src="/images/rust-talk/slide_10_small.png"></a>
</div>
<div class="content">

In particular, I didn't know anything really about how the Linux kernel worked, even though I'd been using Linux for 8 years. I think I'd never heard the words "system call".

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_11.png"><img src="/images/rust-talk/slide_11_small.png"></a>
</div>
<div class="content">

<p>
</p>
So I went to the Recurse Center! RC is a 12-week programming retreat in New York where you go to learn whatever you want about programming. 

<p>
It's totally self-directed, and while I was there I ended up spending a lot of time learning about operating systems, because that was the most confusing thing I could find to work on.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_12.png"><img src="/images/rust-talk/slide_12_small.png"></a>
</div>
<div class="content">

On my <a href="http://jvns.ca/blog/2013/10/02/day-3-what-does-the-linux-kernel-even-do/">third day </a> at RC, I learned what the Linux kernel does! I found out what a system call is! 

<p>
It turns out it had a pretty simplex explanation -- your operating system knows how to do things like open files, you program does not, so your program asks your operating system to do things with system calls! Like `open`.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_13.png"><img src="/images/rust-talk/slide_13_small.png"></a>
</div>
<div class="content">

Three weeks before the end of my time there, I decided to write an operating system. Lindsey Kuper suggested I try Rust, which I was also a beginner at, so I tried that!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_14.png"><img src="/images/rust-talk/slide_14_small.png"></a>
</div>
<div class="content">
<p>
It turns out that writing an operating system in Rust is actually impossible, so I reduced my scope a lot -- I decided to just write a keyboard driver from scratch. So my goal was, when I typed a key on my keyboard, that key would appear on my screen!
</p>
<p>
Turns out that this is not at all trivial.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_15.png"><img src="/images/rust-talk/slide_15_small.png"></a>
</div>
<div class="content">

<p>
So, one of the themes for this talk was "you can contribute without coding". I
really believe in this -- I think that code contributions are great, don't get
me wrong.
</p>

<p>
But I have basically never contributed code to an open source
project (even though I'm a programmer!) and I think I've contributed a lot to
open source communities.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_16.png"><img src="/images/rust-talk/slide_16_small.png"></a>
</div>
<div class="content">

<p>
When I started doing this I discovered a really surprising thing. At the time I was writing blog posts every day about what I'd learned that day.
</p>

<p>
And even though I was a beginner to both Rust and operating systems development, it turned out that some of these blog posts were really popular! People were learning from them!
</p>

<p>I wrote buzzfeed-style posts like "12 things I learned today about linkers", <a href="http://jvns.ca/blog/2013/12/04/day-37-how-a-keyboard-works/">After 5 days, my OS doesn't crash when I press a key</a>, <a href="http://jvns.ca/blog/2013/12/13/day-42-how-to-run-an-elf-executable-i-dont-know/">How to run a simple ELF executable, from scratch (I don't know)</a>, and a lot more.
</p>

<p>
So this is interesting, right! To teach people it turns out you don't have to be an expert at all. Maybe it's actually even better to be a beginner!
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_17.png"><img src="/images/rust-talk/slide_17_small.png"></a>
</div>
<div class="content">

Niko made this comment "if it's not documented, it might as well not exist" in his keynote this morning. And I think this is really true. If there's an amazing program in the world, but you don't know about it.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_18.png"><img src="/images/rust-talk/slide_18_small.png"></a>
</div>
<div class="content">

<p>
My friend Maya jokes that I'm basically developer relations for strace.
</p>

<p>
This happened because in 2013, someone told me about strace, a program I love that traces system calls. And I was so shocked that I hadn't known about it before! So I started telling everyone.
</p>

<p>
And now all kinds of people know about strace because of me, and they have a new useful tool! So that basically makes me the inventor of strace for those people, right? :)
</p>

<p>
I like doing this in my spare time because I write code at work, so it's a really nice change of pace.
</p>
</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_19.png"><img src="/images/rust-talk/slide_19_small.png"></a>
</div>
<div class="content">

<p>
Writing code is a lot of work. And when you write the code, if you want people to use it, it's a lot of work to tell people about it!
</p>

<p>
So I like to skip the whole first step of writing code, and just tell people about awesome things that already exist. I'm like the most productive software developer ever.
</p>
</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_21.png"><img src="/images/rust-talk/slide_21_small.png"></a>
</div>
<div class="content">

<p>
Let's switch gears and talk about learning systems programming.
</p>
<p>
My coworker asked me the other day "I'm reading a book about Rust, what would be a good example program to write?". And this is a hard question to answer!
</p>
<p>
So here's a possible answer to that question. I think it's important to have a lot of answers like this, because there's so much to learn!
</p>
</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_22.png"><img src="/images/rust-talk/slide_22_small.png"></a>
</div>
<div class="content">

<p>
So one evening, I was at home, and I wanted to know more about concurrency.
</p>
</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_23.png"><img src="/images/rust-talk/slide_23_small.png"></a>
</div>
<div class="content">

<p>
But this isn't a very specific question! A better question is -- what are the systems primitives for concurrency?
</p>
<p>
I knew that a lot of concurrent programs used the same kind of functions and ideas and systems calls. So what were those things, and how did they work?
</p>
<p>
Many concurrent programs use operating systems threads, they need to control access to resources with mutexes, and sometimes they do these "atomic instruction" things.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_24.png"><img src="/images/rust-talk/slide_24_small.png"></a>
</div>
<div class="content">
<p>
My favorite way to start out exploring idea is to write a program that doesn't work.
</p>

<p>
It's easy to write unsafe programs in C, so I did it in C. I made 1000 threads that each incremented the same counter 1000 times. You should get 100000 at the end, right?
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_25.png"><img src="/images/rust-talk/slide_25_small.png"></a>
</div>
<div class="content">
<p>
Nope! Instead we get a data race! The answer is way less than a million. This is great! I was very happy already because I'd made a race and it worked. 
</p>

</div>
</div>



<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_26.png"><img src="/images/rust-talk/slide_26_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_27.png"><img src="/images/rust-talk/slide_27_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_28.png"><img src="/images/rust-talk/slide_28_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_29.png"><img src="/images/rust-talk/slide_29_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_30.png"><img src="/images/rust-talk/slide_30_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_31.png"><img src="/images/rust-talk/slide_31_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_32.png"><img src="/images/rust-talk/slide_32_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_33.png"><img src="/images/rust-talk/slide_33_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_34.png"><img src="/images/rust-talk/slide_34_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_35.png"><img src="/images/rust-talk/slide_35_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_36.png"><img src="/images/rust-talk/slide_36_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_37.png"><img src="/images/rust-talk/slide_37_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_38.png"><img src="/images/rust-talk/slide_38_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_39.png"><img src="/images/rust-talk/slide_39_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_40.png"><img src="/images/rust-talk/slide_40_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_41.png"><img src="/images/rust-talk/slide_41_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_42.png"><img src="/images/rust-talk/slide_42_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_43.png"><img src="/images/rust-talk/slide_43_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_44.png"><img src="/images/rust-talk/slide_44_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_45.png"><img src="/images/rust-talk/slide_45_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_46.png"><img src="/images/rust-talk/slide_46_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_47.png"><img src="/images/rust-talk/slide_47_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_48.png"><img src="/images/rust-talk/slide_48_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_49.png"><img src="/images/rust-talk/slide_49_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_50.png"><img src="/images/rust-talk/slide_50_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_51.png"><img src="/images/rust-talk/slide_51_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_52.png"><img src="/images/rust-talk/slide_52_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_53.png"><img src="/images/rust-talk/slide_53_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_54.png"><img src="/images/rust-talk/slide_54_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_55.png"><img src="/images/rust-talk/slide_55_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_56.png"><img src="/images/rust-talk/slide_56_small.png"></a>
</div>
<div class="content">
<p>
</p>
<p>
</p>

</div>
</div>