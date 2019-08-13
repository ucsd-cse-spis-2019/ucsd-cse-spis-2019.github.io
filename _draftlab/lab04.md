---
layout: lab
num: lab04
ready: true
desc: "Recursion and fractals with Turtle"
assigned: 2019-08-13 09:00:00.00-7
due: 2019-08-20 17:00:00.00-7
---

If you find typos or problems with the lab instructions, please report them on Piazza.


# Learning Goals

This includes writing parameterized functions, developing test code and solving problems using recursion. You'll do some warm up recursive programs, predict and test what they do, and then top it all off by creating some very cool fractal art. 

Your learning goals are:

* Determine the base case and recursive step in a recursive solution.
* Implement this recursive solution in Python.
* Learn to reason about your program, and justify its correctness.
* Find and fix errors in simple Python functions.
* Trace the value of variables in Python code.
* Reason about the quality and completeness of test cases.
* Use geometry and turtle graphics to draw fractals in Python.


# Work Flow

For each of the programming exercises in this lab come up with a solution outline by discussing with your partner. Don't be in a hurry to start coding unless you have a fairly clear idea of a solution strategy. Only when you have come up with a clear strategy, start the coding process. Test your code constantly, maybe starting with simple cases first. Make sure to commit your code frequently. Push working versions of your code to github. 

Developing code is an iterative process. Your code will probably not work as expected on the very first try. Don't be dismayed. Work through your code to identify bugs, test new code frequently and seek help if you feel you are stuck!


