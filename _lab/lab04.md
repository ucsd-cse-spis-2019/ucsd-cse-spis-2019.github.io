---
layout: lab
num: lab04
ready: false
desc: "Recursion with turtle and intro to the Python Imaging Library, by Diba"
assigned: 2016-08-10 09:30:00.00-7
due: 2016-08-12 15:45:00.00-7
---

If you find typos or problems with the lab instructions, please report them on Piazza


# Learning Goals
In this lab you will practice some of the key concepts from Chapter 4 of Guttag.
This includes writing parameterized functions, developing test code and solving problems using recursion. You'll do some warm up recursive programs, predict and test what they do, and then top it all off by creating some very cool fractal art. Your learning goals are:

* Determine the base case and recursive step in a recursive solution.
* Implement this recursive solution in Python.
* Learn to reason about your program, and justify its correctness.
* Find and fix errors in simple Python functions.
* Trace the value of variables in Python code.
* Reason about the quality and completeness of test cases.
* Use geometry and turtle graphics to draw fractals in Python.

# Work Flow

* Step 1: Read Chapter 4 of Guttag

* Step 2: Create a new github repo under the "ucsd-cse-spis-2016" organization. Your github repo should be called spis16-lab04-Name1_Name2 (where Name1 and Name2 are the first names of the pair partners). Get the starer code from the repo lab04-startercode. If you don't recall how to do this, refer to the [instructions on using git to complete the labs](/topics/github/)

* Step 3: For each of the programming exercises in this lab come up with a solution outline by discussing with your partner. Don't be in a hurry to start coding unless you have a fairly clear idea of a solution strategy.

* Step 4: Unit test your code as you write new code using the pytest framework

* Step 5: Commit and push your code to github frequently. Once you feel you have sufficiently tested your code, additionally submit it to gradescope (remember you can submit multiple times). Only select exercises need to be submitted to gradescope. Refer to this link for instructions on how to submit your code to git and gradescope: TO DO: Add link

Developing code is an iterative process. Your code will probably not work as expected on the very first try. Don't be dismayed. Work through your code to identify bugs, test new code frequently and seek help if you feel you are stuck!

# Programming Exercises
Let's begin with our very first exercise which is a warmup on recursion.

## Multiply without the '*' operator 
We're going to write a recursive function that multiplies two integers without using the * (times) operator, only + (addition). Your program should work for positive, and negative values of 'a' and 'b'. For now, let's consider the case where 'b' takes only  non-negative values and 'a' may be positive, negative or zero. Recognize that:


a * b = a + a + a + ... + a (with b copies of a added together)

E.g., 

3 * 4 = 3 + 3 + 3 + 3

In other words, we want to define a function recProduct(a, b) which will have integers as arguments and will return the product of its arguments.  But, the function won't use the operation *.

Just for practice, take a minute to (a) determine the base case and (b) write the recursive step without looking below.  After you've got it, read on. If you don't know where to ask, please ask for help.

Your base case probably looks something like:

a * 0 = 0

That is, when b is 0, then the product of 0 times any number is 0.

Your recursive step should be something like:

a * b = a + a * (b-1)

Now, implement these steps in your code. Once you have that, its time to test you code. Using the pytest framework, unit test your code for some typical inputs.

For example check that your program does the following:

`recProduct(0,5)` returns 0

<code> recProduct(1,5) </code> returns 5
 
<code> recProduct(-1,5) </code> returns -5
 
<code> recProduct(5,-1) </code> returns -5

If any of your test cases fail, it means either there is an error in your code or your code doesn't cover that particular case and you need to write additional code. You have to re-examine your code and figure out what is wrong.
This process is known as debugging. If you are not sure how to debug your code, refer to this link to begin debugging your code in a systematic way. TO DO: Link to debugging tips

Once you have sufficiently tested your code submit it via gradescope. Remember you can do this as many times as you like prior to the deadline. Refer to the submission guidelines here. TO DO: Link to instructions on submitting code via gradescope.

## Recursive Rendering
It is time for you to start showing off your skills visually. You will do this by writing programs to create cool fractal art, which is based on internal self-similarity. 

