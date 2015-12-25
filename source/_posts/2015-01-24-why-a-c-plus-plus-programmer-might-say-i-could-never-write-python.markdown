---
layout: post
title: 'Why a C++ programmer might say "I could never write Python"'
date: 2015-01-24 10:15:27 -0500
comments: true
categories: python
---

I once heard a C++ programmer say "oh no, Python, that's so hard, I could never
write that. I'm so used to having a compiler!". And at the time I thought they
were just being silly -- Python isn't that hard! We're humans, we can learn and
grow! Of course they could!

But I've been writing both Scala and Ruby lately, and I've had some new
thoughts. There's not much to them, and maybe they're obvious, but:

If you work with a compiled typed language like Scala, you develop a lot of
skills around working with the type system to get better correctness.

If you spend all your time working in Python, by default you can't even detect
basic typos in your code like

```python
def foo(elephant):
    return elephnt + 2
```

So you need to spend all your time learning how to write correct code without a
static type checker, partly by writing a much better test suite, by using a
linter, etc. Tests that wouldn't tell you very much at all in Scala (that just
run the code and don't check the result) suddenly become incredibly useful! And
it's extra important to write testable code.

So maybe the C++ programmer who says she can't write Python is really saying
"Writing safer code in a dynamic language is a skill that takes time to learn!
I have not yet learned it! I would be too scared to commit to writing a
reliable Python program right now!"

And maybe this is part of why Haskell programmers get so attached to Haskell --
because they've invested so much in learning the type system, and those skills
don't transfer well to other languages like Python.

I'd be interested to know what you think. (though: I do not want to talk about
whether {Python, Ruby, Javascript} are *better or worse* than {Scala, C++,
Haskell}. There are already too many flamewars discussing that so we're not
going to talk about it. I just want to talk about skills attached to specific
kinds of programming languages and how transferable they are.)
