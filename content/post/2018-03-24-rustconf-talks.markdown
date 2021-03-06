---
title: "Talks I'd love to see at RustConf"
juliasections: ['On blogging / speaking']
date: 2018-03-24T14:37:49Z
url: /blog/2018/03/24/rustconf-talks/
categories: []
---

I'm on the RustConf program committee this year, so here is a quick list of ideas for talks I'd be
interested in seeing submitted.  These are things I personally think are interesting -- I certainly
don't represent the program committee as a whole, and there are lots of very important topics that
I've left out :)

There's an overarching theme here which is "talks that help people become better systems
programmers" -- my main interest in Rust is that it lets me to do systems programming, which I
couldn't really do before! So I'd love to see talks that help the audience level up as a systems
programmer a little bit.

[Submit a proposal here!](https://cfp.rustconf.com/events/rustconf-2018). The deadline is April 13,
2018 -- in just over 2 weeks! The earlier you submit the better -- if you submit early, the program
committee can give you feedback on your proposal :)

Here are my ideas for you:

### introduce a small part of the Rust compiler

I imagine a lot of Rust developers have never read any of the code in the Rust compiler (I
haven't!). And I know the language is trying to bring in more contributors! So I think an awesome
talk could be:

1. pick a small part of the Rust compiler (maybe a part you've contributed to!)
1. explain how it works!
1. briefly talk about opportunities for contributing to Rust RFCs today that involve that part of the compiler!

### explain how a popular Rust library works!

Is there a Rust library you love and that has made really interesting/unusual implementation choices? Explain what those choices are! What's the secret sauce that makes that library interesting? I'm personally especially interested in talks about libraries by folks other than the primary maintainer (maybe you're not the primary maintainer, but it's a library you really love and have contributed to a little bit!)

### explain an important systems concept using Rust

Did you write a database? Some high-performance networking code? I'd love to see talks that dive
into specific important systems concepts and that explain both how the systems thing works in
general (what's an L2 cache?) and how to use that thing in your Rust programs specifically (how do
you write cache-efficient code in Rust? what's an example of a crate that does that well?)

A few ideas for systems concepts to tackle:

* filesystems (so many [weird things can happen with file systems](http://danluu.com/filesystem-errors/)!!)
* databases! How do they work? What's hard about writing a database?
* a deep dive on threads: what do you have to be careful of when using Unix threads? What's
  surprising about them? Do you need to do anything special to make a threaded application portable?
* profilers! What are the best tools to use to improve your Rust performance!

### C interop & cross-platform code

interoperating with C code and writing cross-platform code are super important but I feel like I
haven't seen that many resources about how to work with C libraries effectively in Rust. I feel like
it's very easy to write sketchy Rust bindings for a C library and I'd love to see some best
practices here!

Two talks I'd love to see:

* a guide to best practices/common mistakes writing cross-platform Rust code.
* a guide to wrapping a C library in Rust, maybe using an example of some existing Rust C bindings
  that are exceptionally well implemented.

### lessons from C/C++ code

As someone who isn't that familiar with C/C++ development, I'd LOVE to have someone give an overview
of some of the architecture choices behind a large, high-quality C/C++ codebase. How is it designed?
What can we learn about structuring complex Rust programs from looking at how complex C/C++ programs
work?

### emerging Rust programming patterns

I feel like since Rust is so new, we're still learning what works and what doesn't when writing Rust
code. Are there a few specific things you've seen work well across a wide variety of Rust codebases?
What's a pattern that works well in other programming languages but often turns out not to work that
well in Rust?

One really simple example of this is -- when I started writing Rust this year, I got the advice to
make my structs own all of their data, and then almost always make my functions take references to
structs.  Obviously that's not a strict rule, but I've found following it most of the times makes my
code a lot easier.

### give a talk even if you aren't the most experienced Rust programmer!

Often people think that you need to be a wizard expert to give a talk at a programming conference.
This isn't true! What I've seen is that often people who are at an intermediate level give extremely
useful talks, because they remember what it was like to learn the material for the first time and so
can explain it well.

I think quite a few of these talks could be done well by someone who isn't an extremely experienced
Rust programmer. I'd love to hear from:

* people who have done a lot of systems programming in other languages but are relatively new to
  Rust
* people who are doing systems programming for the first time in Rust (what have you learned so far
  that really helped you?)
* and of course people who aren't really involved in systems programming at all and are using Rust
  for other reasons!! (what are you doing with Rust? :D)
