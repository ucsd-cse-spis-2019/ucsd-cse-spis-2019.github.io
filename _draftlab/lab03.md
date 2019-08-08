---
layout: lab
num: lab03
ready: true
desc: "More functions and drawing with Turtle Graphics"
assigned: 2019-08-12 12:00:00.00-7
due: 2019-08-15 17:00:00.00-7
---

If you find typos or problems with the lab instructions, please report them on [Piazza]({{site.piazza}})


Goal
====

The goal of this exercise is to begin to implement more complex programs and to become familiar with Python's Turtle package.  In particular, you will:
* Read data from a (csv) file
* Use a loop to process data
* Create graphical programs using Python's Turtle package
* Visualize the path and strength of hurricanes

There is both a pair and an individual component of this lab.  The individual component will be completed first.  You *may not start* the pair portion until both you and your partner have completed the individual component.  When you get to the pair portion, you must use *pair programming*.  Remember that this means two people will work at the same computer, one driver and one navigator. The driver does the typing and using the mouse, while the navigator makes suggestions, points out errors, and helps guide the process.  You should switch roles every 15-30 minutes.

# Setting up your git repo for {{page.num}} (WITH your partner)

You will create one repository for this assignment between the two of you, but you will need to import some starter code.  Create a joint git repo for you and your partner for {{page.num}}. However, create a completely empty repository with no Readme, no .gitignore, and no license named `spis19-lab03-name1-name2`.  

After you create the new repository, you will see a new screen with the option to import code from another repository.  You should import the code from this repository:

```
https://github.com/ucsd-cse-spis-2019/lab03starter.git
```

It will take a few minutes, but when you return to the repo on github you should see some starter code.

Finally, clone your newly created private repo following the instructions in [lab02](/lab/lab02/).

Next, you will complete the individual portion of your assignment, adding your files to this shared repo.

# The individual portion: Getting familiar with the Turtle
To warm up with the Turtle, you will use the Turtle to draw your first initial (the first letter of your first name) on the screen.  
You should complete this part individually.  You may talk to your partner and have them help you, or give help to your partner, but you should try to do as much of it on your own as possible, and all the code you write should be done individually.  

## Step 1.1: Get familiar with the Turtle
In gVim, create a new file and at the top of this file put a comment with your name and a description of what this file will do (a program to draw the first letter of your name).  Save this file as `lab03Warmup_YourName.py` where YourName is replaced with your first name.

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

It's a good idea to check out the [library documentation](https://docs.python.org/3/library/turtle.html) (a.k.a. reference manual, API docs, etc.) when you're learning how to use a new library (set of methods).  

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
Create a new file named `drawLetter_YourFirstName.py` in gVim.  In that file, write the following method:

```python
drawA(theTurtle)
```

Note that the name of this method should correspond to the letter you are drawing.  So if my name is Chris, my function would be named `drawC`.  The parameter to this method `theTurtle` is the turtle you should use to draw the letter.  

Feel free to be creative here.  Right now, you can draw the letter any size, using any style.  You will probably find the functions `penup` and `pendown` useful, but check the documentation for other functions that will allow you to change the style of the lines your turtle draws.

### Test your function
Test your function to see if it works by creating at least *two* different Turtles, moving one of these Turtles away from its default position (you probably want to lift the pen before moving the Turtle), and then calling your `drawA` function with *each* Turtle.  You should see two letters drawn, one drawn by each Turtle (one after the other).  Does the output look good?  Do both the Turtles draw?  If there are bugs in your code (we'd be surprised if there weren't!) fix them before moving on (though remember you can always add and commit non-working code to your repo with an appropriate comment).

### add, commit and push
At this point you are almost finished with the individual portion and ready to commit and push your code so far.  Here's a checklist to make sure you haven't forgotten anything:
1.  Do you have a comment at the top of your files? 	
2.  Do you have a draw function for your first initial?
3.  Does this function have one parameter: a turtle?
4.  Does this function have a reasonable docstring (recall from class what a docstring is)
5.  Did you test your function with at least two Turtles to make sure it's working correctly? (And is it?)
If so, you are ready to submit!

To submit, use the command line tools `git add`, `git commit` and `git push`. You must only push working versions of your code (though you can commit code in progress locally). Make sure your code is pushed to git by navigating to your repo on github.com and viewing your latest changes.

### What happens if it won't let you push?
You might get a message at this point telling you that your push failed.  This will happen if your partner has pushed before you.  Now you need to incorporate their changes to the central repository into your local version of the repository before github will allow you to push.  To do this you will need to execute a `pull` command:

`git pull origin master`

Then you will be able to push and everything should be OK.  Since you and your partner have been editing different files, you should not have any merge conflicts, but if you do, stop and ask a mentor for help.

