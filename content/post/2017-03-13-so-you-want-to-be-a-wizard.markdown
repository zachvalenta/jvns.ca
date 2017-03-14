---
title: "So you want to be a wizard"
date: 2017-03-13T20:54:08Z
url: /blog/so-you-want-to-be-a-wizard/
categories: []
---


Today I did the opening keynote at SRECon. This talk was a little less technical than my normal talks: instead of talking about tools like tcpdump (though tcpdump makes an appearance!), I wanted to talk about how to make a career where you're constantly learning and how to be good at your job whether or not you're the most experienced person.

Here's the talk description.

<blockquote>
I don't always feel like a wizard. Like many of you, I've been doing operations for a couple of years, and I still have a TON TO LEARN about how to do this "SRE" job.
<br><br>

But along the way, I have learned a few ways to debug tricky problems, get the information I need from my colleagues, and get my job done. We're going to talk about
<br><br>

<ul>
<li>
 how asking dumb questions is actually a superpower
</li>
<li>
how you can read the source code to programs when all other avenues fail
</li>
<li>
debugging tools that make you FEEL like a wizard
</li>
<li>
and how understanding what your _organization_ needs 
can make you amazing
</li>
</ul>

At the end, we'll have a better understanding of how you can get a lot of awesome stuff done even when you're not the highest level wizard on your team.

</blockquote>

Here are the slides & a rough transcript of the talk. I've included links to every resource I mentioned.

<style>
.container{display:flex;}
.slide{
width:40%;
border-bottom: 2px #ccc dashed;
padding: 10px 0px;
}
.content{
    width:60%;
    align-items:center;
padding:20px;
}
@media (max-width: 480px) 
{
.container{display:block;}
.slide{width:100%;}
.content{width:100%;}
}
</style>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-0.png"><img src="/images/srecon-talk/slide-0.png"></a>
</div>
<div class="content">


</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-1.png"><img src="/images/srecon-talk/slide-1.png"></a>
</div>
<div class="content">

This talk is called "so you want to be a wizard". The main problem with being a wizard is that, of course, computers are not magic! They are logical machines that you can totally learn to understand.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-2.png"><img src="/images/srecon-talk/slide-2.png"></a>
</div>
<div class="content">

So this talk is actually going to be about learning hard things and understanding complicated systems.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-3.png"><img src="/images/srecon-talk/slide-3.png"></a>
</div>
<div class="content">

I work as an engineer at <a href="https://stripe.com">Stripe</a>. (this is the <a href="https://stripe.com/jobs/positions/infrastructure-engineer">job description for my job</a>).

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-4.png"><img src="/images/srecon-talk/slide-4.png"></a>
</div>
<div class="content">

My team is in charge of a ton of things. Every so often I find out about a new thing that we're in charge of ("oh, there's a GPG keyserver we depend on? Okay!!")

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-5.png"><img src="/images/srecon-talk/slide-5.png"></a>
</div>
<div class="content">

What this means is that I (like many of you!) need to know about a ton of different systems. There are about a million things to know about Linux & networking, the AWS platform is really complicated and there's a ton to know about how it works exactly. <br><br>

And there's a seemingly neverending amount of new technology to learn about. For instance we're looking at Kubernetes, and to operate a Kubernetes cluster you need to operate etcd, which means that you need to understand a bunch of distributed systems concepts to make sure you're doing it right.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-6.png"><img src="/images/srecon-talk/slide-6.png"></a>
</div>
<div class="content">


So to do my job effectively, like many of you, I need to constantly learn new things. This talk is about how to do that, and why I like it.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-7.png"><img src="/images/srecon-talk/slide-7.png"></a>
</div>
<div class="content">

Here are the wizard skills we're going to be discussing in this talk!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-8.png"><img src="/images/srecon-talk/slide-8.png"></a>
</div>
<div class="content">


</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-9.png"><img src="/images/srecon-talk/slide-9.png"></a>
</div>
<div class="content">

In software engineering, I think it's really important to understand both the systems that are a little higher-level than you and lower-level systems.<br><br>

In reliability engineering, what lives below us is typically "systems stuff" like operating systems & networking. Above us is stuff like business requirements & the programs we're trying to make run reliably.
<br><br>

This talk is mostly going to be about understanding lower-level systems, but we're also going to talk a little about humans and how to make sure you're actually building the right thing :)