We'll start by creating two classical fractals: a spiral and a tree. Afterward, try your hand at creating snowflakes, too, or any fractals beyond the problems below!
We've included suggestions for extensions on the Challenge page. TO DO: Link to challenge page

*The Python Turtle Library*

To draw pictures in Python, we can use the Python Turtle Library (For more information on the turtle library refer to the [documentation on the turtle library](http://pydoc-zh.readthedocs.io/en/latest/library/turtle.html)). The functions in this library emulate a robotic turtle which draws as it moves. We can also specify colors and all kinds of other cool attributes. You've already started playing with this library in the Python exercises from the previous labs. Today, you'll draw your own pictures and write code from scratch.

But let's start simple. We will draw a square. In Recursion.py, you will see the following code:

```import turtle
```

This first line above tells Python about the turtle library and allows you to call its functions. The function below does the actually drawing.

```
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

```

What happens when you run the above function?

Modify the function(s) in various ways to see what happens:
Change the number in the first `turtle.forward()` call in the drawPicture function. What's the role of the number?

Change the values in the calls to `turtle.left()`. What units are being used?

Play around with the `drawPicture()` function to get comfortable with the Turtle Library. Can you draw a rectangle? How about a smiley face? See if you can draw an equilateral triangle. The equilateral triangle if the first step to drawing the Koch snow flake, which is the apex of this lab.


Add each of your new functions to the Recursion.py file, making sure to comment your code and include descriptive and concise docstrings.

*Referring the turtle documentation*

It's a good idea to check out the [library documentation](http://pydoc-zh.readthedocs.io/en/latest/library/turtle.html) (a.k.a. reference manual, API docs, etc.) when you're learning how to use a new library (set of methods).  Google can be very helpful when exploring a new tool. Here are a couple of links that can help you get started drawing pictures and seeing what's possible.

Here's the entry in the documentation for the function that lets us move forward:

****

```
 turtle.forward(distance) turtle.fd(distance)
```

Parameters:	distance – a number (integer or float)
Move the turtle forward by the specified distance, in the direction the turtle is headed.

****

If you and your partner get stuck, look back at the examples we worked through together in class and try to adapt the strategies.  If you're still stuck, ask for help.

Don't forget to save your work often and to add helpful comments to your code.

## Draw a Spiral
The spiral function has the following signature:

```
 spiral(initialLength, angle, multiplier)
```

The function takes as arguments
an initialLength of the spiral's first line segment,
an angle specifying the degree of the angle formed by neighboring segments, and
a multiplier indicating how each segment changes in size from the previous one.
For example, the following are example screenshots from the call spiral(100, 90, 0.9) and spiral(1, -45, 1.1), respectively:


<p align="center">

![alt-Spiral-1](/lab/images/spiral1.gif){:height="200px" width="200px"} ![alt-Spiral-2](/lab/images/spiral2.gif){:height="200px" width="200px"}

</p>

	
Notice that the angle is specified in degrees.

In the first call the fractal starts from the center with initialLength 100 pixels. It turns right by 90 degrees when it needs to draw a successive segment whose length is 0.9 times that of the previous one. In the second one, the fractal starts from the center with initialLength 1 pixel. Each iteration the line turns left by 45 degree and draw a segment whose length is 1.1 times longer.

Note the spiral function can be computed inside-out, or outside-in, depending on the multiplier, therefore the base case varies. The spiral should stop drawing when it has reached a side lengh of less than 1 pixel (if multiplier<1) or greater than 200 pixels (if multiplier>1).

Implement the function and use it to draw an interesting spiral of your own.  

Help!  Stack Overflow!  Do not be alarmed if you find you are getting stack overflow errors when you try to run the "growing spiral" example above.  This error is caused by an infinite recursion.  I.e. a recursion that never hits its base case.  Not sure why?  This is a perfect time to practice some of those debugging skills you learned above.  :)  Ask a tutor if you need help.

## Grow a Tree

Next, you will write the tree function.  It has the following signature:
 
```
 tree(trunkLength, height)
```
The function takes as arguments:
a trunkLength which is the length of the main trunk of the tree, and
the height indicating the number of levels of branching of the tree.
For example, the following is an example screenshot from the call to tree(200, 4):

<p align="center">
![Tree](/lab/images/tree.gif){:height="200px" width="200px"} 
</p>

The tree "grows" from the ground of the world, with initial length of the first trunk 200 pixels. At the end of the first segment, the trunk forks into two directions. The forked trunk in each direction has a shorter length and continues to fork at the end, until the tree has forked 4 times.

Think about the base case and its recursive steps before implementing the function. 

Your tree will be personalized by the aesthetic choices you make about
the number of branches at each fork (anything greater than 1 is OK), 
the exact angle of branching, 
the reduction of trunkLength in sub-branches.
Your tree is planted on the ground and should grow upward. 

Draw some interesting trees using your function.


## Create Snowflakes ... in San Diego!

By now you should be very skilled at creating fractals using recursions. Congratulations! Now you can do much more, even making it snow during summer in sunny San Diego! In this exercise you will create the following snowflake structure (a.k.a. Koch Snowflake).

<p align="center">
![](/lab/images/Von_Koch_curve.gif)
</p>

As the animation shows, the Koch snowflake begins with an equilateral triangle; at each stage, the middle third of each line segment is replaced by a pair of line segments that can, together with the replaced segment, form an equilateral triangle; then the replacement will be performed again on all the component line segments of the newly created shape, over and over.

We will draw the Koch Snowflake by first defining the snowflake function with the following signature:

```
snowflake(sideLength, levels)
```

which takes as arguments:
a sideLength of the initial equilateral triangle, and
the levels indicating the number of recursive levels performed to create the final snowflake.
Observe that the base case is simply an equilateral triangle with side length equal to sideLength. Each increment of level replaces the middle third of all of the snowflake's sides with a "bump" that is, itself, a smaller equilateral triangle.

Hint: It might be useful to write helper function named

```
snowflakeSide(sideLength, levels)
```

that draws just one side of the underlying equilateral triangle -- along with all of its squiggles or bumps, recursively! 

All of the recursion will then be in snowflakeSide. So, first try creating snowflakeSide and make sure that it works and draws a single side of the snowflake curve at the appropriate level of recursion. Once snowflakeSide works, then your snowflake function will call snowflakeSide four times, with appropriate angles between them.

Again, in this strategy, all of the recursion occurs in snowflakeSide. Remember that 
if levels is zero, then snowflakeSide should produce a single line segment (this will be the base case of the recursion);
otherwise, snowflakeSide needs to call itself four times; and, 
keep in mind that you're only creating one of the three sides of the snowflake!
Here are images of four steps (after three levels of recursions) of the overall Koch curve's progression:

<p align="center">
![](/lab/images/360px-KochFlake.gif)
</p>

Test your implementation by calling snowflake(280, 4); you should get the following snowflake:

<p align="center">
![](/lab/images/Koch_280_4.gif)
</p>



Thinking about the snowflake

What's the perimeter of the Koch snowflake?

If levels == 0, then the distance is just sideLength.  Why?

What about for higher levels?  For simplicity, let's assume that sideLength == 1.  We can define the sequence of numbers

L_n = distance around edge snowflake(1, n) is called.

Can you compute the first few values of L_n by hand?

You might notice a pattern emerging ....  Can you express that pattern using an algebraic formula?


It turns out that, for all natural numbers n, 

L_(n+1) = (4/3) * L_n .

Modify your implementation of snowflake(sideLength, levels) so that the function returns the length of the line being drawn Run snowflake(1, n) for some small values of n to confirm the equation above.

How does this quantity change as n gets very very large?  What does that say about this shape for very, very large n?

## Part 2: Introduction to the Python Imaging Library (PIL)

Turtle is a great drawing tool but when it comes to manipulating existing image files, python's imaging library is the module. 

But what is a image file and how is it different other types of data?

Our computers encode all data (pictures, games, files) as sequences of 0s and 1s.  They are just a digital kingdom of bits! Some of the text below is review, but be sure to read it over (quickly) anyway.

In your computer, images (pictures) are files stored on your hard disk. An digital image is logically a rectangular grid of pixels, which appear as squares when enlarged; each pixel then typically consists of 1 byte (8 bits) for a Black-and-White image or 3 bytes (24 bits) for a color image, where one byte (a value between 0 and 255) each is for Red (R), Green (G), and Blue (B). R, G, B are three ingredients for all visible colors; for example: blue is 0 redness + 0 greenness + 255 blueness, white is 255 redness + 255 greenness + 255 blueness, and brown is 165 redness + 42 greenness + 42 blueness, etc.. The following figure by Wikipedia shows a color image with enlarged pixels.

![](/lab/images/Pixel-example.gif)

In this lab we'll work with the Python Imaging Library (PIL) which is a graphics library like turle designed for working with image files. So let's warm up!

## Getting familiar with PIL

Download the  "stone bear" picture below and save it in your github repo working directory. You can do this by right clicking on the image and selecting the option to save. Be sure to save the image as "stoneteddybear.jpg".

![](/lab/images/stoneteddybear.jpg)


Next, launch IDLE in the same directory that you stored the stone bear image.

Before we can manipulate a picture in PIL, we will need to tell Python and PIL where to find it.  To do this, you will need to specify the exact path to the picture on your computer.  You also need to tell Python about the PIL Image library.  We'll start by playing around with the teddy bear image in the shell.  In the shell, type the following to load the Image library into the shell (later you'll put this line at the top of your file).  

