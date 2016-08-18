---
topic: "Webapps Intro, Part 2"
desc: "ftoc (from url), and intro to templates"
---

In part 2 of the SPIS 2016 webapps tutorial, we'll learn about how to:

* Perform a calculation based on a parameter that's in the url
* Start building a larger multi-page web application

## Keeping your ACMS Account Safe: turn debug mode off.

So, trying to teach web development in an academic computing environment such as ACMS is always a bit of a risk.   The basic problem is this combination of things:

* Web servers, by their very nature while under development, can contain security vulnerabilities
* Because of this, web developers typically test web apps on systems that "have one job", i.e. to test a web app, 
    and are used by "only one user", the one doing the web app development.
* But, in an academic computing environment, it is typical for many students, (i.e. many users), to all be running on the      same system.
* Hence, the problem.

This is not a show-stopper of a problem.  There are some reasonable things you can do to mitigate the risk.   You should definitely do these things. 

To use Flask safely on ACMS, do NOT enable debug mode:

```python
app.run(port=5000,debug=True)  # DO NOT do this on your ACMS ACCOUNT
```

If you do set `debug=True`, that allows anyone that can bring up your web app to execute any line of Python code they want, but as you, in your account.  That means they could launch a spambot, delete all your files, or do something even more awful.

```
app.run(port=5000,debug=False)   # ALWAYS DO THIS when  RUNNING ON ACMS, THIS IS THE SAFE THING TO DO
```
This is the safe thing to do when running on ACMS.

Note that debug mode is really useful, but if you want to be able to use it, you'll need to invest the time in installing Python on your own personal computer (laptop or desktop) and then running Flask there.   That's the only safe environment to turn debug mode on—when you can be totally sure that no-one but you can get to the web browser where debug mode is enabled.

# Our next step with Flask: actually computing something

Ok, a web page that prints "Hello World" is not really very compelling.  Let's do something a bit more interesting.

## Add an ftoc function to hello.py

We've already seen a function that converts Farenheit to Celsius.  Let's add this to our hello.py file, so that we have the following:

Put these lines of code in a file called hello.py

```python
def ftoc(ftemp):
   return (ftemp-32.0)*(5.0/9.0)
```

Then, add the additional lines of code shown in the example below:

```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

def ftoc(ftemp):
   return (ftemp-32.0)*(5.0/9.0)

if __name__ == "__main__":
    app.run(port=5000)
```

Now, you can test your function by doing this: 
* Save your file
* Go to IDLE shell prompt and type `from hello import ftoc`
* Try various values of ftoc, such as ftoc(212.0) and ftoc(32.0)
* If your ftoc function works, then you are good to go the next step where we hook this up to the web app.

# Hooking this up to the web app

To make this code work with the web app, we need to add a few more lines of code.

First, we'll just do it and see what it does, then we'll unpack each line of code and explain its purpose.



{% highlight python linenos %}
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
def ftoc(ftemp):
   return (ftemp-32.0)*(5.0/9.0)

@app.route('/ftoc/<ftempString>')
def convertFtoC(ftempString):
    ftemp = 0.0
    try:
        ftemp = float(ftempString)
        ctemp = ftoc(ftemp)
        return "In Farenheit: " + ftempString + " In Celsius " + str(ctemp) 
    except ValueError:
        return "Sorry.  Could not convert " + ftempString + " to a number"

if __name__ == "__main__":
    app.run(port=5000)
{% endhighlight %}

Now try running that.   

You should now be able to put in URLs such as these where the last part is a farenheit temperature you want to convert to Celsius:

