---
topic: "APIs"
desc: "Application Programming Interfaces"
---

# APIs: your gateway to data from Google, Facebook, Twitter, Reddit, etc.

An *Application Programming Interface*, or API, is a way that your own program can interact with 
data from another piece of software.  That software might be something provided by Google, Facebook, Twitter, 
Reddit, etc.

# API keys and Rate Limits

Some APIs are open APIs, which means you can use them without having to register first.  These are typically *rate limited*
meaning that you can only access the API a certain number of times per minute, or per hour.   These limits are usually
pretty low. They are find for initial testing, but for anything beyond that, you typically need to get an API key.

The API key is something you should NOT hard code in your Python code and then store in github.  Instead, you should
use the same techniques used for the OAuth GITHUB_CLIENT_ID and GITHUB_CLIENT_SECRET that are documented elsewhere on this
website, namely storig the value in environment variable (TODO: Link to description of that technique).   That involves:

* setting up an `env.sh` for use when running on your own laptop or ACMS account
* using 'congiguration variables' when running on Heroku

# Direct, or via a library

There are two main ways to work with an API from Python code

* Directly, through calls to the a library such as `urllib` or `requests`, where you directly interact with the web addresses
    provided in the API.  
* Through a Python library that provides a more convenient interface.

I *highly recommend* using a library whenever one is available.

# A few APIs 

* Google Places API
    * Working Example: <https://github.com/ucsd-cse-spis-2016/spis19-webapps-google-places-demo>  
    * Main Page: [https://developers.google.com/places/](https://developers.google.com/places/)
    * Python Library: <https://github.com/slimkrazy/python-google-places>
    * Code to do it "by hand": <https://andrewpwheeler.wordpress.com/2014/05/15/using-the-google-places-api-in-python/>
    * Commentary from stack overflow: <http://stackoverflow.com/questions/18485044/where-do-i-find-the-google-places-api-client-library-for-python>
    

# 
