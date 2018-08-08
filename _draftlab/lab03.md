---
layout: lab
num: lab03
ready: true
desc: "More functions and drawing with Turtle Graphics"
assigned: 2018-08-13 12:00:00.00-7
due: 2018-08-16 15:00:00.00-7
---

If you find typos or problems with the lab instructions, please report them on [Piazza]({site.piazza}}


Goal
====

The goal of this exercise is to begin to implement more complex programs and to become familiar with Python's Turtle package.  In particular, you will:
* Read data from a (csv) file
* Use a loop to process data
* Create graphical programs using Python's Turtle package
* Visualize the path and strength of hurricanes

There is both a pair and an individual component of this lab.  The individual component will be completed first.  You *may not start* the pair portion until both you and your partner have completed the individual component.  When you get to the pair portion, you must use *pair programming*.  Reemember that this means two people will work at the same computer, one driver and one navigator. The driver does the typing and using the mouse, while the navigator makes suggestions, points out errors, and helps guide the process.  You should switch roles every 15-30 minutes.

# Setting up your git repo for {{page.num}}

Create a joint git repo for you and your partner for {{page.num}}, following Step 2 in the [lab02](/lab/lab02/) writeup. Assuming that you have done the one time configurations related to your ETS account, clone your newly created private repo following the instructions in lab02.

You will complete the individual portion of your assignment in this pair repository.


# The individual portion: Getting familiar with the Turtle
To warm up with the Turtle, you will use the Turtle to draw your first initial (the first letter of your first name) on the screen.  
You should complete this part individually.  You may talk to your partner and have them help you, or give help to your partner, but you should try to do as much of it on your own as possible, and all the code you write should be done individually.  

## Step 1.1: Get familiar with the Turtle
In idle, create a new file and at the top of this file put a comment with your name and a description of what this file will do (a program to draw the first letter of your name).  Save this file as `lab03Warmup_YourName.py` where YourName is replaced with your first name.

In order to work with the Turtle, you need to import the `turtle` module.  Do this by putting the line:

```python
import turtle
```
at the top of your file, either before or after the comment you wrote.  This above line tells Python about the turtle library and allows you to call its functions. 

Next, let's write a simple function that uses the Turtle package to draw a shape.  Copy the following code into your file.

```python
def drawPicture(theTurtle):
    ''' Draw a simple picture using a turtle '''
    theTurtle.forward(100)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.left(90)
    theTurtle.forward(100)
    theTurtle.left(90)    

myTurtle = turtle.Turtle()  # Create a new Turtle object
drawPicture(myTurtle)   # make the new Turtle draw the shape
```

What happens when you run your file?

Modify the function in various ways to see what happens:
Change the number in the first `theTurtle.forward()` call in the drawPicture function. What's the role of the number?

Change the values in the calls to `theTurtle.left()`. What units are being used?

### What's the difference between `theTurtle`, `myTurtle` and `turtle`?
You might notice that there seem to be three names "turtle" in the code above.  What's going on?!  The Turtle library works a little differently than other libraries we've looked at so far, in that it uses a style of coding called "Object Oriented Programming".  You'll learn much more about objects in CSE 8A or CSE 11, but for now you can think of objects as complex types of data that also have built-in functions associated with them.   

So, `turtle` on the line
```python
myTurtle = turtle.Turtle()
```
is the name of the package, i.e. the built-in Python library where you will find all of the functions for the Turtle.  `myTurtle` and `theTurtle` are variable names.  They each store references to (the same) Turtle object.  Finally `Turtle()` is a special function that creates a new Turtle object.  

We can create more than one Turtle to work with at a time.  For example, try adding the following code to your warmup file:

```python
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle1.setpos(-50, -50)
turtle2.setpos(200, 100)
turtle1.forward(100)
turtle2.left(90)
turtle2.forward(100)
```

Can you explain what's happening?

### Python's "anonymous" Turtle
In the code above you noticed that by calling `Turtle()` three times we got three Turtles that we could control independently.  However, if you *know* you only want to use one Turtle, Python will provide an "anonymous Turtle" that you can control without actually creating explicitly.  So you might sometimes see lines of code that look like 

