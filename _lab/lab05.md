---
layout: lab
num: lab05
ready: false
desc: "lab05 covering Guttag Ch5, by Diba"
assigned: 2016-08-12 09:30:00.00-7
due: 2016-08-15 17:00:00.00-7
---

If you find typos or problems with the lab instructions, please report them on Piazza

# Learning Goals 
In this lab you will practice the use of lists and other mutable data structures following Chapter 5 of Guttag. We will also review concepts from Chapter 4 of Guttag: recursion, interacting with text files and media files (pictures). 
Note that while media files are not covered in Guttag, working with media requires many of the concepts covered in lecture and in the book. To top it all you will manipulate and transform images.

Your learning goals are:

* Solidify your understanding of recursion.
* Learn to work with larger data sets using lists and files
* Use a new data type: the tuple!
* Import and export media (picture) files in PIL
* Use your programming knowledge so far to manipulate pixels in picture files
* Invent and implement algorithms to transform pictures 

# Work Flow 

* Step 1: Review Chapters 4 and Chapter 5 of Guttag

* Step 2: Get the starter code by cloning the github repo called spis16-lab05-Pair_Name1_Name2 (where Name1 and Name2 are the first names of the pair partners.) Keep your github repo up to date by committing and pushing your changes frequently.  
If you don't recall how to do this, refer to the instructions on using git to complete the labs: TO DO: Add link

* Step 3: For each of the programming exercises in this lab come up with a solution outline by discussing with your partner. Don't be in a hurry to start coding unless you have a fairly clear idea of a solution strategy and your first steps.

* Step 4: Unit test your code as you write new code using the pytest framework

* Step 5: Once you feel you have sufficiently tested your code, submit it to gradescope (remember you can submit multiple times). Only certain exercises require submitting your code to gradescope Refer to this link for instructions on how to submit your code using git: TO DO: Add link

Remember: Developing code is an iterative process. Your code will probably not work as expected on the very first try. Don't be dismayed. Work through your code to identify bugs, test new code frequently and seek help if you feel you are stuck!

We will start with an exercise that reviews recursion and introduces lists for maintaining a dictionary.

# Programming Exercises

## Part 1: Warm up with scrabble  

Recursive functions can be very useful when we're reading, writing, and processing strings. Strings are lists of symbols, like words or sentences. For a review of strings, check out Section 2.3 of the Guttag Python textbook. If you have not worked with strings in Python you should read this section of the book before you proceed.

This exercise is about speeding up your Scrabble scoring with Python and it meant to give you practice with recursion, files and lists. If you've ever played Scrabble, you know that each word is assigned a point value given by the sum (adding together) of the points for each of the letters in the word.  For now, we'll ignore special cases like "double word" and "triple letter" that can increase the point value of a word.  Write a Python function letterScore(let) to take as input a single-character string and produce as output the value of that character on a scrabble tile. If the input is not one of the letters from 'a' to 'z', the function should return 0. 

To write this function you will need to use this mapping of letters to scores

![](/lab/images/alphaScrabble.gif)


