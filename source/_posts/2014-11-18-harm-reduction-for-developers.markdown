---
layout: post
title: "Harm reduction for developers"
date: 2014-11-18 08:14:32 -0800
comments: true
categories: culture
---

[Harm reduction](https://en.wikipedia.org/wiki/Harm_reduction) is an
idea in public health that says basically: people are going to do risky
activities (intravenous drug use, sex, drinking alcohol, maybe abusing
alcohol), and instead of saying "just say no to drugs!", we can choose
to help make those activities less risky.

Some examples of measures:

* needle exchanges and safe injection sites
* designated drivers and free taxis home
* safer sex classes

I don't want to trivialize any of these issues, but I think the idea
that switching out YOU'RE WRONG TO DO THAT JUST DON'T DO THAT for *doing
something to help people be safer* is super powerful and useful, and I
see it in discussions of software development all the time.

<!-- more --> 

Some of my favorite writing about writing software is like this.

* Dan Luu has a fantastic post today called [Given That We Aren’t Going to Put Any Effort Into Testing, What’s the Best Way to Test?](http://danluu.com/everything-is-broken/)
* Unit testing in dynamic languages by itself is like this -- you have
  **no idea** if your code works, so you do what you can to get a little
  more certainty.
* Violet Blue gave a talk at CCC several years ago about [harm reduction for hackers](http://violetblue.tumblr.com/hackharmreduction), which
  started me thinking about this in the first place. She mentions
  somewhere that people aren't going to stop using Facebook and Twitter
  to coordinate actions, and we need to do what we can to make that less
  dangerous.
* A lot of cryptography software is like this. GPG is incredibly
  powerful and incredibly hard to use, and tools like
  [Cryptocat](https://crypto.cat/) try to make secure communications
  more accessible. Key exchange isn't just an algorithmic problem, it's
  a social problem!
 
Dan Luu talks about this *again* (can you tell that I love his blog? I love his blog.) in 
[Read Along: The Chubby Lock Service for Loosely-Coupled Distributed Systems ](http://danluu.com/everyday-chubby/), 
where he quotes a paper about design decisions for a distributed
systems:

> Originally, we did not appreciate the critical need to cache the
> absence of files, nor to reuse open file handles. Despite attempts at
> education, our developers regularly write loops that retry
> indefinitely when a file is not present, or poll a file by opening it
> and closing it repeatedly when one might expect they would open the
> file just once.

Instead of yelling at developers for using the library wrong, they added
caching to the library.

In Valerie Aurora's wonderful [Operating systems war story: How feminism helped me solve one of file systems’ oldest conundrums](http://blog.valerieaurora.org/2014/10/03/operating-systems-war-story-how-feminism-helped-me-solve-one-of-file-systems-oldest-conundrums/), she says:

> I try to take that human-centered, feminist approach with other topics
> in file systems, including the great fsync()/rename() debate of 2009
> (a.k.a “O_PONIES”) in which I argued that file systems developers
> should strive to make life easier for developers and users, not
> harder.

Let's do what we can to make life easier for developers and users (and
ourselves!), not harder :)