</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-10.png"><img src="/images/srecon-talk/slide-10.png"></a>
</div>
<div class="content">

As a quick aside, I think understanding computer networking is so important that I wrote a <a href="http://jvns.ca/networking-zine.pdf">whole zine about it</a>, which you can pick up at the end of this talk.


</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-11.png"><img src="/images/srecon-talk/slide-11.png"></a>
</div>
<div class="content">


So -- why is it important to understand the systems you work with?

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-12.png"><img src="/images/srecon-talk/slide-12.png"></a>
</div>
<div class="content">


I think there are 3 main important reasons:
<br><br>
First, understanding <strong>jargon</strong> is really useful. If someone says "hey, this process got killed by the OOM killer" it's useful to know what that means! (we're going to talk about what it means later)

<br><br>

second, it lets you  <strong>debug harder problems</strong>. When I set up a web server (Apache) for the first time, maybe 8 years ago, I didn't understand the HTTP protocol very well and I didn't understand what many of the configuration options I was using meant exactly. <br><br>

So I would normally debug by Googling things and trying random fixes. This was a pretty viable strategy at the time (I got my webservers working!) but today when I configure webservers, it's important for me to actually understand what I'm doing and exactly what effect I expect it to have. And now I can fix problems much more easily.
<br><br>
<a href="https://rachelbythebay.com/w/">rachelbythebay</a> is a great collection of debugging stories, and it's clear throughout that she has a really deep understanding of the systems she works with.

<br><br>
The last reason is -- having a solid understanding of the systems you work with lets you <strong>innovate</strong>. I think Docker is a cool example of this. Docker was not the first thing to ever use namespaces (one of the kernel features that <a href="http://jvns.ca/blog/2016/10/10/what-even-is-a-container/">people call "containers"</a>), but in order to make a tool that people loved to use, the Docker developers had to have a really good understanding of exactly what features Linux has to support isolating processes from others.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-13.png"><img src="/images/srecon-talk/slide-13.png"></a>
</div>
<div class="content">

So, a system like Linux seems really intimidating at first, especially if you want to understand some of the internals a little bit. It's like 4 million or 10 million lines of code or something.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-14.png"><img src="/images/srecon-talk/slide-14.png"></a>
</div>
<div class="content">

So let's talk about how to break off pieces of knowledge one at a time so that you can tackle the challenge!


</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-15.png"><img src="/images/srecon-talk/slide-15.png"></a>
</div>
<div class="content">

My first favorite thing to do is <strong>learn fundamental concepts</strong>. <br><br>

This is incredibly useful -- in networking, if you know what a packet is and how it's put together, then it really helps to tackle other more complicated concepts.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-16.png"><img src="/images/srecon-talk/slide-16.png"></a>
</div>
<div class="content">

The Recurse Center is a 12 week programming retreat in New York where you can go to learn fun new things about programming. I went 3 years ago, partly with the goal of understanding operating systems better.<br><br>

When I got to RC, I learned about the concept of a "system call"! (here's <a href="http://jvns.ca/blog/2013/10/02/day-3-what-does-the-linux-kernel-even-do/">the blog post I wrote the day I learned that</a>). System calls are how applications talk to the operating system. I felt kind of sad that I didn't know about them before, but the important thing was that I learned it! That's exciting!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-17.png"><img src="/images/srecon-talk/slide-17.png"></a>
</div>
<div class="content">

This is the only piece of homework in this talk :)<br><br>

TCP is the protocol that runs a lot of the internet that we use day to day. Often it "just works" and you don't need to think about it, but sometimes, well, we do need to think about it! So it's helpful to understand the basics. <br><br>

The way I started learning about TCP was, I wrote a <a href="/blog/2014/08/12/what-happens-if-you-write-a-tcp-stack-in-python/">TCP stack in Python</a>! This was really fun, it didn't take that long, and I learned a ton by doing it and writing up what I learned.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-18.png"><img src="/images/srecon-talk/slide-18.png"></a>
</div>
<div class="content">

I also like to do <strong>experiments</strong>.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-19.png"><img src="/images/srecon-talk/slide-19.png"></a>
</div>
<div class="content">


</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-20.png"><img src="/images/srecon-talk/slide-20.png"></a>
</div>
<div class="content">

Also at the Recurse Center, I decided I wanted to write a tiny operating system in Rust</a>. It turns out that writing an OS in 3 weeks when you don't know Rust or operating systems is hard, so I ended up writing a keyboard driver. <br><br>