See the documentation on [this page](https://help.github.com/articles/dealing-with-non-fast-forward-errors/) for a bit more information.

At this point you are done with the individual portion.  If your partner is not yet done DO NOT CONTINUE.  Here are some things you can do while you wait for your partner:
* Work on APS
* View and respond to the enrichment video
* Make your letter prettier/more interesting
* Make more functions to draw more letters


# The Pair Portion: Doing more with the Turtle

**STOP!  Do not start on this part of the lab until BOTH partners have completed the individual portion.  When you do start, make sure you use _pair programming_**

**WARNING: Throughout this section make sure that you always start with an updated version of the repository (use `git pull` as described above to pull the latest version into your account).  If you ever switch to working on the other partner's lab account make sure you do `git add`, `git commit`, `git push` before you switch, and then `git pull` when you switch to the new account.  If you make changes to the same file in the same repo from two different clones, you are likely to get merge conflicts, which are no fun to deal with.**

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

## Step 2.2: Tracking Hurricanes!
**Switch driver and navigator if you have not yet done so**

This part of the assignment is based on the following assignment: http://nifty.stanford.edu/2018/ventura-hurricane-tracker/irma-assignment.html (http://nifty.stanford.edu/2018/ventura-hurricane-tracker/irma-assignment.html)

In this part, you and your partner will use the Turtle to animate the paths of some real hurricanes!  Your goal is to build a program that functions like the one in [this video](https://youtu.be/c2uRG42M_nc).  Here are the details.

### Understand the starter code
Open the starter file `irma.py` in gVim.  

In the `irma_setup` function, the following are done for you:

* Creating the screen and turtle
* The turtle's shape is changed to that of a hurricane
* Loading a background image of the Atlantic
* Setting the world coordinates of the screen to match the latitude and longitude on the map

You will add your code into the function `irma()`.  Read the comments and the code in that function and make sure you understand what it does so far.  Try moving the turtle (t) around and see it animate.  Notice the coordinates of the world have been changed from their default.  The x values in the new coordinate system range from -90 to -17.66 and the y values range from 0 to 45.  Since the Turtle starts at (0,0) you cannot see it.  Try moving it to a location where you can see it in the new coordinate frame and making it move.

You will also notice that this starter code uses a file named `irma.csv` in the data directory. This data was scraped from https://www.wunderground.com/hurricane/atlantic/2017/hurricane-irma (https://www.wunderground.com/hurricane/atlantic/2017/hurricane-irma),
last access 9/14/2017. This file contains data about hurricane Irma. Each line contains 6 columns separated by commas (thus the .csv file extension). The file can be opened directly in idle or opened in Excel for a columnar view. The first line of the file describes what each column is. Here are the first 3 lines of the file, separated into their columns:

    Date	    Time        Lat     Lon     Wind    Pressure
    30-Aug      15:00 GMT   16.4    -30.3   50      1004
    30-Aug      21:00 GMT   16.4    -31.2   60      1001

The only columns relevant to your code are Lat (the latitude), Lon (the longitude), and Wind (the wind speed in miles per hour).

### Add code to make the Turtle trace the hurricane's path
Using the data in `irma.csv`, your irma function must show hurricane Irma's path. Your solution should look like [the video](https://youtu.be/c2uRG42M_nc) and must include the following:

* Correctly show each point in the data file (together with lines between each point)
* At each point, you must display what category the storm is, if it has hurricane strength winds, otherwise, draw no text.
* Color code the hurricane strength:
  * Red for Category 5
  * Orange for Category 4
  * Yellow for Category 3
  * Green for Category 2
  * Blue for Category 1
  * White if not hurricane strength
* The thickness of the line should change in proportion to the hurricane category.

You can use Google to find the wind speeds for each category of hurricane.

Notice that the starter code already uses the csv package to read the lines from the data file.  The csv package is already imported at the top of the irma.py file, and we've provided some comments and code to help you understand how you can read the lines and get the data out of the lines in the file.  Make sure you understand how this works before you attempt to change the code.  If you have questions, ask a mentor.

**We have provided some comments in the starter code to help you out, but this is a more open-ended task than you've
done in the past.  Make a plan with your partner before you attempt to start coding**

### Run, test and debug your code
Make sure you run your code, and look at the data, to test your code.  

**Ensure the following:**
* Does your line start in the same position as the demo?  Remember, you need to move the turtle to the starting latitude/longitude with the pen UP so you don't draw a line that's not part of the hurricane data.
* Do the number and order of 1s, 2s, 3s, etc, on your path as well as the color of the points in your path, match the demo?
* Does the path go in the same direction as in the demo?
* When you run your code on other data files, do you get the path you'd expect (after looking at the data)?

## Submit everything!
Once you've got your hurricane tracker working, make sure of the following:
* Do you have your names and a comment at the top of each file?
* Do you have docstrings for each function you wrote?
* Did you use meaninful variable names?
* Did you use appropriate commenting in your code when something might be unclear to the reader?

Once you can answer yes to all of the following make sure you add ALL of your files from this lab (the two files from the individual part (4 between the two of you) and the two files you created for the pair part) to your repo, then commit and push to github.  Then you are done!   But of course, you're never done, so keep working on creative extensions of your own!