`turtle.forward(100)`

`turtle` is still the package name, and the `forward` call will control the first Turtle created.  Python will always create this first Turtle, even if you do not include any call to `Turtle()`.

### The turtle documentation

It's a good idea to check out the [library documentation](http://pydoc-zh.readthedocs.io/en/latest/library/turtle.html) (a.k.a. reference manual, API docs, etc.) when you're learning how to use a new library (set of methods).  Google can be very helpful when exploring a new tool. Here are a couple of links that can help you get started drawing pictures and seeing what's possible.

Here's the entry in the documentation for the function that lets us move forward:

****

```python
 turtle.forward(distance) turtle.fd(distance)
```

Parameters:	distance – a number (integer or float)
Move the turtle forward by the specified distance, in the direction the turtle is headed.

****


### Add and commit your code
Now is a good time to make sure you've got helpful comments in your file and that you've saved it.  Also add your file to your repository at this point (if you don't remember how, check the instructions in [lab02](/lab/lab02)) and then commit your code so far.  You do not need to push it to github yet, though you can if you want to.

## Step 1.2: Write a method to draw the first letter of your first name
Create a new file named `drawLetter_YourFirstName.py` in idle.  In that file, write the following method:

```python
drawA(theTurtle)
```

Note that the name of this method should correspond to the letter you are drawing.  So if my name is Chris, my function would be named `drawC`.  The parameter to this method `theTurtle` is the turtle you should use to draw the letter.  

Feel free to be creative here.  Right now, you can draw the letter any size, using any style.  You will probably find the functions `penup` and `pendown` useful, but check the documentation for other functions that will allow you to change the style of the lines your turtle draws.

### Test your function
Test your function to see if it works by creating at least *two* different Turtles, moving one of these Turtles away from its default position (you probably want to lift the pen before moving the Turtle), and then calling your `drawA` function with *each* Turtle.  Does the output look good?  Do both the Turtles draw?  If there are bugs in your code (we'd be surprised if there weren't!) fix them before moving on (though remember you can always add and commit non-working code to your repo with an appropriate comment).

### add, commit and push
At this point you are almost finished with the individual portion and ready to commit and push your code so far.  Here's a checklist to make sure you haven't forgotten anything:
1.  Do you have a comment at the top of your files? 	
2.  Do you have a draw function for your first initial?
3.  Does this function have one parameter: a turtle?
4.  Does this function have a reasonable docstring (recall from class what a docstring is)
5.  Did you test your function with at least two Turtles to make sure it's working correctly? (And is it?)
If so, you are ready to submit!

To submit, use the command line tools `git add`, `git commit` and `git push`. You must only push working versions of your code (though you can commit code in progress locally). Make sure your code is pushed to git by navigating to your repo on github.com and viewing your latest changes.

At this point you are done with the individual portion.  If your partner is not yet done DO NOT CONTINUE.  Here are some things you can do while you wait for your partner:
* Work on APS
* View and respond to the enrichment video
* Make your letter prettier/more interesting
* Make more functions to draw more letters


# The Pair Portion: Doing more with the Turtle

**STOP!  Do not start on this part of the lab until BOTH partners have completed the individual portion.  When you do start, make sure you use *pair programming* **

## Step 2.0: Discuss with your partner
Discuss the following questions with your partner, then put your joint answers into comments at the top of a new file named `lab3Letters_pair.py`. 

1. What is the "anonymous turtle"?
2. In the code below, what is the difference between `turtle` and `Turtle()`?
```python
myTurtle = turtle.Turtle()  
drawPicture(myTurtle)   
```
3. Imagine that I have a turtle in a variable named `myTurtle`.  What line of code will change that turtle's y-position to 100?


## Step 2.1: Extend your `drawA` function
Choose one of your `drawA` (or whatever letter you used) functions and copy it into your `lab03letters_pair.py` file.    Then, modify this function as follows:

1. Add another parameter to your `drawA` function:
```python
drawA(theTurtle, size)
```
`size` will determine the size of your letter.

2. Modify the code in the method so that it respects the size parameter.  You are free to use any interpretation of `size` that you wish, but your letter must be drawn in different sizes for different values of that parameter.  Make sure you modify the docstring for your modified function so that it accurately reflects what this new version of the function does.

Finally, test your new function to make sure that it respects the size parameter.  Fix any bugs you find, then add this file to your repository, commit and push.

### Step 2.2: Tracking Hurricanes!
**Switch driver and navigator if you have not yet done so**
Finally, we'll be using the 

We are going to be using the pre-written functions in the Turtle package to draw on the screen.  However, unlike other build-in functions (e.g. `len` or `print`) these functions work with a kind of data called an "object".  You'll learn much more about objects in CSE 8A or CSE 11, but for now you can think of objects as complex types of data that also have built-in functions associated with them. 

To work with a Turtle, we first need to ask Python to create a new Turtle object.  We can do this with the line:
```python
myTurtle = turtle.Turtle()
```
In this file, you will first need to import the 

Write a function that uses the Turtle to draw the first letter of your first name.  

What you'll be drawing
----------------------

You'll be drawing functions to produce your initials. For example, if your name is Pat Brady, and your pair partner is Chris Jimenez, your initials are PB and CJ.

In this case, the functions you'll write are:

-   drawP(theTurtle, width, height)
-   drawB(theTurtle, width, height)
-   drawC(theTurtle, width, height)
-   drawJ(theTurtle, width, height)

Then, you'll write two more functions:

-   drawInitialsPB(theTurtle, letterWidth, letterHeight, letterSpacing)
-   drawInitialsCJ(theTurtle, letterWidth, letterHeight, letterSpacing)

In the event that you are paired with someone that shares one or more initials with you (e.g. if Riley Jones and Chris Jimenez are partners, they share the letter J), you might have to write fewer functions. However, we'll avoid that, because we want you to get lots of practice. If you share one or more initials, please use your middle initials to get to four unique letters (and mention in your code comments what your middle name is in that case). So basically, combine the first, last and possibly middle initials (if needed), of yourself and your pair partner, to arrive at four unique letters.

You'll also write a function called go() that draws each members of the pair initials three times each, at different sizes.


Programming, Step-by-Step
=========================

You should be sitting WITH YOUR PAIR PARTNER to start this part of the assignment.

Follow these steps to complete the assignment

Step 0: Decide on initial driver/navigator
------------------------------------------

The initial driver will be the one that is typing on the computer.

-   If you are both sitting in front of computers, one of you please CLOSE YOUR COMPUTER NOW. You should both be sitting at the SAME COMPUTER.
-   If you are both logged in, the temptation to "not really do pair programming" will be too great, at least until you are used to the system.



Step 1: Try out the Turtle library
----------------------------------
The Python Turtle library lets you draw on a canvas, by moving around a little turtle. Simple commands make the turtle move and turn and it draws as it goes. 

But before you start with your own turtle, let's show you a simple example. Bring up IDLE. Create a new file called "turtletest.py" in your repo. To do this, in IDLE go to the menu option File-> New. Then continue with the following steps.

First add this code to import the turtle library:

```python
import turtle
```

This above line tells Python about the turtle library and allows you to call its functions. The function below does the actually drawing. Copy the following code into your file.

```python
def drawPicture():

	''' Draw a simple picture using a turtle '''

    turtle.forward(100)

    turtle.left(90)

    turtle.forward(100)

    turtle.left(90)

    turtle.forward(100)

    turtle.left(90)

    turtle.forward(100)

    turtle.left(90)    

drawPicture()
```

What happens when you run your file?

Modify the function in various ways to see what happens:
Change the number in the first `turtle.forward()` call in the drawPicture function. What's the role of the number?

Change the values in the calls to `turtle.left()`. What units are being used?


*Referring the turtle documentation*

It's a good idea to check out the [library documentation](http://pydoc-zh.readthedocs.io/en/latest/library/turtle.html) (a.k.a. reference manual, API docs, etc.) when you're learning how to use a new library (set of methods).  Google can be very helpful when exploring a new tool. Here are a couple of links that can help you get started drawing pictures and seeing what's possible.

Here's the entry in the documentation for the function that lets us move forward:

****

```python
 turtle.forward(distance) turtle.fd(distance)
```

Parameters:	distance – a number (integer or float)
Move the turtle forward by the specified distance, in the direction the turtle is headed.

****


Don't forget to save your work often and to add helpful comments to your code. And, of course, if you get stuck, ask for help.

Next, you'll use a turtle to draw your initials.


Step 2: PLAN your letters on paper
----------------------------------

Plan your drawing. For each letter that you and your pair partner are going to draw, start by drawing a bounding box like this on a piece of paper. Trade off: each of you should do the planning for the letters for your OWN name, with your pair partner watching and making helpful suggestions.

<img src="/images/labs/images/turtle/BoundingBox.png" title="BoundingBox.png" alt="BoundingBox.png" height="200" />

For example, for the name, Phill Conrad, I might plan out bounding boxes like these. Here, I've chosen each of the important points, and labelled them. Note, though, that these are only examples. I don't expect that everyone with a P or a C in their name will make the same choices about how to shape the letters. In fact, I hope each of you will make slightly different choices.

<img src="/images/labs/images/turtle/BoundingBoxP1.png" title="fig:BoundingBoxP1.png" alt="BoundingBoxP1.png" height="200" /> <img src="/images/labs/images/turtle/BoundingBoxC1.png" title="fig:BoundingBoxC1.png" alt="BoundingBoxC1.png" height="200" />

For instance, as an alternative, I might use bounding boxes like these:

<img src="/images/labs/images/turtle/BoundingBoxP2.png" title="fig:BoundingBoxP2.png" alt="BoundingBoxP2.png" height="200" /> <img src="/images/labs/images/turtle/BoundingBoxC2.png" title="fig:BoundingBoxC2.png" alt="BoundingBoxC2.png" height="200" />

Or even these, if I get ambitious, and want to try to make rounded shapes using the turtle's [circle](http://docs.python.org/3.3/library/turtle.html#turtle.circle) function (note: that's a link to the documentation!)