I learned SO MUCH by doing this -- you can <a href="/blog/2014/03/12/the-rust-os-story/">read more about it here</a>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-21.png"><img src="/images/srecon-talk/slide-21.png"></a>
</div>
<div class="content">


</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-22.png"><img src="/images/srecon-talk/slide-22.png"></a>
</div>
<div class="content">

These are the programming experiment rules I like to follow.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-23.png"><img src="/images/srecon-talk/slide-23.png"></a>
</div>
<div class="content">

Sometimes I like to read books! Two books I've learned from in the last couple years are <a href="https://www.michaelwlucas.com/networking/n4sa">Networking for System Administrators</a> & <a href="https://www.amazon.com/Linux-Kernel-Development-Robert-Love/dp/0672329468">Linux Kernel Development</a>.

Networking for System Administrators is written for system administrators who want to be able to do basic networking tasks without having to ask their networking team. I'm not a system administrator, and I don't have a networking team, but I learned a ton by reading this book.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-24.png"><img src="/images/srecon-talk/slide-24.png"></a>
</div>
<div class="content">

Another thing that  I find super helpful is to try to read things or watch talks that are <strong>too hard for me</strong> at the time. For example, aphyr has an amazing series of <a href="https://aphyr.com/">posts about distributed systems failures</a> (the ones called "Jepsen"). When I started reading these posts, I honestly didn't understand them very well. I didn't understand what "linearizable" meant, and I'd never worked with distributed databases. So sometimes I'd read a post and only understand maybe 20% of it.

<br><br>

As I learned more and came back to his writing, I was able to understand more of it! I'm still not a distributed systems expert, but I'm happy I tried to read these posts even when I didn't understand them well.
<br><br>
That Linux kernel development book I mentioned is kind of similar. Its goal is to give you the tools you need to become a Linux kernel developer. I am not a Linux kernel developer (or at least not yet!). But I've learned a few interesting things by reading this book.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-25.png"><img src="/images/srecon-talk/slide-25.png"></a>
</div>
<div class="content">

Another maybe obvious tactic is to work with the thing in your job. Recently I needed to add some logging to a HTTP proxy we had. This was a relatively mundane task, but I learned more about how HTTP proxies work exactly by doing it! That was cool!<br><br>

It's useful for me to remember that I can learn something even when I'm doing work which is sort of routine.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-26.png"><img src="/images/srecon-talk/slide-26.png"></a>
</div>
<div class="content">

This is the last, and maybe most important thing. I have models of how a ton of systems work in my head. Sometimes what happens on the computers work with does not match what my model says!

<br><br>

As a small example -- recently we had a computer that was swapping even though it had 16GB of free memory. This did not match my mental model ("computers only swap memory to disk when they're out of memory"). Obviously there was something wrong with my model. So I investigated, and I learned a couple new things about how swap works on Linux!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-27.png"><img src="/images/srecon-talk/slide-27.png"></a>
</div>
<div class="content">

