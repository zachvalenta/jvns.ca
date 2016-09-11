---
layout: post
title: "Learning systems programming with Rust"
date: 2016-09-11 10:45:47 -0400
comments: true
categories: 
---
<style>

.container {
	display: flex;
}
.slide {
	width: 40%;
}
.content {
	width: 60%;
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


I did the closing keynote at the first RustConf yesterday, on Rust and systems
programming and accessibility and learning about concurrency and why I write
about programming and a bunch other things.

Here's a transcript of that talk (where when I say "transcript") I mean "more
less what I said, kinda".

You can click on any of the slides to see a big version.

<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_01.png"><img src="/images/rust-talk/slide_01_small.png"></a>
</div>
<div class="content">

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
So one of the first ways to work on concurrency is mutexes, or locks. You and all the other threads have one place where you go to control who's allowed to update the counter.
</p>
<p>
I like this as a simple example because you can just get it to work and move on, or, if you want, you can go a lot deeper.
</p>
<p>
For example! To use mutexes, underneath you often use a function called pthread_mutex_lock. And it turns out that sometimes that uses the futex system call, and sometimes it doesn't! So there's all kinds of hidden complexity.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_27.png"><img src="/images/rust-talk/slide_27_small.png"></a>
</div>
<div class="content">
<p>
The next thing I want to talk about is atomic instructions. Basically your CPU knows how to increment counters without races -- if you say "lock inc" then it will make sure that the counter gets incremented exactly once.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_28.png"><img src="/images/rust-talk/slide_28_small.png"></a>
</div>
<div class="content">
<p>
So now we have a nice small exercise! This is not really that hard to do in Rust, but it introduces a lot of new ideas.
</p>
<p>
And there are a lot of opportunities for questions, right? Like, are mutexes or atomics faster? How much? Why? I love problems that you can finish pretty easily, but take farther if you want.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_29.png"><img src="/images/rust-talk/slide_29_small.png"></a>
</div>
<div class="content">
<p>
Now we're onto the last part of the talk.
</p>
<p>
I originally wrote "impossible problems" here. But of course all programs are technically *possible* to write!
</p>
<p>
As we're going to learn shortly, though, right now I really do not know C, and I have a day job, and so my free time for programming is not unlimited. So even if a program is *possible* for me to write, if I have to write it in C/C++, probably in practice it's not going to happen.
</p>
<p>
I'm going to tell you about how Rust helped me write a program that I wanted to write, that would have been improbable otherwise.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_30.png"><img src="/images/rust-talk/slide_30_small.png"></a>
</div>
<div class="content">
<p>
This where we get back to EMPOWERMENT.
</p>
</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_31.png"><img src="/images/rust-talk/slide_31_small.png"></a>
</div>
<div class="content">

<p>
So, here's the problem I was mad about. I'd run "top" on my computer, and it would tell me Ruby was using all the CPU, and I wouldn't know why.
</p>
</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_32.png"><img src="/images/rust-talk/slide_32_small.png"></a>
</div>
<div class="content">
<p>
And the reason this made me mad, is that I could see what other programs like Chrome were doing with  <a href="http://jvns.ca/blog/2016/02/24/perf-top-my-new-best-friend/">perf top</a>
</p>
<p>
(cool demo of perf top goes here)
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_33.png"><img src="/images/rust-talk/slide_33_small.png"></a>
</div>
<div class="content">
<p>
So I wanted to write a program that I could just give the PID of a Ruby process, and it would tell me the top Ruby functions that were running right now.
</p>
<p>
Is that possible? My friend Julian claimed this was totally possible and easy. So eventually I decided to try.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_34.png"><img src="/images/rust-talk/slide_34_small.png"></a>
</div>
<div class="content">
<p>
To do this from the outside, you have to basically spy on the internals of a running Ruby process.
</p>
<p>
The system call I used to spy is called process_vm_readv.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_35.png"><img src="/images/rust-talk/slide_35_small.png"></a>
</div>
<div class="content">
<p>
In the Ruby interpreter, you have the C stack. That has unhelpful things on it like "you're in vm_exec right now" which basically means "you're running a Ruby function"
</p>
<p>
BUT WHICH RUBY FUNCTION?!
</p>
<p>
But somewhere inside its memory, somewhere, you have the Ruby stack. That's what I wanted to get at.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_36.png"><img src="/images/rust-talk/slide_36_small.png"></a>
</div>
<div class="content">
<p>
I'm not going to go into the details of how this works because I don't have time, but I wrote a C demo of this program. I know how to write C! I can allocate memory in C! My demo kinda worked!
</p>
<p>
However, I do not really know how to *free* memory in C. Like, I technically know that there is a free function, but I don't have a lot of experience with it. So my program had some pretty serious memory issues almost right away.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_37.png"><img src="/images/rust-talk/slide_37_small.png"></a>
</div>
<div class="content">
<p>
At this point I asked my partner Kamal for some help translating my program to Rust.
</p>
<p>
At the time I used bindgen and it was awesome, it took maybe a day, and now I had a Rust program that did the same thing! Except I didn't have to know how to free memory anymore.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_38.png"><img src="/images/rust-talk/slide_38_small.png"></a>
</div>
<div class="content">
<p>
If you observe this highly scientific graph of "program workingness", you will see that my productivity went up.
</p>
<p>
I had to fight with the compiler a lot more, but I did not have to learn how to implement hashmaps from scratch. Win.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_39.png"><img src="/images/rust-talk/slide_39_small.png"></a>
</div>
<div class="content">
<p>
But I had one more problem. It turned out that I needed to know what the bytes in memory in my Ruby program *meant*. I wanted to know what the original struct definitions were so I could interpret all these 0s and 1s.
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
Luckily, sometimes the C compiler will save a bunch of debug information in a format called DWARF.
</p>
<p>
This basically has all the structs and saves them inside your programs! Yay! This is the best! I had hope again.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_41.png"><img src="/images/rust-talk/slide_41_small.png"></a>
</div>
<div class="content">
<p>
I needed a library for parsing DWARF, though. I started with trying libdwarf, and I got it maybe 90% working. But it was sort of a terrible experience.
</p>
<p>
The API was terrible, there were no docs that I could find, it was slow, I had a bad time linking the library into my Rust program.
</p>
<p>
One of the most upsetting things to me about this library is that it was really hard to understand how DWARF actually worked by looking at the interfaces it provided. I like knowing how things work.
</p>
</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_42.png"><img src="/images/rust-talk/slide_42_small.png"></a>
</div>
<div class="content">
<p>
A lot of the time when I have programming problems, I complain about them on Twitter. Somebody suggested I try a Rust library called 'gimli'.
</p>
<p>
One of the maintainers, Nick Fitzgerald, told me it wasn't done but he thought it might have all the features I needed! GREAT.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_43.png"><img src="/images/rust-talk/slide_43_small.png"></a>
</div>
<div class="content">
<p>
Using Gimli was a way better experience. It didn't have too much documentation either, but that was okay -- the example program they provided was really helpful, and explained how to do basically everything I needed to do.
</p>
<p>
The only thing it didn't do that I wanted was really small, and I submitted a tiny pull request to get it.
</p>
<p>
And the maintainers were really helpful! I understood DWARF better after I started working with Gimli.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_44.png"><img src="/images/rust-talk/slide_44_small.png"></a>
</div>
<div class="content">
<p>
"How does DWARF work" is a question pretty far out of the scope of this talk, but basically if your program is a train car (made of a bunch of ELF section), DWARF debug info is basically just a bunch of extra train cars tacked on to the end. One of the sections just basically has all the strings in your program concatenated together!
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
So, after this whole saga, we did it!! I worked on this a lot with Kamal and our ruby stacktrace program worked! It's <a href="https://github.com/jvns/ruby-stacktrace">on github</a> and everything. It works on 3 computers.
</p>
<p>
(insert cool demo here)
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_46.png"><img src="/images/rust-talk/slide_46_small.png"></a>
</div>
<div class="content">
<p>
I spend a lot of time being frustrated with the Rust compiler, but I still like it because it lets me do things I probably wouldn't get done otherwise.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_47.png"><img src="/images/rust-talk/slide_47_small.png"></a>
</div>
<div class="content">
<p>
I want to leave you with a few things.
</p>
<p>
One delightful thing about systems is that there's always SO MUCH MORE TO LEARN. I don't think there's any danger of any of knowing everything about systems programming any time soon.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_48.png"><img src="/images/rust-talk/slide_48_small.png"></a>
</div>
<div class="content">
<p>
I'm pretty sure all of you know cool things about programming that I don't know. If you like writing, this can be a great way to make the community around you know more!
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_49.png"><img src="/images/rust-talk/slide_49_small.png"></a>
</div>
<div class="content">
<p>
One thing I really want to emphasize is -- I see a ton of resources for beginners, and I think those are really awesome.
</p>
<p>
What I don't see as much of as I'd like is resources for people who know how to program, or know Rust, and really want to take their skills to the next level. I think the Rust community is really well placed to help people do this.
</p>
<p>
Writing down information like this for developers who might already have 5 or 10 years of experiences is where I spend almost all my time.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_50.png"><img src="/images/rust-talk/slide_50_small.png"></a>
</div>
<div class="content">
<p>
And while you're writing down cool things to help people level up -- remember that a lot of systems things aren't really that hard.
</p>
<p>
I think computer networking is a really good example of this -- a lot of people get really intimidated by networking, but a lot of the core concepts like IP addresses and ports and packets are not really that hard, and once you understand them you can learn a lot.
</p>
<p>
I wrote a zine called "linux debugging tools you'll love" that talks about ngrep, tcpdump, strace, etc. And somebody tweeted at me saying he was using it to teach his 8 year old! What? So I'm not totally sure I believe that the 8 year old is using tcpdump. But maybe I'm wrong!! Who am I to say that?
</p>

<p>
So I've discovered that the audience for clear writing about systems programming is huge. A lot bigger than you might think.
</p>
</div>
</div>

<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_51.png"><img src="/images/rust-talk/slide_51_small.png"></a>
</div>
<div class="content">
(the <a href="http://jvns.ca/zines">zine</a> I wrote)
</div>
</div>

<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_52.png"><img src="/images/rust-talk/slide_52_small.png"></a>
</div>
<div class="content">
<p>
I'm really happy about the Rust community because there are a ton of people in this room who know about Linux and networking and concurrency and all these topics that have historically been really hard to learn about.
</p>
<p>
But now many of you are gathered here inside this really welcoming and wonderful community! This feels magical to me and like it's going to be a really good thing for programming as a whole.
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_53.png"><img src="/images/rust-talk/slide_53_small.png"></a>
</div>
<div class="content">
<p>
So, to close, for real, I'm excited for this to be a place where people can walk in asking "what's a system call?"
</p>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_54.png"><img src="/images/rust-talk/slide_54_small.png"></a>
</div>
<div class="content">
<p>
and wake up a year later knowing how to do systems programming, and thinking it wasn't really that hard.
</p>

</div>
</div>



<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_55.png"><img src="/images/rust-talk/slide_55_small.png"></a>
</div>
<div class="content">
<p>
this is a picture I commissioned of myself at the san franscisco zine festival from <a href="https://twitter.com/ohmaipie">@ohmaipie</a> as a wizard.
</p>
</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/rust-talk/slide_56.png"><img src="/images/rust-talk/slide_56_small.png"></a>
</div>
<div class="content">
♥♥♥
</div>
</div>