```
>>> from PIL import Image

```

Then, you can open the picture you just downloaded as an image as follows:

```
>>> stonebear = Image.open( "stoneteddybear.jpg" )

```

The argument to the open function tells Python where to find the image. If you are getting an error here it's probably because of a typo in your filename, or because you either placed the file in the wrong place or launched IDLE from a directory different from where the image was stored. 

To ensure that the command you just executed works you can show the image you just created:

```
>>> stonebear.show()
```

Logically, an image is a grid of pixels. The size of the "stone bear" picture is 600 x 800, i.e., 480,000 pixels. You can pick a specific pixel from the image by using the `getpixel()` function. The arguments of this function are a picture object and the pixel's X position and its Y position; the function returns the pixel object at the coordinate(X, Y) of the image. Note that in the image grid, the axis is a little different from the usual 2D Cartesian axis, in that it counts from upper left to bottom right. For example, in the following 18 x 18 image grid, the coordinate (11, 7) is the grey block. Note the index starts at 0.

![](/lab/images/coordinates.gif)

So, if you call

```
>>> pixel = stonebear.getpixel( ( 100, 200) )

```

The pixel returned is a tuple representing the RGB values of the pixel on the 200th row from top, 100th column from left, in the stonebear image. You can see this by looking at the value stored in pixel.

