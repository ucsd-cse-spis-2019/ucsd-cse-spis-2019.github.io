---
topic: "Webapps Intro, Part 2"
desc: ""
---

# Keeping your ACMS Account Safe

So, trying to teach web development in an academic computing environment such as ACMS is always a bit of a risk.   The basic problem is this combination of things:

* Web servers, by their very nature while under development, can contain security vulnerabilities
* Because of this, web developers typically test web apps on systems that "have one job", i.e. to test a web app, 
    and are used by "only one user", the one doing the web app development.
* But, in an academic computing environment, it is typical for many students, (i.e. many users), to all be running on the      same system.
* Hence, the problem.

This is not a show-stopper of a problem.  There are some reasonable things you can do to mitigate the risk.   You should definitely do these things. 

To use Flask safely on ACMS, do NOT enable debug mode:

```python
app.run(debug=True)  # DO NOT do this on your ACMS ACCOUNT
```

If you do set `debug=True`, that allows anyone that can bring up your web app to execute any line of Python code they want, but as you, in your account.  That means they could launch a spambot, delete all your files, or do something even more awful.

```
app.run(debug=False)   # ALWAYS DO THIS when  RUNNING ON ACMS, THIS IS THE SAFE THING TO DO
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

```
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

# What comes next?

Our next steps will be to learn a bit about:

* HTML and CSS, the languages we use to make our web pages look like "real web pages" instead of just plain text.
* Both of those are for our next lesson, but we can at least get a head start if you've finished this material early.

# HTML and CSS

So, at the moment, the values we are returning from our functions are plain text that shows up in the browser.  That's fine for getting started, but eventually we'd like something that looks like a "real web page". For that, we'll need to learn a little bit about HTML and CSS.   That's for our next lesson.

If you want to get started on learning HTML and CSS now though, one of the best resources on the web for that is the site: [w3schools.com](http://w3schoos.com)

* Visit their HTML tutorial to get started
* After learning some HTML, learn a bit of CSS


# The next lesson

The next lesson is [Web Apps Intro (part 3)](/webapps/webapps-intro-part-3.md)

 
