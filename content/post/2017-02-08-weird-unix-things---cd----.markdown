---
title: "Weird unix thing: 'cd //'"
juliasections: ['How a computer thing works']
date: 2017-02-08T23:37:12Z
url: /blog/2017/02/08/weird-unix-things-cd/
categories: []
---


Today my friend Mat told me an interesting trivia fact about cd!

Look at this interaction, where we try to `cd /tmp`, `cd //tmp`, and `cd ///tmp`, in bash and in fish.

```
bork@kiwi/> bash
bork@kiwi:/$ cd //tmp
bork@kiwi://tmp$ echo $PWD
//tmp
bork@kiwi:/tmp$ cd ///tmp
bork@kiwi:/tmp$ echo $PWD
/tmp
bork@kiwi://tmp$ fish
Welcome to fish, the friendly interactive shell
Type help for instructions on how to use fish
bork@kiwi:/tmp> cd //tmp
bork@kiwi:/tmp> echo $PWD
/tmp
```

What is `//tmp`? What is happening? Why is `cd ///tmp` different from `cd //tmp`? Here's what we know so far:

### are `/` and `//` the same file?

Yes. We can check this with `stat`. They both have the same inode number (256)
so they are the same file.

```
bork@kiwi:~$ stat /
  File: '/'
  Size: 244       	Blocks: 0          IO Block: 4096   directory
Device: 16h/22d	Inode: 256         Links: 1
Access: (0755/drwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2017-02-08 23:13:55.647187990 -0500
Modify: 2017-01-10 13:01:30.987733887 -0500
Change: 2017-01-10 13:01:30.987733887 -0500
 Birth: -
bork@kiwi:~$ stat //
  File: '//'
  Size: 244       	Blocks: 0          IO Block: 4096   directory
Device: 16h/22d	Inode: 256         Links: 1
Access: (0755/drwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2017-02-08 23:13:55.647187990 -0500
Modify: 2017-01-10 13:01:30.987733887 -0500
Change: 2017-01-10 13:01:30.987733887 -0500
 Birth: -
```

Cool. But what is `//`? Why doesn't bash just correct it to `/`?

### the specification

The specification for cd is [here](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/cd.html)

Here's the relevant section

> An implementation may further simplify curpath by removing any
> trailing &lt;slash&gt; characters that are not also leading &lt;slash&gt;
> characters, replacing multiple non-leading consecutive &lt;slash&gt;
> characters with a single &lt;slash&gt;, and replacing three or more leading
> &lt;slash&gt; characters with a single &lt;slash&gt;. If, as a result of this
> canonicalization, the curpath variable is null, no further steps shall
> be taken.


So! We can replace "three or more leading / characters with a single
slash". That does not say anything about what to do when there are 2 `/`
characters though, which presumably is why `cd //tmp` leaves you at
`//tmp`.

Why is this the specification? Mat pointed out there is a "Rationale"
section in this spec, but it does not really explained.

In another
[specification](http://pubs.opengroup.org/onlinepubs/009604599/basedefs/xbd_chap04.html#tag_04_11), it says:

> A pathname that begins with two successive slashes may be interpreted
> in an implementation-defined manner

So you can define `//tmp` to mean whatever you want? Like it could be different
than `/tmp`? Why? Somebody on stack overflow said that this is related to the
double slash in URLs ("http://"...) but didn't provide a citation. Is that
true?

If I find out, I will update this blog post with an answer.

**update 1**: there seems to be a pretty good answer in [this stack overflow question](http://unix.stackexchange.com/questions/256497/on-what-systems-is-foo-bar-different-from-foo-bar/256569#256569)