This function will not involve recursion, but will involve an if-statement (with several elif's and and else).  For example, imagine that your parameter is named letter. You could start with something like:

```
if letter == 'a':
    return 1
elif letter == 'b':
    return 3
# more here
```

What!? Do I have to write 25 or 26 if elif or else statements? Well, you can, but you don't have to! Instead, use the in keyword to combine multiple cases together:

```
>>> 'a' in 'this is a string including a'
True

>>> 'q' in 'this string does not have the the letter before r'
False
```

Phew!
Here are some examples of letterScore in action:

```
>>> letterScore('w')
4
>>> letterScore('%')
0
```

Next, write the function `scrabbleScore(s)` which should take as input a string s, 
which will have only lowercase letters, and should return as output the Scrabble score of that string. For now, ignore the fact that, in reality, the availability of each letter tile is limited. Also ignore the fact that in a real Scrabble game the words played have to be from the Official Scrabble Dictionary and must use only valid letters. You take this into account later in this exercise. If the user inputs a word with capital letters or punctuation, scrabbleScore still outputs a score: the "bad" letters don't contribute any value to the total word score.   Hint: use the above letterScore function and recursion.

Here are some examples:

```
>>> scrabbleScore('quetzal')
25

>>> scrabbleScore('jonquil')
23

>>> scrabbleScore('syzygy')
25
```

Hints:
As with any recursive problem, your first step is to break this problem down into a base case and a recursive step.  For this problem, your recursive step will probably involve pulling off the first letter in the string and processing it, and then using recursion to calculate the scrabble score for the rest of the string.  
Use string indexing (e.g. `word[0]`) to get the first character, and string slicing (e.g. `word[1:]`) to get the rest of the string.
Think about what happens with the empty string.

## Testing your code

To test your code create a new file named `test_scrabble.py` and implement your test cases in this file. to help you with the testing we have provided you with a file named 'reference.txt'. This file contains a list of words and the scrabble score for each word as computed by our reference implementation. Your test code should read this file, extract each word and its corresponding scrabble score. Then check that the output of your scrabbleScore() implementation matches that provided to you in the reference file. Create your own test files and do some more testing. Once you have your scabbleScore() tested, submit your code to gradescope. You may submit it as many times as you like. Then go on to make the following enhancements.

As a second part to this exercise we ask that you additionally check for valid words before computing the scrabble score of that word. Specifically, implement the function `scrabbleScoreDict(word, dictionary)` that takes as input a dictionary parameter and returns the appropriate score. The parameter 'dictionary' is a list of valid scrabble words and not the dictionary data type that Guttag talks about in Chapter 5. The function should return a score of 0 if the dictionary is empty or if 'word' is not a word in the given dictionary. Other than checking for these two conditions `scrabbleScoreDict()` should behave exactly as the function `scrabbleScore()`. Remember that reusing functions that you have already tested is good coding practice. So, we recommend that you use your `scrabbleScore()` function in your implementation of `scrabbleScoreDict()`, without duplicating the code. If you are wondering where the 'dictionary' parameter is going to come from, worry not. As a final piece of this exercise, you will write the code to read and store a dictionary in your Python program.

To build your own dictionary we have given you a file named dictionary.txt in the starter code. This file contains 235,886 words, one on each line of the file. You are required to read each word in dictionary.txt and store it in a list of words.
The function that does this has the following outline:

``` 

def buildDictionary(filename):

    # Creates a dictionary as a list of words by reading the words in the given file. 
    # Assumes the file contains one word per line

    dict =[]    # Creates an empty list that represents a dictionary
    
    # Your code goes here
    
    return dict
``` 

In the file `scrabble_score.py` create a dictionary list by calling the function `buildDictionary('dictionary.txt')`.

A correct implementation of `buildDictionary()` would populate the 'dict' variable with all the words in the dictionary.txt file and return this large list to the caller of the function. Now think on the following questions:

* Is the 'dict' variable visible/accessible to the caller of `buildDictionary()`? Reason about your answer. 

* Do you think that the caller receives a copy of this large list of words? Why or why not?

* Can you comment on the efficiency of using lists in your Python programs?


## Testing your code with the latest additions
Its time to test the two new functions that you just wrote. Add your test cases to the file `test_scrabble_score.py`. You can reuse the reference.txt file provided to you as before. You should also add additional test cases, for example, checking for invalid words that are not in the 'dictionary.txt' file provided to you.

To test your implementation against our test cases, submit your code to gradescope.
As always, make sure you commit and push your code to github frequently. 

You have gained experience with text files and lists. We will now progress to working with media files (specifically pictures). Just like lists, images are represented in your program as mutable types, which means you can change them in place. Look for this common trait in the following exercises on image manipulation

## Introduction to the Python Imaging Library (PIL)

Our computers encode all data (pictures, games, files) as sequences of 0s and 1s.  They are just a digital kingdom of bits! Some of the text below is review, but be sure to read it over (quickly) anyway.

In your computer, images (pictures) are files stored on your hard disk. A digital image is logically a rectangular grid of pixels, which appear as squares when enlarged; each pixel then typically consists of 1 byte (8 bits) for a Black-and-White image or 3 bytes (24 bits) for a color image, where one byte (a value between 0 and 255) each is for Red (R), Green (G), and Blue (B). R, G, B are three ingredients for all visible colors; for example: blue is 0 redness + 0 greenness + 255 blueness, white is 255 redness + 255 greenness + 255 blueness, and brown is 165 redness + 42 greenness + 42 blueness, etc.. The following figure by Wikipedia shows a color image with enlarged pixels.

![](/lab/images/Pixel-example.gif)

In this exercise (and the subsequent lab) we'll work with the Python Imaging Library (PIL) which is a graphics library like turle designed for working with image files. So let's warm up!

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

The point function takes two arguments: 
(1) a list of pixel coordinates each represented by an (x, y) tuple.  In the example below our first argument is:
  [ (100, 200) ]
which is a list of a single pixel.  Typically in these function, you will be modifying one pixel at a time.
(2) a tuple representing the RGB color to set the pixel to.  In the example above, this color is (0, 0, 0), i.e. black.

After running the command above, show the bear image again and see if you can find the modified pixel.  It's there!
Hiding the stone bear's face

Now we are going to start working in a file so that we can save our work.  If you haven't done so already, create a new Python file, and place the appropriate header comment at the top.  Don't forget your header comment!  Really.  You will lose points for not having your header comments, and these are the most frustrating points to lose!

Now, after the header comment, tell Python that you want to use the Image and ImageDraw modules from the PIL library, as follows:

from PIL import Image, ImageDraw

Next save your file in your Assignments folder as week3Python.py.  Now you're ready to write your first function for this lab.

The stone bear is shy, and he wants you to cover his face using a dark rectangular area. To do this, you will write a function called blockHead which will transform the color of a specified range of the picture to be all black. The header for this function is 

def blockHead( im, startx, starty, endx, endy ):

im is the image to modify (not the Draw object, but the Image), startx and starty represent the x and y coordinates of the upper left corner of the box to paint black and endx and endy represent the x and y coordinates of the lower right corner of the image to paint black.  Your function will not return anything.  For reasons we will discuss in the next week or two, the image will be modified even after the function returns!

You might notice that blockHead is in fact not specific to blocking the head in the stone bear image, but rather will block any rectangle in any image, according to the parameters passed in.

Notes and hints:

In your implementation, the first thing you will need to do is create an ImageDraw.Draw object that will work on im.  For example, the first line of your function will probably be something like:

draw = ImageDraw.Draw( im )

Then you can use this draw object to paint on the image.
Because this is the warmup, you may use the rectangle function in the ImageDraw module to paint the black rectangle.   However, for the rest of this lab, we'll ask you to use nested loops and the paint method, so feel free to try this here.
Don't forget you can access the documentation for the ImageDraw module here
When you have finished writing your function, test it by calling it in the shell to block the stone bear's face.  Note, to do this you will need to do the following as commands in the shell:
Create an image from the stone bear file (if you haven't done so already)
Call your blockHead method, passing in the appropriate arguments  The coordinates of the four corners of the rectangle are (240, 130), (450, 130), (450, 290), and (240, 290), starting from upper left, clockwise.  
Show the image after you call the function to make sure that the black rectangle appears as expected.
If your blockHead is implemented correctly, you should have the shy bear's head cover as follows (left - original, right - covered):

                

## Saving modified pictures

The last step of our warm-up: be aware you just changed a COPY of the stone bear image! Even though you see the change in the stone bear image, that change will not be saved when you exit Python.  What? What does that mean? 

Even after all your work playing with colors and hiding the bear's face in the previous activities, the original picture file has not changed!  To see this, open your "stone bear" file by opening up your Assignments directory on the Desktop and double clicking on the image file. You will find nothing changed. It looks like nothing has been done to it. Why?

Basically, the Python functions you've used are not directly processing the stone bear image on the hard disc.  Rather,  when you open an image, PIL makes a duplicate of that image and loads that duplicate copy into  memory. The copy, as you can imagine, is exactly what was assigned to stonebear, so whatever you have done to stonebear only happened to the copy of your "stone bear" image. 

As a programmer, you should always have the concept of the computer memory in your mind. This technique of loading a copy of a file to memory (which is relatively fast) rather than directly handing a file on the disk (slow) is very common. 

What if we we want to save the changes we've made to the file on disk? We will need to force computer to write the latest memory copies back to the disk, so that the files on the disk change, too.

Let's get back to the shy stone bear. If you correctly changed the stonebear, and you want the actual file of "stone bear" picture to be changed accordingly, you should use the Image.save function. Read the documentation to see how it works (HINT: It takes one argument, which is a string specifying where you want the file saved including its name) and save your modified stonebear picture now.  A word of advice: we recommend you don't apply the changes to the original "stone bear" image, but to a different file (let's say, "shystonebear.jpg" somewhere). This way you won't lose your original picture in case you blocked a wrong area of the shy bear.  

That is all for our warm-ups. Make sure you understand how all this works before launching into your tasks below.
