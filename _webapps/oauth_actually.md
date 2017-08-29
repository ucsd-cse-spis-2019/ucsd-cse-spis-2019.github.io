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

We're going to create a basic webapp with OAuth, step-by-step. We're going to break down each and every part, especially the OAuth code that will be going in. First, create a repo on Github called `spis17-oauth-org-example-Name1-Name2`, add your partner, and then clone the repo into your github directory on your local workstation. Don't forget to commit when you finished implementing a feature or think it is a good place to save your work.

# Templates Set-Up

Before we dive into OAuth, we need to get some other files set up. First, we're going to set up the templates that render the webpages themselves. Inside your `spis17-oauth-org-example-Name1-Name2` directory, create a `templates` folder using the mkdir command. Then, cd into it. 

The code for `layout.html` is: 

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
github organization: {{ github_org }} </p>

<p>The source code is available on github at <a href="">TODO</a></p>


{% raw %}{% endblock %} {% endraw %}

```
