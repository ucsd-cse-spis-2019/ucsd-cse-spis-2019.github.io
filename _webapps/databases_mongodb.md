---
topic: "Databases: MongoDB"
desc: "NoSQL database system"
indent: true
---

For an introduction to Databases, and their role in webapps, see the article:

* [Webapps: Databases](/webapps/databases/)




# MongoDB

<div style="width:80%; padding: 1em; margin: 1em; border: 2px solid red;" markdown="1">

UPDATE: It turns out that the MongoDB service on Heroku, even though it is "free", requires entering a credit card for "account validation".  We therefore do not wish to use it during SPIS.

We might go back to using Heroku Postgres instead, since it does NOT require credit card validation.

</div>

There is a Python module called [Flask-PyMongo](http://flask-pymongo.readthedocs.io/en/latest/) that we can install with `pip install` to make working with MongoDB easier.

To install it on ACMS, use:

```
pip install --user Flask-PyMongo
```

on Windows or Mac, just:

```
pip install Flask-PyMongo
```

You'll also need to make sure that you add these lines to the `requirements.txt` file for any webapp that you want to 
run on Heroku with MongoDB:

```
Flask-PyMongo==0.4.1
pymongo==3.3.0
```