<img src="/images/labs/images/turtle/BoundingBoxP3.png" title="fig:BoundingBoxP3.png" alt="BoundingBoxP3.png" height="200" /> <img src="/images/labs/images/turtle/BoundingBoxC3.png" title="fig:BoundingBoxC3.png" alt="BoundingBoxC3.png" height="200" />

A warning about that last approach: although it may seem like it isn't that tough, there are some subtle traps. For example, in the C, what if we are drawing a short, fat C where height &gt; width? Then h-w will be negative, and there may be "issues". You might find that you would need more than one drawing, one for when (h-w)&gt;0, and a different approach when (h-w)&lt;0, and then use an if/else statement in your drawing code. It might be better to stick to approaches that don't involve interaction between height and width, which probably means straight lines. If you and your partner are up for the challenge of using curves and circles, you are welcome to try, but I advocate trying the straight line approach FIRST just to be safe.

Once you've planned your letters on paper, you are ready to start coding.


Step 3: Driver gets things started on first letter 
-----------------------------------------------------------------

Create a new file called "lab03.py" in your repo, and start creating a function definition for your first inital.

-   If the initial is A, the function should be called drawA. If it is a C, it should be called drawC, etc.
-   The function should take there parameters: the name of a turtle, a width, and a height.
-   Start the function with a docstring (a sandwich where the bread is three double quotes `"""` and the innards are a text comment indicating what the function does:

Example:

    def drawA(someTurtle, width, height):
       """
       draw the letter A using someTurtle, with some width and height
       """

      # Find my starting point
      xStart = someTurtle.xcor()
      yStart = someTurtle.ycor()

      # The rest is up to you to figure out

At the top of your file, add this comment (with your names), and the `import` `turtle` line, and save the file as lab03.py. (The function def for drawA or whatever your first initial is that you are trying to draw goes below that point, as shown:

    # lab03.py for Alice Baker and Chris Gaucho
    # Draw some initials using turtle graphics

    import turtle

    def drawA ... etc...

Now at the bottom of your file, make a go() function that you can type in at the Python prompt to make everything happen when you run your program, and outside that function (i.e. NOT indented), a line that creates a turtle. In my example, I called my Turtle fred, but may use any name you like:

That will look like this:

    fred = turtle.Turtle()
    def go():
         drawA(fred, 50, 100)



The advantage of declaring fred the turtle outside of the function definition is that your Turtle Graphics window will appear on the screen as soon as you hit F5 or select Run from the Run Module menu. That can make it easier to debug your code, because you can arrange your windows so that you can SEE the Turtle move when you type go().

Now save your file, and try running it. You should see a Turtle pop up, but unless/until you put more code in your drawA function, the turtle is going to just sit there.

Your next task: start adding code into your first initial drawing routine so that it draws an initial. My suggestion is to NOT wait until you have the whole thing done to test---instead, work with one or two points at a time, and one or two line segments at a time, and after each one is added, try to run and see if what you have so far is working.

As you code, put a comment before each step, that explains in English what you are doing. 


Step 4: Draw the remaining letters
----------------------------------

When your first initial looks good, its time to try the next one.

Suppose the second initial is B. Right under your function definition for drawA, but before your function definition for go, add a function definitions for drawB (or whatever your next initial is):

    def drawB(datTurtle, width, height):
       """
       draw the letter B using datTurtle, with some width and height
       """

      # Find my starting point
      xStart = datTurtle.xcor()
      yStart = datTurtle.ycor()

      # The rest is up to you to figure out

### A word about variable name choices

Note that the parameter name for the turtle in the function definition can be aTurtle, datTurtle, someOlTurtle, t, or really (just about) anything. It helps if the name is suggestive that it is the "role" of a turtle that is drawing our letter. But there is no python "rule" about what this name should be, other than:

-   it must be a legal variable name: starts with a letter or underscore, and consists of letters, digits and/ or underscores (see <http://www.w3resource.com/python/python-variable.php> )
-   can't be names already used for something else (e.g. `turtle` is no good, because its the name of the `turtle` module we are importing.

Same for width and height--you can call them w and h, or wd and ht, or xsize and ysize: whatever makes sense to you.

All that is required is that:

-   your letter drawing functions have exactly three parameters, that represent, in this order, the turtle, the width and the height
-   that the names be somewhat reasonable--a reasonable person should be able to guess what they are for from the names.

So calling them (pickle, tomato, cucumber) is not ok---you could make it work, but it is "bad style". 

But (turt, wid, hght) is fine, as is (t, w, h), or (aTurtle, width, height).

Step 5: Testing your first and second letters
----------------------------------------------

To test your first and second drawing function, add code into your go() function, like this:


    def go():
         fred = turtle.Turtle()
         drawA(fred, 50, 100)

         fred.forward(25)
         drawB(fred, 50, 100)

Or, you may even want to comment out the drawA call while you work on the B:


    def go():
         fred = turtle.Turtle()
         # drawA(fred, 50, 100)

         drawB(fred, 50, 100)

In any case, repeat this for all of the initials you need to draw.

AS YOU WORK, SWITCH DRIVER AND NAVIGATOR FREQUENTLY. Each member of the team should be the driver for the function for at least one their own initials.

Repeat the steps above until you have all your letters done, and switch driver/navigator between each function. Then you are ready for the combining steps.

Step 6: The step where you combine things
-----------------------------------------

In this step, you are going to write two new functions, for each of the initials of the members of the pair.

For example, for Phill Conrad, the function is :

    def drawPC(aTurtle, letterWidth, letterHeight, spacing):
       """
       draw the letters PC, using aTurtle, and the width and height given.  Use spacing * width as the space between letters.
       For example, if spacing is 0.5, then the space between the right edge of the P and the left edge of the C
       should be half of the average letter width.  If spacing is 1, it should be the same as the average letter width, and 
       if it is 2, it should be double the letter width.

       """

       # draw the P
      
       drawP(aTurtle, letterWidth, letterHeight)

       # do something here to space out the letters--you figure it out


       # draw the C

       drawC(aTurtle, letterWidth, letterHeight)

Your functions will look just like these, except that probably you'll have different letters. And you have to figure out the thing to do in between the letters (it's not that hard.)

Add them after your draw functions for each letter, but before your go() function.

AS YOU WORK, SWITCH DRIVER AND NAVIGATOR FREQUENTLY. Each member of the team should be the driver for the function for their own initials.

Then, modify your go() function so that it draws each member of your team's initials, at least three times each, with DIFFERENT widths, heights, and spacings. You'll need to pick up the pen between calls to drawXM() or drawPC() or drawJH() or whatever. And choose starting points (using t.goto(x,y)) so that all of the initials are on the screen, and none of them overlap.

When that's done, you are ready to do your finalcheck list on your code before submission, and then use the git command line to submit.

Step 7: Final Checklist
-----------------------

Here's your final checklist.

1.  Do you have a comment at the top of your file? 	
2.  Do you have a draw function for each of your initials?
3.  Does each of these functions have three parameters, a turtle, a width and a height?
4.  Does each of these have a reasonable docstring (see discussion in step 2.)
5.  Does each of your letter drawing functions have parameters names that are reasonable? (See pickle, tomato, cucumber discussion at step 5.)
6.  Does each of your letter drawing functions have comments throughout explaining the steps you are taking to draw, in plain English? (See discussion in Step 2, and the example code from lecture.)
7.  Does each letter drawing function assume that the turtle starts at lower left, pen down, pointing right, and leave the turtle at lower right, pointing right, pen down?
8.  Do you have a draw function for each pair of initials?
9.  Do your draw functions work for pairs of initials
10. Does each of your draw functions for pairs of initial have reasonable variables names, and good comments?
11. Does each of your draw functions have a reasonable docstring?
12. Is the spacing between letters handled correctly?
13. Do you have a go() function?
14. Does your go() function have a reasonable docstring?
15. Does your go() function call your initial functions, three times each, with different parameter values for width and height each time?
16. Do all the initials appear in each of the three appearances, not overlapping each other, and do they all appear on the screen?

If so, you are ready to submit!

NOTE: Only one member of each pair has to submit, but BOTH members of the pair are responsible to make sure the submit happens.

Step 7: Submit to github
-----------------------------

To submit, use the command line tools `git add`, `git commit` and `git push`. You must only push working versions of your code. Make sure your code is pushed to git by navigating to your repo on github.com and viewing your latest changes.

Congratulations on finishing lab 3!!! Hope you had fun with turtle graphics!


# Additional Fun with Turtle

When you are finished with the main part of lab03, here is an extension that you can start working on, and continue
to contribute to throughout SPIS.

You are invited to create a *public* github repo under the ucsd-cse-spis-2017 organization with this naming convention:

* `spis16-drawings-Name-Name`  (e.g. `spis16-drawings-Alex-Chris` )

In this repo, you can add files that provide drawing routines to draw whatever you like.

You can use the code from [https://github.com/ucsd-cse-spis-2017/spis16-lecture-0809](https://github.com/ucsd-cse-spis-2016/spis16-lecture-0809) as a model.

Then, try looking at the code from some of your fellow classmates public `spis16-drawings...` repos.

See if you can copy some of their files into your repo (add a comment indicating where the code came from,
e.g.

```python
# This file copied from spis16-drawings-Alex-Chris
```

Then try using `import` to get access to those functions, and use them in your own drawings.

See how creative you can get in terms of combining different drawings together from many other fellow SPISers.

Put the code for these additional "mash-ups" in the same `spis16-drawings-Name-Name` repo, just perhaps in a different python file, e.g. `mashups.py`.

