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

# Back to all those Templates

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
