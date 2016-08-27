---
topic: "Webapps Intro, Part 5"
desc: "Working with Sessions in Flask"
---

# Sessions in Flask

To do anything remotely interesting with a web application, you must build on the concept of a *session*.

A *session* is a place that we can store some information, temporarily, while a user navigates from one page to another within our web
application.    

Here is an example of a running application on Heroku that uses sessions:

* [http://calm-caverns-10201.herokuapp.com/](http://calm-caverns-10201.herokuapp.com/)
* The code for that app is here: [https://github.com/ucsd-cse-spis-2016/spis16-webapps-flask-sessions](https://github.com/ucsd-cse-spis-2016/spis16-webapps-flask-sessions)
* In this lesson we'll go through the code that makes this example work.

## How do you use a session?

To create a session in Flask, you first need to import the session object from flask:

```python
from flask import session
```

You also need to set a secret key.  

The secret key is used to encrypt our session to avoid something called "session hijacking", which
is a way that an evildoer can hack into a running web app session and take it over (potentially stealing private data, or creating other mayhem).

The value of the secret key can be pretty much any string of letters and digits.  More information on the secret key can be found here: [http://flask.pocoo.org/docs/0.10/quickstart/#sessions](http://flask.pocoo.org/docs/0.10/quickstart/#session)

Set the secret key sometime after the `app = Flask(__name__)` line.

```python
app = Flask(__name__)
app.secret_key='w98fw9ef8hwe98fhwef'   # This sets the secret key for sessions
```

In this example, the secret key is hard coded right in the Python code that implements
the web app, which is fine for a simple example, but there are better ways to do it, such as reading the value
from an environment variable.   We'll discuss how that works when we get to OAuth and databases.



## Some things to know about sessions:

* A session is created when the user navigates to some page that has code on the backend (the Python part of our web application) that
    creates the session.
* Each page we visit can then store things into the session, or get things out of the session.
* The session is temporary: if you close the browser, restart the Python code that is running your server, 
    the session object goes away.  (For more permanent storage we typically use a database of some kind; more on that later.)
* Webapps typically offer the user some way (e.g. by clicking a button) to start a new session.   Starting a new session
    discards everything in the current session, and starts from scratch.
* It is typically not possible to have two sessions running at a time in the same browser.  If you want to test with multiple
    sessions, you can use multiple browsers, or the "incognito"/"private-browsing" feature that most browsers offer.

## The concept of a session is not specific to Flask or Python

You'll find the concept of a session in pretty much every web framework, regardless of whether you are using Python 
for your web "backend" language, or something else such as Java, PHP, Ruby on Rails, Node (server-side JavaScript), etc.
