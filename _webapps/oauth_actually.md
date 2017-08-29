---
topic: "OAuth: Actually doing it"
desc: "Adding OAuth to an existing Flask Webapp"
indent: True
---


This tutorial assumes that you have already:

1. Understood how to work with sessions, as described here: [Sessions](/webapps/sessions/)
1. Read through the introductory material on OAuth here: [OAuth (introduction)](/webapps/oauth/)
1. Worked through the example of forking and configuring one of the OAuth working code examples from here: [OAuth: Deploy Examples](/webapps/oauth_deploy_examples)

# TODO: Insert instructions for adding OAuth to an existing non-OAuth based flask app with sessions

Note: this lesson is adapted from a sample webapp created by a SPIS instructor from 2016.

We're going to create a basic webapp with OAuth, step-by-step, with Github, restricting it to only the people inside the 2017 SPIS Github Organization. We're going to break down each and every part, especially the OAuth code that will be going in. First, create a repo on Github called `spis17-oauth-org-example-Name1-Name2`, add your partner, and then clone the repo into your github directory on your local workstation. Don't forget to commit when you finished implementing a feature or think it is a good place to save your work.

# Templates Set-Up

Before we dive into OAuth, we need to get some other files set up. First, we're going to set up the templates that render the webpages themselves. Inside your `spis17-oauth-org-example-Name1-Name2` directory, create a `templates` folder using the mkdir command. Then, cd into it. 

Here is the code for `layout.html`. Notice the similarities and differences from the lab. We'll explain the flash_messages in a bit. 

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->

    <!-- Bootstrap -->

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

  <!-- Optional theme -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  <title>{% raw %}{% block title %}{% endblock %}{% endraw %} - My Webpage</title>


  </head>
  <body>
    {% raw %}{% include 'navbar.html' %}{% endraw %}


    <div id="content">
    <!-- Serves as placeholder for flash_messages depending on the result from Github login -->
    {% raw %}{% include 'flash_messages.html' %} {% endraw %}

  {% raw %}{% block content %}{% endblock %}{% endraw %}</div>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->

  <!-- Latest compiled and minified JavaScript -->
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

  </body>
</html>
```


The code for `home.html` is:

```html
{% raw %}{% extends "layout.html" %}{% endraw %}

{% raw %}{% block title %}Home{% endblock %}{% endraw %}

{% raw %}{% block content %}{% endraw %}
  <h1>Home</h1>
  <ul>
    <li><a href="/page1">That thing we do</a></li>
    <li><a href="/page2">The other thing</a></li>
  </ul>

<p>This is a sample application to demonstrate authenticating against github oauth,
using Flask, on Heroku.   This app restricts logins only to members of the 
github organization: {% raw %}{{ github_org }}{% endraw %} </p>

{% raw %}{% endblock %} {% endraw %}
```

Here is the code for `navbar.html`. Notice the if-statements using the Jinja2 templates. It checks whether or not the user is logged in and updates what is shown on the navigation bar accordingly. Where does logged_in get its value? It pulls session data, injected from `webapp.py` (more on that later).

```html
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="/">Home</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li><a href="/page1">Page 1</a></li>
        <li><a href="page2">Page 2</a></li>
      </ul>
      
      <ul class="nav navbar-nav navbar-right">
      
   <!-- Checks if logged_in is true to display your github avatar and name -->  
   <!-- logged_in is injected from webapp.py using the token from OAuth -->
	{% raw %}{% if logged_in %}{% endraw %}
	      <li><a class="navbar-brand" href="#">
	      <img src="{{ session['user_data']['avatar_url'] }}&s=30" 
		     width="30" height="30" style="display: inline-block;" ></a></li>

	      <li><p class="navbar-text">{{ session['user_data']['name']}}</p></li>	
              <li><p class="navbar-text">Github userid: {{ session['user_data']['login']}}</li>
	{% raw %}{% endif %}{% endraw %}
  
        <!-- Displays the correct button to log the user in or out -->
        <li>
          {% raw %}{% if logged_in %}{% endraw %}
	          <a href="/logout">Logout</a>
	        {% raw %}{% else %}{% endraw %}
	          <a href="/login">Login</a>
	        {% raw %}{% endif %} {% endraw %}
	      </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
```

Next, we'll have the code for two sample pages, `page1.html` and `page2.html`. Notice the code on `page1.html`. The `<pre>` tags indicate an area for preformatted text. If this webapp has user data from being logged in via Github and Oauth, information will be presented there. If logged out, it'll remain empty. Here is `page1.html`:

```html
{% raw %}{% extends "layout.html" %}{% endraw %}

{% raw %}{% block title %}{% endraw %}page1{% raw %}{% endblock %}{% endraw %}

{% raw %}{% block content %}{% endraw %}
  <h1>This is Page 1</h1>

  <p>Lorem ipsum sit dolor amet.</p>

<pre>
  {% raw %}{{ dump_user_data }}{% endraw %}
</pre>

{% raw %}{% endblock %}{% endraw %}
```

Here is `page2.html`:
```html
{% raw %}{% extends "layout.html" %}

{% raw %}{% block title %}{% endraw %}page1{% raw %}{% endblock %}{% endraw %}