```
>>> pixel
(166, 201, 239)
```

Now, let's see how to modify the colors of individual pixels in the image.  We'll be using the ImageDraw library to modify the image.  First, tell Python about the ImageDraw library as follows:

```
>>> from PIL import ImageDraw

```

Now you can create a Draw object that will act on the stonebear image as follows:

```
>>> beardraw = ImageDraw.Draw( stonebear )

```

You can now use all of the ImageDraw functions to modify the stonebear image. For more information refer to the [documentation on ImageDraw](http://pillow.readthedocs.io/en/latest/reference/ImageDraw.html). Most of your work in this lab involves modifying the colors of individual pixels, so the function we will use is the `point()` function.  Here's an example of how it works.  Try it in the shell:

```
>>> beardraw.point( [(100, 200)], (0, 0, 0) )
```

The point function takes two arguments: 

* a list of pixel coordinates each represented by an (x, y) tuple.  In the example below our first argument is: [ (100, 200) ], which is a list of a single pixel. Typically using this function, you will be modifying one pixel at a time.

* a tuple representing the RGB color to set the pixel to.  In the example above, this color is (0, 0, 0), i.e. black.

After running the command above, show the bear image again and see if you can find the modified pixel.  It's there!

If you have a hard time seeing the modified pixel, try the following code to turn a range of pixels black.

```
for i in range(100):
    beardraw.point( [(i, 200)] , (0, 0, 0) )

```






