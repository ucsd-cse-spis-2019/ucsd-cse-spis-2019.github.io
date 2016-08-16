---
topic: "Python: JSON"
desc: "Access JSON data in Python"
---

# Python: Accessing JSON Data 

There is a notation called *JSON*, which stands for *JavaScript Object Notation*.  Although this notation
comes from the language *JavaScript*, it is used across many languages other than JavaScript, including Python.

Many websites and other data services provide access to data in JSON format.  

One easy example to see is the social media site [reddit.com](https://reddit.com).  

* Side note: Before going further, let us
    acknowledge that there are some controversies about the [reddit.com](https://reddit.com) site, some of which
    provoke passionate opinions.  If there were a better example website, I would use it.   The reason I use
    reddit.com is not because I necessarily endorse the site, but because it is one of the easiest sites for
    beginners to get access to JSON data easily and quickly.

The site reddit.com has various online communities called *subreddits*.  Most college/universities have one;
for example, here are the ones for the various UC Campuses with undergraduate programs:

| School	| Subreddit link	| School web page   |
|---------|-----------------|-------------------|
| UC Berkeley	| http://www.reddit.com/r/berkeley/	| http://www.berkeley.edu |
| UC Davis	| 	http://www.reddit.com/r/ucdavis	| 	http://www.ucdavis.edu	| 
| UC Irvine		| http://www.reddit.com/r/uci		| 	| http://www.uci.edu	| 
| UCLA	| 	http://www.reddit.com/r/ucla/		| http://www.ucla.edu	| 
| UC Merced		| http://www.reddit.com/r/ucmerced	| 	http://www.ucmerced.edu/	| 
| UC Riverside	| 	http://www.reddit.com/r/ucr/	| 	www.ucr.edu	| 
| UC San Diego	| 	http://www.reddit.com/r/ucsd	| 	http://www.ucsd.edu	| 
| UC Santa Barbara	| 	http://www.reddit.com/r/ucsantabarbara	| 	http://www.ucsb.edu	| 
| UC Santa Cruz	| 	http://www.reddit.com/r/ucsc	| 	http://www.ucsc.edu	| 

Suppose you visit the page for the UCSD subreddit.  If you simply add the following characters: `.json` to the URL,
you'll get a representation of the content of the page in JSON format:


* UCSD Subreddit: http://www.reddit.com/r/ucsd
* UCSD Subreddit in JSON format: http://www.reddit.com/r/ucsd.json

Here is a snapshot of what some of that JSON looks like.  Because it goes on for pages and pages,
I'm showing only the first few lines, and this excerpt will likely *not* be valid since its clipped off in the middle.

```json
{"kind": "Listing", "data": {"modhash": "", "children": [{"kind": "t3", "data": 
{"domain": "self.UCSD", "banned_by": null, "media_embed": {}, "subreddit": "UCSD",
"selftext_html": "&lt;!-- SC_OFF --&gt;&lt;div class=\"md\"&gt;&lt;p&gt;I&amp;#39;m 
basically just copying this directly from last year&amp;#39;s Q&amp;amp;A, but
I don&amp;#39;t think many things have changed. (so thank &lt;a 
href=\"/u/inconditus\"&gt;/u/inconditus&lt;/a&gt; for this, because they wrote most
of it)&lt;/p&gt;\n\n&lt;p&gt;So, you got into UCSD, congratulations! It&amp;#39;s a
great school! But you have questions, most of which the administration can&amp;#39;t 
help you with. Come ask us! I&amp;#39;m rolling over a lot of info from the &lt;a 
```
etc...

The point is that data in JSON format can be easily converted into a Python dictionary.

Here's how.

First, here is some code that we can type in at the Python prompt just to experiment a bit.

There is a Python module called `requests` that we can use to get data from a website.

We simply type `import requests`, then assign a variable to the result of `requests.get(url)`,
where `url` is a Python string with a web address.  For example:

```
>>> import requests
>>> result = requests.get("https://www.reddit.com/r/ucsd.json")
```

Now, if we type `result.text`, we get the entire contents of that web page (in this case, all the JSON that
was returned.   I'm not showing the whole thing, because it is enormous.  Here are just the first 100 characters:



```
>>> result.text[:400]
u'{"kind": "Listing", "data": {"modhash": "", "children": [{"kind": "t3", "data": {"domain": 
"self.UCSD", "banned_by": null, "media_embed": {}, "subreddit": "UCSD", "selftext_html":
"&lt;!-- SC_OFF --&gt;&lt;div class=\\"md\\"&gt;&lt;p&gt;I&amp;#39;m basically just copying
this directly from last year&amp;#39;s Q&amp;amp;A, but I don&amp;#39;t think many things
have changed. (so thank &lt;a href=\\"/u/'
>>> 
```

We can see how big it is by using `len`.  The `type` comes back as `unicode` rather than `str`;
that just means that it is a special type of string, one that may have various kinds of international
characters in it. (That's an oversimplification of what unicode is, but if you are curious, you can 
look up the details yourself.)

```
>>> len(result.text)
67435
>>> type(result.text)
<type 'unicode'>
>>>
```

We can convert the `result.text` into a Python dictionary using the following Python code:

```python
>>> import json
>>> rdata = json.loads(result.text)
>>> type(rdata)
<type 'dict'>
>>> 
```

Now, `rdata` is a Python dictionary that contains the data from the UCSD subreddit that we retrieved.

This opens up many possibilities for processing the data using Python code.

But what?

One of the problems with this `rdata` dictionary is that it is so big.   If we try to see all of it, it goes
on for pages and page:

```python
>>> rdata
{u'kind': u'Listing', u'data': {u'modhash': u'', u'children': [{u'kind': u't3', u'data': {u'domain': u'self.UCSD', u'banned_by': None, u'media_embed': {}, u'subreddit': u'UCSD', u'selftext_html': u'&
```
<em>... dozens of lines omitted ... </em>
```
se, u'created': 1471193347.0, u'url': u'https://www.reddit.com/r/UCSD/comments/4xnf96/fraternities_or_dance_groups/', u'author_flair_text': None, u'quarantine': False, u'title': u'Fraternities or dance groups?', u'created_utc': 1471164547.0, u'ups': 3, u'num_comments': 4, u'visited': False, u'num_reports': None, u'distinguished': None}}], u'after': u't3_4xnf96', u'before': None}}
>>>
```

So, what can we do?   One possibility is to just find out: what keys are at the top level of this dictionary?

We can do that by typing `rdata.keys()`.   (Note that the `u` in front of `kind` and `data` just indicates
that it is a unicode string instead of a regular string.)

```python
>>> rdata.keys()
[u'kind', u'data']
>>> 
```

So, we know that, at the top level, the dictionary `rdict` contains two key value pairs.  That is, 
it is of the form `rdata = { u'kind': `<em>something</em>`, u'data': `<em>something-else</em>` }`

So, we can try to next figure out, what is the <em>something</em> and the <em>something-else</em>.

The first <em>something</em> is going to accessed by `rdata[u'kind']`:

```python
>>> rdata[u'kind']
u'Listing'
>>> 
```

We see that it is a `Listing'.   So, let's figure out what the <em>something-else</em> is.  We type
`rdata[u'data']` and we get another super long listing:

```python
>>> rdata[u'data']
```
<em>way too much output here...</em>
```
>>> 
```

So, instead of listing the whole thing, we
can try to ask another question: what <em>type</em> thing is it?

```python
>>> type(rdata[u'data'])
<type 'dict'>
>>> 
```

Ah, that is better.  We see that it is a dictionary object. So we can repeat the process we used before with
a "too big" dictionary, that is, asking what its keys are:

```python
>>> rdata[u'data'].keys()
[u'modhash', u'children', u'after', u'before']
>>>
```

What we get back is a python list of the keys for `rdata[u'data']`.    We see that there are four of them:

1. `u'modhash'`
1. `u'children'` 
1. `u'after'` 
1. `u'before'`

We can represent what we've learned about `rdata` so far by drawing a diagram.  It looks like this:

<img src="https://docs.google.com/drawings/d/1zRIQIeaTI3-AZskqwvYvtwv_3Q_EPQnGtZqi-HdTtBE/pub?w=966&amp;h=422">