* [`http://localhost:5000/ftoc/212.0`](http://localhost:5000/ftoc/212.0)
* [`http://localhost:5000/ftoc/32.0`](http://localhost:5000/ftoc/32.0)
* [`http://localhost:5000/ftoc/-40.0`](http://localhost:5000/ftoc/-40.0)

Try it and see what you get.

Also try some URLs where the last part is not valid, e.g.

* [`http://localhost:5000/ftoc/banana`](http://localhost:5000/ftoc/banana)
* [`http://localhost:5000/ftoc/foobar`](http://localhost:5000/ftoc/foobar)

If you've gotten this far, you've gotten a great start.


# How does it work?

One of the keys to understanding how Flask works is to focus first on these lines of code in hello.py.

```python
@app.route('/')
@app.route('/ftoc/<ftempString>')
```

The parts of our code that start with the `@` sign are called decorators.  In this case, they come right before a function definition, and they tell Python to do something special with the function definition that follows.  

In this case, the `@app.route(path)` decorator indicates that URLs that end in path should be routed to the function that follows.    

In the path parameter of the `app.route` decorator, anything in angle brackets, such as `<ftempString>` stands for a value that is passed into the function as a parameter.  These are always of type `str` (string) and therefore have to be converted if they are going to be used as something else (e.g. `float`, `int`, etc.)

Now try some things on your own


# Try the following for practice:

* Add a function that converts miles to kilometers, i.e. def milesToKm(miles): ... that just like the ftoc function, is a "pure" function that "doesn't know its part of a web app".

* Then, add a function with a decorator `@app.route('/mtokm/<milesString>')` that will convert the `milesString` into a number, pass it into the function, and produce output.  You can use the `convertFtoC` function as an example to build on.
* If that works, then see if you can write your own function.  Note that you can use a route such as `@app.route('someroute/<a>/<b>/<c>')` if you wanted to have a function that took three inputs instead of just one.   

# Templates


Our next steps will be to learn a bit about:

* HTML and CSS, the languages we use to make our web pages look like "real web pages" instead of just plain text.
* Both of those are for our next lesson, but we can at least get a head start if you've finished this material early.

# HTML and CSS

So, at the moment, the values we are returning from our functions are plain text that shows up in the browser.  That's fine for getting started, but eventually we'd like something that looks like a "real web page". For that, we'll need to learn a little bit about HTML and CSS.   That's for our next lesson.

If you want to get started on learning HTML and CSS now though, one of the best resources on the web for that is the site: [w3schools.com](http://w3schools.com)

* Visit their HTML tutorial to get started
* After learning some HTML, learn a bit of CSS

# Using Templates

Now that we know a bit about HTML, we can try building a multi page application that uses HTML
on each page.

Here is an example of how that would look.  You need to create a subdirectory called `templates`.

Into that directory, the first file you should create and store is one called `layout.html`

That file should look like this.   You can use idle to create a new file, copy/paste the following HTML code into the
file, and then save it in your templates directory with the name `layout.html`.

```html
<!doctype html>
<html>
  <head>
     <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
     <title> {% raw %}{% block title %}{% endblock %}{% endraw %} - My Webpage</title>
   </head>

  <body>
    <div id="content">{% raw %}{% block content %}{% endblock %}{% endraw %}</div>
  </body>
</html>
```


This file `layout.html` defines a template for every page of your web application. 

There are two parts of this file that are, strictly speaking, not HTML code. Those are:
* `{% raw %}{%  block title %}{% endraw %}{% raw %}{%  endblock %}{% endraw %}` 
* `{% raw %}{%  block content %}{% endraw %}{% raw %}{%  endblock %}{% endraw %}` 

These are placeholders where some other HTML code will be inserted, and the syntax is defined by a system called
Jinja2, which is part of the Flask framework.    That's all you really need to know about Jinja2 for now, but if you are curious to learn more, there is documentation here: [http://jinja.pocoo.org/](http://jinja.pocoo.org/).

The `title` and `content` blocks for each of our pages are going to be defined in additional files in our `templates` directory. 

## Creating a template for the home page

Now you can define the templates for the rest of the pages in your web application.   Let's make a web application with three pages: one that converts fahrenheit to celsius, another than converts celsius to fahrenheit, and a third that
converts miles to kilometers.

The template for the home page will be called `home.html` and should be in the `templates` subdirectory.  It will look like this:

```html
 {% raw %}{%  extends "layout.html" %}{% endraw %}

 {% raw %}{%  block title %}{% endraw %}Home{% raw %}{%  endblock %}{% endraw %}

 {% raw %}{%  block content %}{% endraw %}
  <h1>Home</h1>
  <ul>
    <li><a href="/ctof">Convert celsius to Fahrenheit</a></li>
    <li><a href="/ftoc">Convert Fahrenheit to Celsius</a></li>
    <li><a href="/mtokm">Convert Miles to Kilometers</a></li>
  </ul>
 {% raw %}{%  endblock %}{% endraw %}
```

## Creating templates for pages with user input

Then you'll have three more templates for the pages where you ask the user for the input for each of these
calculations.   Here are the first two, which you should call `ctof.html` and `ftoc.html`.  Each of these should be 
stored under your templates directory.

Here's `ctof.html`:

```html
{% raw %}{%  extends "layout.html" %}{% endraw %}

{% raw %}{%  block title %}{% endraw %}Convert ctof{% raw %}{%  endblock %}{% endraw %}

{% raw %}{%  block content %}{% endraw %}

<p>Enter a temperature and click "submit" to convert to Fahrenheit</p>

<form action="/ctof_result">
  Fahrenheit Temp:<br>
  <input type="text" name="cTemp" value="20.0">
  <input type="submit" value="Submit">
</form>

{% raw %}{%  endblock %}{% endraw %}
```

Here's `ftoc.html`:

```html
{% raw %}{%  extends "layout.html" %}{% endraw %}

{% raw %}{%  block title %}{% endraw %}Convert ftoc{% raw %}{%  endblock %}{% endraw %}

{% raw %}{%  block content %}{% endraw %}

<p>Enter a temperature and click "submit" to convert to Celsius</p>

<form action="/ftoc_result">
  Fahrenheit Temp:<br>
  <input type="text" name="fTemp" value="68.0">
  <input type="submit" value="Submit">
</form>

{% raw %}{%  endblock %}{% endraw %}
```

You'll also need a file in `templates` called `mtokm.html`.  For now, just enter the following html code as a placeholder&mdash;getting that one to work is left as an exercise for you.

Here's `mtokm.html`:

```html
{% raw %}{%  extends "layout.html" %}{% endraw %}

{% raw %}{%  block title %}{% endraw %}Convert miles to kilometers{% raw %}{%  endblock %}{% endraw %}

{% raw %}{%  block content %}{% endraw %}

<p>Coming soon...</p>

{% raw %}{%  endblock %}{% endraw %}
```

## Creating templates for the results pages

Finally you'll need three templates for the HTML for the pages that come up after you do the conversions.  

Those will be called `ftoc_result.html`, `ctof_result.html` and `mtokm_result.html`.  Here's what the first two 
of those will look like:

Here's `ftoc_result.html`:

```html
{% raw %}{%  extends "layout.html" %}{% endraw %}

{% raw %}{%  block title %}{% endraw %}Result of converting Fahrenheit to Celsius{% raw %}{%  endblock %}{% endraw %}

{% raw %}{%  block content %}{% endraw %}
<p> In Fahrenheit: {% raw %}{{ fTemp }}{% endraw %}.  In Celsius: {{ cTemp }} </p>
{% raw %}{%  endblock %}{% endraw %}
```

Here's `ctof_result.html`:

```html
{% raw %}{%  extends "layout.html" %}{% endraw %}

{% raw %}{%  block title %}{% endraw %}Result of converting Celsius to Fahrenheit{% raw %}{%  endblock %}{% endraw %}

{% raw %}{%  block content %}{% endraw %}
<p> In Celsius: {{ fTemp }}.  In Fahrenheit: {{ cTemp }} </p>
{% raw %}{%  endblock %}{% endraw %}
```

Finally, you'll also need a `mtokm_result.html` file.    Here's a placeholder for it.  The final content is up to you to fill in:

```html
{% raw %}{%  extends "layout.html" %}{% endraw %}

{% raw %}{%  block title %}{% endraw %}Result of converting Miles to Kilometers{% raw %}{%  endblock %}{% endraw %}

{% raw %}{%  block content %}{% endraw %}
<p>Coming soon...</p>
{% raw %}{%  endblock %}{% endraw %}
```

## Adding a `style.css` file

You should also create a subdirectory of the top of your repository called `static`, at the same level as your `hello.py` file, and as a sibling of your `templates` directory (not inside it.)

Inside that folder, put a file called `style.css`.   This file will contain rules for the fonts, colors, spacing, and layout for your web page, expressed in a language called CSS, which stands for *Cascading Style Sheets*.

Here is a basic `style.css` file. You can learn more about CSS rules at [w3schools.com](http://w3schools.com) and experiment with the style if you like.

```css

body {
    background-color: #eef;
    color: black;
}

```

Other things that might go into our `static` directory later on include things like images (.png, .jpg files) that we may want to display on our web pages.

## Changes to `hello.py` to use templates

Finally, we are ready for the changes to our `hello.py` that allow us to use these templates.

For each of the different URLs that our web application can serve, we will still write a function, just like before.
But this time, instead of directly returning the string that makes up the web page, we'll call the Flask function
`render_template`, like this:

```
@app.route('/')
def renderMain():
    return render_template('home.html')
```

Here's a complete example of the code that we'll want to put into our hello.py file.

Note the the additional `import` statements that are needed:

```python
import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('home.html')

@app.route('/ctof')
def render_ctof():
    return render_template('ctof.html')

@app.route('/ftoc')
def render_ftoc():
    return render_template('ftoc.html')

@app.route('/mtokm')
def render_mtokm():
    return render_template('mtokm.html')
    
@app.route('/ftoc_result')
def render_ftoc_result():
    try:
        ftemp_result = float(request.args['fTemp'])
        ctemp_result = ftoc(ftemp_result)
        return render_template('ftoc_result.html', fTemp=ftemp_result, cTemp=ctemp_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route('/ctof_result')
def render_ctof_result():
    try:
        ctemp_result = float(request.args['cTemp'])
        ftemp_result = ctof(ctemp_result)
        return render_template('ctof_result.html', cTemp=ctemp_result, fTemp=ftemp_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route('/mtokm_result')
def render_mtokm_result():
    try:
        # You'll need some code here, and maybe some extra parameters in render_template below...
        return render_template('mtokm.html')
    except ValueError:
        return "Sorry: something went wrong."

def ftoc(ftemp):
   return (ftemp-32.0)*(5.0/9.0)
    
def ctof(ftemp):
   return -42.0 # replace with correct formula

# You'll probably want a basic function here to convert miles to kilometers too...
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
```


# The next lesson

The next lesson is [Web Apps Intro (part 3)](/webapps/webapps-intro-part-3/)

In that lesson, you'll learn how to start hosting your webapps on Heroku so that they can be accessed by anyone anywhere,
and not just looking at a web browser on your local computer.

 
