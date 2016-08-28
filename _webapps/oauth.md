---
topic: "OAuth"
desc: "Delegating username/password authentication to Github, Facebook, Google, etc."
---

# TODO: Introductory material about OAuth

Explain what OAuth is, and why we need it here.

# Example code: 

TODO: Explain these examples a bit more

* Simple github oauth: <https://github.com/ucsd-cse-spis-2016/spis16-webapps-oauth-example>
    * If you have a github account, you can log in.
    * This app only works with sessions; no connection to a database
    * No ability to store user preferences, or any other persistent data
* Github OAuth based on organization membership: <https://github.com/ucsd-cse-spis-2016/spis16-webapps-oauth-github-org-example>
    * Checks is you have a github account, AND if you are a member of specific github organization specified by the application (e.g. `ucsd-cse-spis-2016`, for example.)
    * Like preceding one, this app only works with sessions; no connection to a database
    * No ability to store user preferences, or any other persistent data

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


# References

* <https://github-flask.readthedocs.io/en/latest/>