# Setting up your repo
Create a new shared repo for this lab assignment as you did in lab02. There is no starter code this time. The name of your repo should be `spis19-`<tt>{{page.num}}</tt>`-Name1-Name2` where the `Name1-Name2` part matches the *Pair Name* column of the [Pairs table from the SPIS FOCS Website](http://ucsd-cse-spis-2019.github.io/info/pairs/), as we have done for the previous labs.


# Programming Exercises
Let's begin with our very first exercise which is a warmup on recursion.

## Multiply without the '*' operator 
We're going to write a recursive function that multiplies two integers without using the * (multiply) operator, only + (addition). Your program should work for positive, and negative values of 'a' and 'b'. For now, let's consider the case where 'b' takes only  non-negative values and 'a' may be positive, negative or zero. Recognize that:


a * b = a + a + a + ... + a (with b copies of a added together)

E.g., 

3 * 4 = 3 + 3 + 3 + 3

In other words, we want to define a function recProduct(a, b) which will have integers as arguments and will return the product of its arguments.  **But, the function shouldn't use the operation *.**

Just for practice, take a minute to (a) determine the base case and (b) write the recursive step without looking below.  After you've got it, read on. If you don't know where to start, please ask for help. Scroll down when you have an answer.


<div style="margin-bottom:32em">
</div>


Your base case probably looks something like:

a * 0 = 0

That is, when b is 0, then the product of 0 times any number is 0.

Your recursive step should be something like:

a * b = a + a * (b-1)

Bring up gVim, and create a new file "recursiveProd.py". Your task is to complete the function below, which implements recursive multiplication.

```python
def recProd(a,b):
	'''Calculate product a*b recursively'''
	
```

When you are done, test your code. For example check that your program does the following:

`recProduct(0,5)` returns 0

`recProduct(1,5)` returns 5
 
`recProduct(-1,5)` returns -5
 

If any of your test cases fail, it means either there is an error in your code or your code doesn't cover that particular case and you need to write additional code. You have to re-examine your code and figure out what is wrong.
This process is known as debugging.

Once you have tested your code for the cases where the parameter `b` is non-negative, while `a` is any integer that maybe positive, negative or zero, test a few additional cases where the parameters `b` is negative. Here are a few example cases:

`recProduct(5,-1)` should return -5

`recProduct(-5,-1)` should return 5

If your code passes these cases, great! If not implement the logic needed to handle the case where `b` is negative. After you are done, consider refractoring your code to arrive at an elegant and concise solution.


## Recursive Rendering
It is time for you to start showing off your skills visually. You will do this by writing programs to create cool fractal art, which is based on internal self-similarity. 

We'll start by creating two classical fractals: a spiral and a tree. AThen you get to try your hand at creating snowflakes.


*The Python Turtle Library*

You've already started playing with Python's Turtle library in the previous lab. For more information on the turtle library refer to the [documentation on the turtle library](http://pydoc-zh.readthedocs.io/en/latest/library/turtle.html).

In your git repo create a file called "recursiveDrawings.py" and put all your upcoming code in that file. Remember, to be able to use our turtle, we need to import the turtle library:

```python
import turtle
```


## Draw a Spiral
In the file "recursiveDrawings.py" create the spiral function which has the following signature. 

```python
 spiral(initialLength, angle, multiplier)
```

The function takes as arguments
an initialLength of the spiral's first line segment,
an angle specifying the degree of the angle formed by neighboring segments, and
a multiplier indicating how each segment changes in size from the previous one.
For example, the following are example screenshots from the call spiral(100, 90, 0.9) and spiral(1, -45, 1.1), respectively:


<p align="center">

![alt-Spiral-1](/images/labs/images/spiral1.gif){:height="200px" width="200px"} ![alt-Spiral-2](/images/labs/images/spiral2.gif){:height="200px" width="200px"}

</p>

	
Notice that the angle is specified in degrees.

In the first call the fractal starts from the center with initialLength 100 pixels. It turns right by 90 degrees when it needs to draw a successive segment whose length is 0.9 times that of the previous one. In the second one, the fractal starts from the center with initialLength 1 pixel. Each iteration the line turns left by 45 degree and draw a segment whose length is 1.1 times longer.

Note the spiral function can be computed inside-out, or outside-in, depending on the multiplier, therefore the base case varies. The spiral should stop drawing when it has reached a side lengh of less than 1 pixel (if multiplier<1) or greater than 200 pixels (if multiplier>1).

Implement the function and use it to draw an interesting spiral of your own.  

Help!  Stack Overflow!  Do not be alarmed if you find you are getting stack overflow errors when you try to run the "growing spiral" example above.  This error is caused by an infinite recursion.  I.e. a recursion that never hits its base case.  Not sure why?  This is a perfect time to practice some of those debugging skills you learned above.  :)  Ask a tutor if you need help.

Useful debugging hint: You can change the speed with which your turtle draws. Assuming your turtle is `bob`, adding the code below causes it to move as slow as possible, which can help you figure out what is going on in your algorithm. If you change '1' to higher numbers, your turtle will speed up. However, somewhat counter-intuitively, `speed(0)` has the turtle move as fast as possible, which is useful when your algorithm is working and you want to try it out with a larger recursion depth. 

```python
bob.speed(1)
```


## Grow a Tree

Next, you will write the tree function.  It has the following signature:
 
```python
 tree(trunkLength, height)
```
The function takes as arguments:
a trunkLength which is the length of the main trunk of the tree, and
the height indicating the number of levels of branching of the tree.
For example, the following is an example screenshot from the call to tree(200, 4):

<p align="center">
![Tree](/images/labs/images/tree.gif){:height="200px" width="200px"} 
</p>

The tree "grows" from the ground of the world, with initial length of the first trunk 200 pixels. At the end of the first segment, the trunk forks into two directions. The forked trunk in each direction has a shorter length and continues to fork at the end, until the tree has forked 4 times.

Think about the base case and its recursive steps before implementing the function. 

Your tree will be personalized by the aesthetic choices you make about
the number of branches at each fork (anything greater than 1 is OK), 
the exact angle of branching, 
the reduction of trunkLength in sub-branches.
Your tree is planted on the ground and should grow upward. 

Draw some interesting trees using your function.


## Create Snowflakes

By now you should be very skilled at creating fractals using recursions. Congratulations! Now you can do much more, even making it snow during summer in sunny San Diego. In this exercise you will create the following snowflake structure (a.k.a. Koch Snowflake).

<p align="center">
![](/images/labs/images/Von_Koch_curve.gif)
</p>

As the animation shows, the Koch snowflake begins with an equilateral triangle; at each stage, the middle third of each line segment is replaced by a pair of line segments that can, together with the replaced segment, form an equilateral triangle; then the replacement will be performed again on all the component line segments of the newly created shape, over and over.

We will draw the Koch Snowflake by first defining the snowflake function with the following signature:

```python
snowflake(sideLength, levels)
```

which takes as arguments:
a sideLength of the initial equilateral triangle, and
the levels indicating the number of recursive levels performed to create the final snowflake.
Observe that the base case is simply an equilateral triangle with side length equal to sideLength. Each increment of level replaces the middle third of all of the snowflake's sides with a "bump" that is, itself, a smaller equilateral triangle.

**Hint:** It is useful to write a helper function with the following signature:

```python
snowflakeSide(sideLength, levels)
```

The above functions should draw just one side of the underlying equilateral triangle -- along with all of its squiggles or bumps, recursively! 

**All of the recursion will then be in snowflakeSide.** So, first try creating snowflakeSide and make sure that it works and draws a single side of the snowflake curve at the appropriate level of recursion. Once snowflakeSide works, then your snowflake function will call snowflakeSide three times, with appropriate angles between them.

Again, in this strategy, all of the recursion occurs in snowflakeSide. Remember that 
if levels is zero, then snowflakeSide should produce a single line segment (this will be the base case of the recursion);
otherwise, snowflakeSide needs to call itself four times; and, 
keep in mind that you're only creating one of the three sides of the snowflake!
Here are images of four steps (after three levels of recursions) of the overall Koch curve's progression. The first one, the triangle, corresponds to the snowflake with levels = 0 (for snowflake() and snowflakeSide()), with the subsequent ones represent the Koch snowflake with levels = 1, 2 and 3 respectively.

<p align="center">
![](/images/labs/images/360px-KochFlake.gif)
</p>

Test your implementation by calling snowflake(280, 4); you should get the following snowflake:

<p align="center">
![](/images/labs/images/Koch_280_4.gif)
</p>


Drawing the snowflake is definitely challenging. If you have completed this exercise consider it a major accomplishment!! Congratulations on working your way through recursion and lab04! 
However, you may find that you may want to hone your recursion skills a little more. So try out the challenge problems.


# Challenge Problem - Sierpinski Triangles
Create a new file `triangles.py`. Use recursion to have your turtle create the famous Sierpinski triangles, shown below. 

<p align="center">
![alt-frac-3](/images/labs/images/fractals/Sierpinski.png){: height="200px" }
</p>




# More fractal challenge problems

If you want to go still deeper into fractals and recursion, get creative drawing new fractals. There is a general way to recursively create many types of fractals, called fractal decomposition. One starts with a shape oriented in a space along with a replacement rule which is used to refine the picture.  One useful (but optional) rule of thumb is to not remove any shapes once they have been put down, but only to add on to what already exists. Another is to use different replacement rules with various probabilities. Try several of these out, and figure out what kinds of rules lead to beautiful designs. Put all of your code for the optional fractal drawing in a new file called "fractalChallenge.py". 

A list of famous, and intensively studied, fractals is available <http://en.wikipedia.org/wiki/List_of_fractals_by_Hausdorff_dimension> .  

Here are some pictures for inspiration:


<p align="center">

![alt-frac-1](/images/labs/images/fractals/Julia.png){: height="200px" }
![alt-frac-2](/images/labs/images/fractals/Douady_rabbit.png){: height="200px" }

</p>


<p align="center">
![alt-frac-4](/images/labs/images/fractals/fern.png){: height="200px" }
</p>



# Additional exercises

As an individual, you could create an art gallery out of the fractals!  Consider the fractals you created in this lab and imagine what you could create by making changes to your existing code.  Please be sure to name your art gallery fractal files differently from the lab fractal files so that your mentor can review all that you created.

Great job working through lab 4. Feel free to move on to the next lab.