{% raw %}{% block content %}{% endraw %}
  <h1>This is Page 2</h1>

  <p>Lorem ipsum Tritons rule!</p>
{% raw %}{% endblock %}{% endraw %}
```

Finally, we have our `flash_messages.html`. Depending on how the OAuth login went (successful, unsuccessful, etc.), we will get messages. In this sample webapp, we're going to display what those messages are onto our web page. Here is the code for `flash_messages.html`:

```html
<div class="flash-messages">
{% raw %}{% with messages = get_flashed_messages(category_filter=["message"]) %}{% endraw %}
  {% raw %}{% if messages %}{% endraw %}
    <div class="alert alert-info">
      <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
      
      <ul>
        {% raw %}{%- for msg in messages %}{% endraw %}
          <li>{{ msg }}</li>
        {% raw %}{% endfor -%}{% endraw %}
      </ul>
    </div>
  {% raw %}{% endif %}{% endraw %}
{% raw %}{% endwith %}{% endraw %}

{% raw %}{% with errors = get_flashed_messages(category_filter=["error"]) %}{% endraw %}
  {% raw %}{% if errors %}{% endraw %}
    <div class="alert alert-warning">
      <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
      <ul>
        {% raw %}{%- for msg in errors %}{% endraw %}
          <li>{{ msg }}</li>
        {% raw %}{% endfor -%}{% endraw %}
      </ul>
    </div>
  {% raw %}{% endif %}{% endraw %}
{% raw %}{% endwith %}{% endraw %}
</div> <!-- End of class="flash-messages" -->
```

# Static & Style Set-Up

Next, we need to set up how the webpage elements look. Use the `cd ..` command to go up a level in your directory. You should now be back in your `spis17-oauth-org-example-Name1-Name2`. Make a directory called static, cd into it, and create a file called `style.css`. The code for this is simple:

```css
body {

}

#content {
     margin-left: 20px;
}

div.flash-messages {
  min-height: 4em;
}
```

Once you're done with this lesson, feel free to add, remove, or change values to this file to change your webapp to the way you want it to look. 

# Procfile & Requirements.txt

Remember, in order for our webapp to be hosted on Heroku, we need to create these two files. Your `Procfile` should have this line:

```
web: gunicorn webapp:app --log-file=-
```

Your `requirements.txt` should have these lines (Note the additional two lines at the bottom in this lesson): 

```
Flask==0.10.1
itsdangerous==0.24
Jinja2==2.8
MarkupSafe==0.23
Werkzeug==0.10.4
wheel==0.24.0
gunicorn==19.3.0
Flask-OAuthlib==0.9.3
PyGithub==1.26.0
```

# The fun stuff: `webapp.py` and OAuth

Now, we can *finally* dive deep into actual implementing OAuth. At the same level as your `templates` and `static` directories, create a file called `webapp.py`. We're going to add blocks of code, one block at a time. Each block of code should appear one after the other. With each block, we will go into detail with what it is doing. 

## Step 1

At the top of the file we should have all the right import statements so that we have the necessary modules. Some of these modules should look familiar. Some of the new lines include importing OAuth in line 3 and importing Github in line 5.

```python
from flask import Flask, redirect, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth
from flask import render_template, flash, Markup

from github import Github

import pprint
import os
import sys
import traceback
```

## Step 2

As you remember from the previous lessons, there are certain variables that act as keys that need be defined for the OAuth communication between our webapp and Github to work correctly. This block of code checks if these variables have not been defined. If they have not, it raises the exception, printing a message to define the 4 variables. We will go more in depth in later steps. 

```python
class GithubOAuthVarsNotDefined(Exception):
    '''raise this if the necessary env variables are not defined '''

if os.getenv('GITHUB_CLIENT_ID') == None or \
        os.getenv('GITHUB_CLIENT_SECRET') == None or \
        os.getenv('APP_SECRET_KEY') == None or \
        os.getenv('GITHUB_ORG') == None:
    raise GithubOAuthVarsNotDefined('''
      Please define environment variables:
         GITHUB_CLIENT_ID
         GITHUB_CLIENT_SECRET
         GITHUB_ORG
         APP_SECRET_KEY
      ''')
```

## Step 3

The first two lines are familiar to you. We call Flask to create the app and set debug to False to ensure safety. In the next line, we set the secret key (remember from sessions?) to the value found in the environment variable called 'APP_SECRET_KEY'. Since we're hosting it on Heroku, we will set these up in the next part of this article [here](), but we'll worry about that when we finish the rest of the code. Talk to a mentor if you're wondering about how to set it up on localhost. Finally, we're going to create an OAuth object with our app.

```python
app = Flask(__name__)

app.debug = False

app.secret_key = os.environ['APP_SECRET_KEY']
oauth = OAuth(app)
```

## Step 4

```python
# This code originally from https://github.com/lepture/flask-oauthlib/blob/master/example/github.py
# Edited by P. Conrad for SPIS 2016 to add getting Client Id and Secret from
# environment variables, so that this will work on Heroku.


github = oauth.remote_app(
    'github',
    consumer_key=os.environ['GITHUB_CLIENT_ID'],
    consumer_secret=os.environ['GITHUB_CLIENT_SECRET'],
    request_token_params={'scope': 'read:org'},
    base_url='https://api.github.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize'
)
```
