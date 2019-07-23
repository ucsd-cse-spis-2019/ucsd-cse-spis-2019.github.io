---
topic: "Python: Requests: User-Agent"
desc: "The first thing to try when you get 'access denied'"
---

# When `requests.get` doesn't work, what do you do?

If you are using the Python `requests` module to load web content, you may occassionally run into problem with access, where
you get "Forbidden", or "Access Denied" or "Too many requests" errors.

These are especially frustrating when you find that issuing the EXACT SAME REQUEST in a web browser results in no problem at all.

It really makes you wonder: why does my web browser work, but my `requests.get` or `requests.post` doesn't?  Especially when the
requests are coming from the exact same computer?

So, it isn't *always* the case, but it is *often* the case that the problem is something called the 'User-Agent'.

The 'User-Agent' is the identifier for a particular kind of "browser-like-thing".     Each web browser, e.g. Firefox, Chrome, IE, Safari, etc.
has its own particular signature that it sends along with requests in a header called the 'User-Agent'.

And, when you send a request from the Python `requests` module, if you don't set a User-Agent, then you might appear to
be some kind of badly behaved bot.   This often triggers code on the server that will keep you out!

There are a couple of ways to address this.

One is to set a User-Agent that describes who you are and what you are doing.  It is best, in this case, to add something
to your User-Agent string that differentiates your request from others, especially if you are on a shared machine such as
an ACMS machine.  For example:

Instead of:
```python
>>> result = requests.get("http://www.reddit.com/r/ucsd.json")
>>>
```

Use this:
```python
>>> result = requests.get("http://www.reddit.com/r/ucsd.json", headers = {'User-agent': 'spis19t3 bot 1.0'})
>>>
```

If that still doesn't work, you can get really devious, and try to mimic the User-agent string of an actual browser
that is known to be working.  You can use various developer tools inside browsers such as Chrome and Firefox to peek
at the HTTP headers that are being sent along with successful requests, and then try to spoof those headers.  This is
a bit "dirty", and it should not be abused.    It is important to respect the terms of service and limitations of data
providers.
