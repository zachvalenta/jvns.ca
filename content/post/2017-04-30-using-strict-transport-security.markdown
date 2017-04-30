---
title: "Using the Strict-Transport-Security header"
date: 2017-04-30T13:27:17Z
url: /blog/2017/04/30/using-strict-transport-security/
categories: []
---

I just updated my site today to use the `Strict-Transport-Security` (or
"HSTS" as it's often called) header, and I think it's an interesting
thing to know about so I thought I'd tell you all about it.

Extra disclaimer for web security posts: I'm not a security
person, you should not take security advice from me, security is
complicated. This is just what I understand so far! I think most of this
is right but if it's wrong let me know!

### HTTPS is good

The idea behind the Strict-Transport-Security header is that if you
have a HTTPS site, you might want your users to *always* use the HTTPS
version of my site.

Until yesterday, my site had a HTTP version and an HTTPS version. So you
could go to http://jvns.ca or https://jvns.ca, depending on what you
wanted! This was fine, because my site is a static HTML site and there's
no private content on it at all.

But a lot of sites *do* have private content, and should always use
encryption! The standard practice if you always want your site to be
served with HTTPS is:

1. always redirect HTTP to HTTPS (run `curl -I http://github.com` to see
  that they do a redirect to HTTPS!)
2. force browsers to *never* visit the HTTP version (using the HSTS
   header and the "preload list", which I'll explain!)

As I understand it, the reason it isn't enough to *just* redirect is --
if I go to http://github.com, by default my browser will send my GitHub
cookies unencrypted, which is bad! Somebody could steal them! So it's
better if I never visit http://github.com at all.

### The Strict-Transport-Security header

Strict-Transport-Security is also knows as "HTTP Strict Transport
Security" or "HSTS". I'll use "HSTS" and "Strict-Transport-Security"
interchangeably.

Let's start with an example of how GitHub uses the
Strict-Transport-Security header and then we'll talk about what it
does!

First, if I try to go to http://github.com, I just get a redirect to the
HTTPs version of the site. Here's what that looks like

```
bork@kiwi~> curl -I http://github.com
HTTP/1.1 301 Moved Permanently
Content-length: 0
Location: https://github.com/
Connection: close
```

Next, when I visit https://github.com, you can see that they return this
header called `Strict-Transport-Security`

```
bork@kiwi~> curl -I https://github.com
HTTP/1.1 200 OK
Server: GitHub.com
Date: Sun, 30 Apr 2017 17:36:21 GMT
Content-Type: text/html; charset=utf-8
Status: 200 OK
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
(a bunch more stuff removed)
```

So, what does this `Strict-Transport-Security` header mean?
"Strict-Transport-Security" is a way to to tell browsers "hey, never
visit the HTTP version of this site ever".

So after I visit **https**://github.com one time in my browser, it will
never visit **http**://github.com again. If I write http://github.com
it'll just pretend I wrote `https`.

### The preload list

Okay, so you set the Strict-Transport-Security header! That's awesome,
but the first someone tries to go to http://github.com they'll still
visit the insecure version one time.

So browsers do **another** thing called the "preload list". The idea
here is that Chrome & Firefox will download a list of sites which should
all use HTTPS. If a site is on the list.

If you want to apply to have your site added to the list, you can do it
at https://hstspreload.org/. You can see GitHub's status at https://hstspreload.org/?domain=github.com. (they're on the list!)

### why did I turn it on?

Basically I put an embedded payment form in [this blog post](https://jvns.ca/blog/2017/04/29/new-zine--let-s-learn-tcpdump/)
(from Gumroad) and so I wanted the site to be always served with HTTPS.
The payments were definitely made using HTTPS either way (Gumroad
embedded a secure iframe in my site), but if you mix HTTP & HTTPS on
your site then users' browsers will show a "mixed content warning" so I
wanted to avoid that.

There's also an argument to be made that [HTTPS can faster than HTTP](https://www.troyhunt.com/i-wanna-go-fast-https-massive-speed-advantage/) 
(for sites that support HTTP/2, which mine does because I use Cloudflare). I don't actually know
if my site is faster with HTTPS, but that blog post is really
interesting and you should read it.

### HSTS: you can't go back

I use Cloudflare's free version, and I turned on HSTS with Cloudflare by
clicking an "Enable HSTS". Before letting me do it, I had to read the
following warnings:

> If you have HSTS enabled and leave Cloudflare, you need to continue to
> support HTTPS through a new service provider otherwise your site will
> become inaccessible to visitors until you support HTTPS again.


> If you turn off Cloudflare’s HTTPS while HSTS is enabled, and you
> don't have a valid SSL certificate on your origin server, your website
> will become inaccessible to visitors.

This is kind of scary! Basically browsers will really refuse the visit
the HTTP version of your site after you turn on HSTS. So you'd better
make sure that you can keep having a HTTPS version of your site forever.
This is what the max-age setting is for (I set it to 1 month to start because I
was nervous and that was the lowest setting they'd let me use).
This is why I didn't turn on HSTS right away when I first made a HTTPS
version for my site. 

Luckily, these days anyone can get a free SSL/TLS certificate with [Let's Encrypt](https://letsencrypt.org/) so even
if I stop using Cloudflare, I can pretty easily get a TLS
certificate for my site and keep providing a secure version.

### how can I tell if my site is using the HSTS header properly?

Great question! There's a site called
https://observatory.mozilla.org/analyze.html that you can use to give
you a report card!

For example:

* github: https://observatory.mozilla.org/analyze.html?host=github.com
* jvns.ca: https://observatory.mozilla.org/analyze.html?host=jvns.ca

You can see that GitHub gets an A+ (yay!) and that I get an F (aw.). I
think this is okay because my site doesn't set any cookies with
sensitive information, but it kinda makes me feel like I
*should* increase my site's rating now =).

### that's all!

There are a lot of security headers to know about. Here's a partial
list:

* Access-Control-Allow-Origin
* Content-Security-Policy
* Strict-Transport-Security

I think those three are the most important?

and there's also

* Public-Key-Pins
* X-Content-Type-Options
* X-Frame-Options
* X-XSS-Protection
* ... and more!

The [Mozilla Web Security Guidelines](https://wiki.mozilla.org/Security/Guidelines/Web_Security)
looks to me like a good reference if you want to understand what some
specific header does.
