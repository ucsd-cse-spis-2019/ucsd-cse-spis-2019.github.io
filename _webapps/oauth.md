---
topic: "OAuth"
desc: "Delegating username/password authentication to Github, Facebook, Google, etc."
---

Here's an example: 

<https://github.com/ucsd-cse-spis-2015/flask-oauth-example>

Here is another example:
<https://github-flask.readthedocs.io/en/latest/>


# Using Flask-OAuthlib

[Flask-OAuthlib](https://flask-oauthlib.readthedocs.io/en/latest/index.html) is a Python module that you can use to add 
authentication to your webapp via any OAuth provider.  

In this section, we'll discuss how to use Github as our OAuth provider, since every SPIS 2016 participant has a github account.

## `pip install Flask-OAuthlib`

First, on any system where you want to use this library, you need to install it.

On ACMS, that's 

```
pip install --user Flask-OAuthlib
```

On Mac or Windows, it's probably just

```
pip install Flask-OAuthlib
```

If you run into problems with that, ask a mentor or instructor for assistance.

## Example code