It turns that there are actually at least 4 reasons a Linux box might swap. 
<br><br>
1. You could be actually out of RAM.
<br><br>
2. You could be "mostly" out of RAM. The "vm.swappiness" sysctl setting controls how likely your machine is to swap. This isn't what was happening to us, though.
<br><br>
3. A cgroup could be out of RAM, which was what was happening to us at the time (<a href="/blog/2017/02/17/mystery-swap/">here's the blog post I wrote about that)</a>.
<br><br>
4. There's also a 4th reason I learned about afterwards: if you have no swap, and your vm.overcommit_ratio is set to 50% (which is the default), you can end up in a situation where only half your RAM can be used. That's no good! <a href="http://engineering.pivotal.io/post/Virtual_memory_settings_in_Linux_-_The_problem_with_Overcommit/">here's a post about overcommit on Linux</a>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-28.png"><img src="/images/srecon-talk/slide-28.png"></a>
</div>
<div class="content">

So it turns out understanding swap isn't actually that simple. In fact, there's a cool 200-page book <a href="https://www.kernel.org/doc/gorman/pdf/understand.pdf">Understanding the Linux Virtual Memory Manager</a>. It also has a bunch of annotated kernel code that handles memory management, which is awesome. 
<br><br>
I'm happy I dug in a bit because now I understand how this part of Linux works better!
</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-29.png"><img src="/images/srecon-talk/slide-29.png"></a>
</div>
<div class="content">

So even getting to understand something that seems relatively basic like "when does a computer start swapping?" can take a while! There's a lot to know, and it's totally okay to not know it all right away. 
</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-30.png"><img src="/images/srecon-talk/slide-30.png"></a>
</div>
<div class="content">


</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-31.png"><img src="/images/srecon-talk/slide-31.png"></a>
</div>
<div class="content">


The next wizard skill I'm going to talk about is asking great questions!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-32.png"><img src="/images/srecon-talk/slide-32.png"></a>
</div>
<div class="content">

A (great) situation I end up in a lot is where I have a coworker who knows something that I want to know, and they want to help me, and I just need to figure out the right questions to ask to get the answers I want!

<br><br>

Asking good questions is really important because people in general cannot just magically guess what I want them to tell me.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-33.png"><img src="/images/srecon-talk/slide-33.png"></a>
</div>
<div class="content">


One of my favorite tricks is to <strong>state what I know</strong>, as a way to frame my question.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-34.png"><img src="/images/srecon-talk/slide-34.png"></a>
</div>
<div class="content">

Stating what I know is awesome because it helps me organize my thoughts, reveals misunderstands (me: "I know X", them: "that not quite right!"), and helps me avoid answers that are too basic (yes yes yes i know that!) and too advanced (NO PLEASE BACK UP 30 STEPS FIRST).

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-35.png"><img src="/images/srecon-talk/slide-35.png"></a>
</div>
<div class="content">

When asking a question, it's pretty natural to want to ask the most experienced person around your question. They will probably know the answer, which is good! But I don't think it's the best strategy.<br><br>

Instead, I instead try to remember to ask a less experienced person, who I think will still know the answer.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-36.png"><img src="/images/srecon-talk/slide-36.png"></a>
</div>
<div class="content">

This is awesome because it reduces the load on the more-experienced person. But there's more reasons this is great! I'm not the most experienced member of my team. I love it when people ask me questions because -- if I don't know the answer to their questions, then I can find out, and I can grow my own knowledge.
<br><br>
So not asking the most experienced person is actually a cool way to show trust in less experienced team members, reduce the bus factor, and spread knowledge around.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-37.png"><img src="/images/srecon-talk/slide-37.png"></a>
</div>
<div class="content">

Doing research is great! It lets me ask more complicated and interesting questions!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-38.png"><img src="/images/srecon-talk/slide-38.png"></a>
</div>
<div class="content">

I really like to ask questions that are relatively easy to answer. yes/no questions are a really good way to accomplish this! And often an interesting yes/no question can lead to a great discussion.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-39.png"><img src="/images/srecon-talk/slide-39.png"></a>
</div>
<div class="content">

When debugging or fixing things, often you can end up in a situation where someone who's super experienced knows how to Do A Thing, and other people on the team don't know how.
<br><br>

And often they have trouble remembering all the details to document them! So I like to (right after someone did something) to ask them to explain exactly what they did, or to ask if I can watch while they do it.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-40.png"><img src="/images/srecon-talk/slide-40.png"></a>
</div>
<div class="content">

The last thing I have to say about asking about questions, especially to senior engineers / managers / leaders is -- please ask questions in public. I find that it's much easier for senior people to admit that they don't know something (because everybody knows you're competent already!), and doing that really creates space for everyone to ask questions.
</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-41.png"><img src="/images/srecon-talk/slide-41.png"></a>
</div>
<div class="content">

Okay, let's talk about reading code!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-42.png"><img src="/images/srecon-talk/slide-42.png"></a>
</div>
<div class="content">

Sometimes error messages are not particularly helpful. If you go read the code around where the error message got printed, sometimes you can get a better clue about what's going on!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-43.png"><img src="/images/srecon-talk/slide-43.png"></a>
</div>
<div class="content">

What's more exciting to me, though, is to read the code when software is poorly documented (which happens all the time, especially when it's changing frequently or isn't used by very many people)

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-44.png"><img src="/images/srecon-talk/slide-44.png"></a>
</div>
<div class="content">

I want to emphasize that reading code isn't just for small projects that you're familiar with, though. <br><br>

In my first job, I was writing plugins to make websites with Drupal, a PHP content management system. Once I remember I had a really specific question about how some Drupal thing worked. It wasn't documented, and there were no results on Google when I looked. <br><br>
I asked my boss at the time if he knew and he told me "julia, you just have to go read the code and find out how it works!". I was a bit unsure about how to approach it ("there's so much code") but he pointed me to the relevant part of the Drupal codebase, and, sure enough, I could see the answer to my question there!<br><br>

Since then I've looked at the code for a bunch of large open source questions to answer questions (nginx! linux!) and even if I'm not a super good C programmer, sometimes I can figure out the answer to my question.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-45.png"><img src="/images/srecon-talk/slide-45.png"></a>
</div>
<div class="content">

Now we're going to talk about one of my favorite things! Debugging!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-46.png"><img src="/images/srecon-talk/slide-46.png"></a>
</div>
<div class="content">

Let's tell a story! One day we had a client that was making a HTTP request, and it wasn't getting a response for 40 milliseconds. That's a long time!


</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-47.png"><img src="/images/srecon-talk/slide-47.png"></a>
</div>
<div class="content">

Why is that a long time? The client and the server were on the same computer. And I expected the server to be fast, so there was no reason for a 40ms delay.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-48.png"><img src="/images/srecon-talk/slide-48.png"></a>
</div>
<div class="content">

As an aside, 40ms synchronously is 25 requests per second, which is really not a lot. It's easy to see how this kind of delay could become a problem quickly.


</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-49.png"><img src="/images/srecon-talk/slide-49.png"></a>
</div>
<div class="content">

I captured some packets with Wireshark to figure out who I should be blaming -- the client or the server! <br><br>
We found out that the client would send the HTTP servers, wait 40ms, and then send the rest of the request. So the server wasn't the problem at all! But why was the client doing this? It's written in Ruby, and initially I maybe thought we should just blame Ruby, but that wasn't a really good reason (40ms is a very long time, even in Ruby).

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-50.png"><img src="/images/srecon-talk/slide-50.png"></a>
</div>
<div class="content">

It turned out what was happening was a bad interaction between two TCP optimizations -- delayed ACKs, and Nagle's algorithm. When the client sent the first packet, the server would wait to send an ACK (becaues of the delayed ACKs algorithm), and the client was waiting for that ACK (because of Nagle's algorithm).<br><br>
So they were stuck in this kind of passive-aggressive-waiting situation.
<br><br>

I wrote a blog post about this called <a href="/blog/2015/11/21/why-you-should-understand-a-little-about-tcp/">Why you should understand (a little) about TCP</a> if you want to know more.
</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-51.png"><img src="/images/srecon-talk/slide-51.png"></a>
</div>
<div class="content">

When we set the TCP_NODELAY socket option, it stopped the client from waiting, and then everything got fast!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-52.png"><img src="/images/srecon-talk/slide-52.png"></a>
</div>
<div class="content">

A while ago I realized I felt like I'd gotten a lot better at debugging since my first job, and I came up with some reasons I think it got easier!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-53.png"><img src="/images/srecon-talk/slide-53.png"></a>
</div>
<div class="content">

Sometimes when I hit a bug, especially a nondeterministic and difficult to reproduce bug, it’s tempting to think “oh you know, things just happen, who knows”. But everything on a computer does in fact happen for a logical reason (however much the computer may try to convince you otherwise). Reminding myself of that helps me fix bugs. Also known as “OK JULIA IT IS NOT FAIRIES WHAT ACTUAL REASON COULD BE CAUSING THIS?”

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-54.png"><img src="/images/srecon-talk/slide-54.png"></a>
</div>
<div class="content">

Next up, confidence!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-55.png"><img src="/images/srecon-talk/slide-55.png"></a>
</div>
<div class="content">

A while ago I dealt with a performance problem in a Hadoop job at work that took me 2 weeks to fix (see <a href="http://jvns.ca/blog/2015/09/10/a-millisecond-isnt-fast-and-how-we-fixed-it/">a millisecond isn’t fast</a>). If I hadn’t been able to fix it, I would have felt pretty bad and like it was a waste of 2 weeks.
<br><br>
But we were processing a relatively small number of records, and it was taking 15 hours to do it, and it was NOT REASONABLE and I knew that the job was too slow. And I figured it out, and now it’s faster and everyone is happy.
</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-56.png"><img src="/images/srecon-talk/slide-56.png"></a>
</div>
<div class="content">

From that, I learned that floating point exponentiation is slow, and that 1000 records/second isn't really a lot.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-57.png"><img src="/images/srecon-talk/slide-57.png"></a>
</div>
<div class="content">

The job was processing 1000 records/second. I found this hard to think about at the time though -- was that a lot? not a lot? How was I supposed to know? <br><br>
So I decided I wanted to take some time to train my intuitions about how fast different computer operations should be.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-58.png"><img src="/images/srecon-talk/slide-58.png"></a>
</div>
<div class="content">

I made this game called <a href="http://computers-are-fast.github.io/">computers are fast</a> with my partner Kamal. You can go play it online, and we're going to play it now a little bit!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-59.png"><img src="/images/srecon-talk/slide-59.png"></a>
</div>
<div class="content">

Suppose you have an indexed database table, with 10 million rows in it. How long does it take to select a row from that table? How many times per second can you do that?
<br><br>

The goal isn't to know exactly, but I think it's useful to be right up to an order of magnitude. So can you do it 100 times in a second? 10,000? 10 million times?

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-60.png"><img src="/images/srecon-talk/slide-60.png"></a>
</div>
<div class="content">

It turns out the answer on my laptop is 55,000 times! (or, it takes about 20 microseconds, in Python)

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-61.png"><img src="/images/srecon-talk/slide-61.png"></a>
</div>
<div class="content">

It's also been incredibly helpful for me to have better tools for answering questions about your programs!<br><br>
When I started out, I didn't have very good tools! But now I know about all kinds of profilers! I know about strace, and tcpdump, and way more tools for figuring out what's going on. It makes a huge difference.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-62.png"><img src="/images/srecon-talk/slide-62.png"></a>
</div>
<div class="content">


I wrote a whole zine about debugging tools that have helped me answer questions. You can read it here: <a href="http://jvns.ca/debugging-zine.pdf">Linux debugging tools you'll love</a>

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-63.png"><img src="/images/srecon-talk/slide-63.png"></a>
</div>
<div class="content">

But maybe the most important thing is that I learned to like debugging! I used to get grumpy when I ran into bugs. I felt like they were just getting in my way!
<br><br>
But these days, when I run into a mysterious bug, I think it's kind of fun! I get to improve my understanding of the systems I work with, which is awesome!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-64.png"><img src="/images/srecon-talk/slide-64.png"></a>
</div>
<div class="content">

Now we're going to zoom out a bit from talking about networking and microseconds, and talk about how to design engineering projects. This is something that's really helped me a lot! 

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-65.png"><img src="/images/srecon-talk/slide-65.png"></a>
</div>
<div class="content">

There are a lot of words for design document, but they're basically all the same idea -- you write down words about what work you're going to do before doing the work.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-66.png"><img src="/images/srecon-talk/slide-66.png"></a>
</div>
<div class="content">

When I started at Stripe I thought writing stuff down was kind of dumb. Why couldn't I just start working on the project?<br><br>
But since then, I've learned to find them really useful! (<a href="http://jvns.ca/blog/2016/06/03/learning-to-like-design-documents/">learning to like design documents</a>)

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-67.png"><img src="/images/srecon-talk/slide-67.png"></a>
</div>
<div class="content">

I was worried that if I wrote a document, I'd either get WAY TOO MUCH feedback, or total silence.<br><br>

One thing I learned is that it's helpful at first to just share a design I'm working with a few people. Like I'll show it to a couple of other people on my team, see what they think, and then make changes! It's not always necessary to ask every single person who might have an opinion what they think.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-68.png"><img src="/images/srecon-talk/slide-68.png"></a>
</div>
<div class="content">

I also learned to like designing small projects. Recently I worked on a tiny project that just took about a week. My team lead asked me if I could quickly write up what we were going to do. <br><br>

It took me maybe 45 minutes to write up the plan (super fast!), I showed it to a manager on another team, he had a couple of things he asked me to do differently, and he was SO HAPPY I'd written down a plan so that he understood what was going on. Awesome!
<br><br>
The small project went super smoothly and I was really happly I wrote up a thing about it first.
</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-69.png"><img src="/images/srecon-talk/slide-69.png"></a>
</div>
<div class="content">


How do you know what to write in a design document? I really like to start by writing an announcement email, as if we just finished the project.<br><br>

This is great because it forces me to articulate why the project is important (why did we spend all that time on it), how it's going to impact other teams ans what other people in the organization need to know about, and how we know that we actually met our goals for the project<br><br>

The last thing is really important -- more often than I'd like to admit, I get to the end of a project and realize I'm not quite sure how we can tell whether the project is actually going to improve things or not. Planning that out at the beginning helps make sure that we put in the right metrics!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-70.png"><img src="/images/srecon-talk/slide-70.png"></a>
</div>
<div class="content">

It's also useful to talk about risks! I actually haven't done this yet, but a cool idea I heard recently for figuring out risks was to do a "premortem" for your project. This is kind of the opposite of an announcement email -- instead, you imagine that the project failed 6 months down the line, and you're making sure you understand why it failed.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-71.png"><img src="/images/srecon-talk/slide-71.png"></a>
</div>
<div class="content">

When I started writing designs, I used to worry a lot that my design would be wrong because things were going to change. It turns out that this is totally true -- designs rarely survive contact with the real world. Priorities change, you run into technical challenges you didn't expect, all kinds of things can go wrong. <br><br>

But this doesn't mean it's not worth designing at all! I like writing down my assumptions explicitly because when things do change, I can go back and see what assumptions we had are no longer true, and make sure that we update everything we need to update. Having a record of changes is useful!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-72.png"><img src="/images/srecon-talk/slide-72.png"></a>
</div>
<div class="content">

We've arrived at the last wizard skill!

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-73.png"><img src="/images/srecon-talk/slide-73.png"></a>
</div>
<div class="content">

Sometimes I'm working on something kind of boring, and I wonder like.. why am I doing this? <br><br>
I usually find it possible to stay motivated if I can remember "ok, I'm spending hours working on configuring nginx, and this is boring, but it's in service of this really cool goal!" <br><br>
But if I *don't* remember the goal (or what I'm working on actually doesn't make sense), it sucks.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-74.png"><img src="/images/srecon-talk/slide-74.png"></a>
</div>
<div class="content">

The solution I'm working on to this right now is to approach project planning with the same kind of excitement and curiosity you might bring to a gnarly bug! <br><br>

I'm trying to get better at saying "okay!!! this project! it has some slow and difficult pieces, so why is it so important? why are we going to feel awesome when it's done? which parts are the most important?"

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-75.png"><img src="/images/srecon-talk/slide-75.png"></a>
</div>
<div class="content">

I have a lot of autonomy in about what I get to work on, so when someone asks me to do something, I like to make sure I understand why it's important. Usually if I don't understand, the right thing to do is to just find out why it's important (usually it actually is!). 
<br><br>
But sometimes the task I'm being given is only maybe 80% thought through, and when I go to understand the exact reason for doing it, it turns out that we don't need to do it at all! (or maybe we should actually be doing something completely different!)

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-76.png"><img src="/images/srecon-talk/slide-76.png"></a>
</div>
<div class="content">
And understanding the big picture helps me make better technical decisions! 



</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-77.png"><img src="/images/srecon-talk/slide-77.png"></a>
</div>
<div class="content">


Like a lot of people, I think a lot about the impact my work has and what I'm really doing here. Kelsey Hightower had a really amazing series of <a href="https://twitter.com/kelseyhightower/status/841446059641466880">tweets today</a>. here are a couple of quotes.

<br><br>

> I’ve yet to find the perfect job or thing to work on, but I have found a way to live a more meaningful life in tech.

<br><br>

> I now put people first. Regardless of the technology involved I gravitate towards helping people.
<br><br>

> People provide a much better feedback loop than computers or the abstract idea of a business.

<br><br>

> Everything I work on has a specific person or group of people in mind; this is what gives my work meaning; solving problems is not enough.

</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-78.png"><img src="/images/srecon-talk/slide-78.png"></a>
</div>
<div class="content">


</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-79.png"><img src="/images/srecon-talk/slide-79.png"></a>
</div>
<div class="content">


</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-80.png"><img src="/images/srecon-talk/slide-80.png"></a>
</div>
<div class="content">

during this conference, I hope you ask a ton of questions to understand what's going on with this "SRE" thing better. There are so many amazing people to learn from!
</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-81.png"><img src="/images/srecon-talk/slide-81.png"></a>
</div>
<div class="content">


</div>
</div>


<div class="container">
<div class="slide">
<a href="/images/srecon-talk/slide-82.png"><img src="/images/srecon-talk/slide-82.png"></a>
</div>
<div class="content">


I handed out fun networking zines at the end of this talk. If you want to read the zine, it's here: <a href="http://jvns.ca/networking-zine.pdf">Networking! ACK!</a>

</div>
</div>

