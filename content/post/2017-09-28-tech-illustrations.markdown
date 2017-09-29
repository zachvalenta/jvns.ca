---
title: "How to make tech illustrations"
date: 2017-09-28T23:09:48Z
url: /blog/2017/09/28/tech-illustrations/
categories: []
---

People sometimes tell me these days "wow julia, you are so good at drawing, it is so cool!"

I think this is kind of funny because, like, this is what happens when I try to draw animals.

<div align="center">
<img src="https://jvns.ca/images/illustrations/animal.png">
</div>

But! I realized a while back that there actually **is** a skill to explaining technical concepts to
people with drawings. And I think I've become pretty good at that skill! 

This post is about a few patterns I use when illustrating ideas about computers.

### cartooning isn't about drawing skills

Just to emphasize it again -- this is basically the entire visual vocabulary I use.

<div align="center">
<img src="https://jvns.ca/images/illustrations/artistic-range.jpg">
</div>


I think of tech cartooning as being about like... cartooning skills. Like I need to be good at

* using a very small number of words to express an idea (for example [this mutexes cartoon](https://drawings.jvns.ca/mutexes/) has maybe 60 words in it)
* breaking something down into simple concepts ("what are the key ideas you need to understand DNS?")
* staging relevant scenarios ("what's a good example to use to show how a mutex works?")

Here are some tactics I like to use when drawing!

### just write some text

We're going to talk about "drawing" and "cartoons" but often I'll just literally write some text by
hand. Here's the start of a page about dstat:

<div align="center">
<img src="https://jvns.ca/images/illustrations/dstat.png">
</div>

This basically just says "every second, dstat prints out how much network & disk your computer used
that second". I could have typed that! But I think writing it by hand emphasizes like "no, this is
something I really love, I love it so much  I wrote it out by hand and made a picture to show you!"

Let's talk about making actual drawings that are not just words though!

### personify the characters

I do a lot of personification/anthromorphizing -- I'll take a system and turn it into a cast of
characters who talk to each other. For example, here's a scene from Kubernetes: the kubelet
component is talking to the API server

<div align="center">
<img src="https://jvns.ca/images/illustrations/personify1.png">
</div>

This is useful because

1. it emphasizes that the "kubelet" and the "api server" (whatever those are) are important concepts
   in Kubernetes
2. it shows you that those two components communicate with each other
3. it's more fun than reading a paragraph saying the same thing


Here's part of the cast of characters from my networking zine: (a laptop! a router! an operating
system! a program!)

<div align="center">
<img src="https://jvns.ca/images/illustrations/personify2.png">
</div>

Taking a complicated computer system and breaking down "ok, these are 3 main important characters in
this system" is incredibly useful.

### show a scene

The next step after just making your characters is to put them into scenes and make them interact
with each other! So once you've established "the important characters here are the laptop, the DNS
server, and the HTTP server", you can show how they actually work together in real life.

Here's a scene with two humans talking:

<div align="center">
<img src="https://jvns.ca/images/illustrations/scene1.png">
</div>

and one with two programs who are both using the same mutex:

<div align="center">
<img src="https://jvns.ca/images/illustrations/scene2.png">
</div>

I think this scene (with program 2 thinking "not my turn yet") is a pretty clear way to explain what
happens when a mutex is in use, and I think it's faster to understand what's going on than if you
read a paragraph explaining the same thing.

### make a list

I make a LOT of lists (for example, this post itself is a "list of things I've learned about making comics
:)"). A few examples:

Here's part of a list of networking tools and what they're for

<div align="center">
<img src="https://jvns.ca/images/illustrations/list1.png">
</div>

a list of attributes of a Unix process

<div align="center">
<img src="https://jvns.ca/images/illustrations/list2.png">
</div>

a list of strategies for asking good questions

<div align="center">
<img src="https://jvns.ca/images/illustrations/list3.png">
</div>

A few things I love about making lists:

* it's a really clear structure and so they're easy to understand
* it's a nice way to teach someone something new (maybe you list 10 interesting things, and they
  only knew about 7 of them!)
* none of them claim to be exhaustive (I didn't say those were *all* the attributes of a process!)
* sometimes I learn surprising things while making them. For example I started listing Linux
  networking tools and I was really surprised by how **many** of them there were (I ended up listing
  24 of them!) ([here's the whole list](https://twitter.com/b0rk/status/851652231862595584))

### make a diagram

A big part of the joy of hand drawing comics is that I can really easy make diagrams to explain what
I mean! No fiddling with LaTeX or graphviz or anything.

Here's part of a diagram I meant to illustrate memory fragmentation:

<div align="center">
<img src="https://jvns.ca/images/illustrations/diagram1.png">
</div>

and a slightly more involved diagram showing the structure of a UDP packet:

<div align="center">
<img src="https://jvns.ca/images/illustrations/diagram2.png">
</div>

I love that I can use arrows / colours to emphasize things I think are important or give extra
information. Like in this UDP packet diagram I greyed out fields that I thought were less important
(like the "fragment offset", which is definitely less important to understand than the source IP
address).

### make a joke

Computers are often really confusing and surprising. This can be kind of frustrating ("what is my
program even doing?!!?!") and also kind of funny! I think all the weird stuff that happens is part of
the joy of computers! So sometimes I try to make jokes.

Here's the Kubernetes scheduler all worried because it noticed a pod that it hasn't been scheduled.
(scheduler: "OH NO! I was supposed to have done that already! julia will be mad!")

<div align="center">
<img src="https://jvns.ca/images/illustrations/joke1.png">
</div>

and a silly "C is for linearizable" joke (because the C in "CAP theorem" stand for "consistent". But
"consistent" is a pretty unclear term, so it's more precise to say that it sounds for linearizable.
So confusing!")

<div align="center">
<img src="https://jvns.ca/images/illustrations/joke2.png">
</div>


### trace icons/logos

At the beginning I said "I can't draw well", which is true! But I **can** trace things and sometimes
that can be a really fun thing to do.

It's useful sometimes to include logos / icons! For example here are versions I traced of the
Kubernetes logo, the Recurse Center logo, Tux (the linux penguin), and a cat. The cat isn't
anybody's logo as far as I know.

<div align="center">
<img src="https://jvns.ca/images/illustrations/icons.png">
</div>

The hand-traced versions of these logos are kind of wobbly and imprecise in a way that is pretty
satisfying to me, I think they look cool.

### tools that make it easy

The tools I use today to make these are (see [this interview for more](https://usesthis.com/interviews/julia.evans/))

* a Samsung Chromebook Plus (though any samsung tablet with an S-pen will do. or an ipad with the
  apple pencil!)
* the Squid app for Android (goodnotes for ipad is good too!)
* that's it!

Having a tablet I can draw on means I can really quickly draw something, click "share on Twitter"
and immediately show it to the world. I definitely produce way more drawings with it than I did when
I was working with pen and paper. And they look way better :)

### drawings don't have to be beautiful to be awesome

I started out by drawing things on paper with a pen / Sharpie and just taking pictures. They all
looked way less good than everything I've posted above, but they were still really cool!!

For example here's a very early drawing that I drew in pen on paper and posted to Twitter. Today I
find this kind of janky & illegible but honestly when I posted it I got TONS of positive comments
([evidence](https://twitter.com/b0rk/status/638365065926811648)). 
<div align="center">
<img src="https://jvns.ca/images/illustrations/wizard-programmer-handwritten.jpg">
</div>

So drawings do not have to be beautiful and clean! They can be a sketchy thing you wrote on paper
and that is okay.

### drawing is fun

If you are also interested
