---
topic: "Webapps Intro, Part 2.5"
desc: "Better Navigation on your Web App - Nav Bars"
---

In the part 3 of your lab, we created a simple web app that had 3 functions, allowing a user to convert temperatures (Celsius to Fahrenheit, Fahrenheit to Celsius) and distance (miles to kilometers).

You might have noticed that after you submitted a value to convert, you couldn't get to the home page or reach any of the other forms to convert different things. 

## Enter the Navigation Bar

Most websites and web applications are designed so that you can easily get around. An easy to implement good navigation is with a navigation bar. Nav bars allow users to have links that are persistent on the web page so they can quickly get to places on your web app. What's the point of a great app if you can't get to the good stuff? 

In this part, we will create a nav bar so that users can quickly get around all of the amazing web pages you just created. 

## Bootstrap: A simple way to get started

We're going to implement this using a library called Bootstrap. Bootstrap is a free and easy way to get responsive features and styles. An article written by the staff from SPIS 2016 with more information and an example web app can be found [here](/_webapps/bootstrap). We will be implementing a more simpler example.

## Back to all those templates (layout.html)

Remember all those templates from Part 2? We're going to use them again.

We want our navigation bar to be present no matter what webpage we are on so that we can always get to where we need to be. Every single one of our webpages files extend `layout.html` so we want to first add some code in there. We have to get it set up so that our web app knows to go to Bootstrap for information. The new lines of code are long with a lot of links, but don't feel overwhelmed! Take your time if you're unsure. Let's start with our `<head>` tags, which should currently look something like this: 

```html
<!doctype html>
<html>
  <head>
     <link rel="stylesheet" href="{% raw %}{{{% endraw %} url_for('static', filename='style.css') {% raw %}}}{% endraw %}">
     <title> {% raw %}{% block title %}{% endblock %}{% endraw %} - My Webpage</title>
   </head>
```

Inside the head tag and before the two lines we currently have, we are going to add some lines of code. First, We need to let the web app know what character encoding standard we are using. UTF-8 (Unicode) covers most of the characters we need. If you want more information, you can check this w3schools article [here](https://www.w3schools.com/html/html_charset.asp). 

```html
  <meta charset="utf-8">
```

Next, we have a line of code to help with the responsiveness of your web app as you change the size of the window. Note the comment: 

```html
   <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above meta tag *must* come first in the head; any other head content must come *after* these tags -->
 ```

Finally, we have to code to get access to Bootstrap and being able to use it. With these links, we'll be able to access Bootstrap's CSS code to easily style our web app. Feel free to copy and paste the long Bootstrap links into your own file.

```html
  <!-- Bootstrap -->

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

  <!-- Optional theme -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous"
```

Your `layout.html` file should now look a little something like this: 

```html
<!doctype html>
<html>
  <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <!-- The above meta tag *must* come first in the head; any other head content must come *after* these tags -->
     
     <!-- Bootstrap -->

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous"
     
     <link rel="stylesheet" href="{% raw %}{{{% endraw %} url_for('static', filename='style.css') {% raw %}}}{% endraw %}">
     <title> {% raw %}{% block title %}{% endblock %}{% endraw %} - My Webpage</title>
   </head>
```

We're almost done with `layout.html`! Now we need include some code inside the body. First, we'll add this line right underneath the `<body>` tags: 

```html
{% raw %}{% include 'navbar.html' %}{% endraw %}
```

This will ensure that our navbar will appear on every single web page. We'll create this file in the next step of the lab. 

Now, beneath our `<div>` tags with the block content, we need to include JavaScript plugins so that Bootstrap works correctly. We won't go into too much detail here, but we will be using [jQuery](https://jquery.com), a JavaScript library. Again, W3 Schools is a great resource and you can play around in your free time with jQuery [here](https://www.w3schools.com/jquery/).

Your final `<body>` tags should look a little something like this:

```html
  <body>
    {% raw %}{% include 'navbar.html' %}{% endraw %}
    <div id="content">{% raw %}{% block content %}{% endblock %}{% endraw %}</div>
     
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->

    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
  </body>
```

## Creating the acutal navbar
