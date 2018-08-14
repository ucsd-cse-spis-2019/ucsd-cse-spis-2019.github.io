---
layout: lab
num: lab05
ready: false
desc: "Image Manipulation"
assigned: 2018-08-16 09:00:00.00-7
due: 2018-08-24 15:30:00.00-7
---

If you find typos or problems with the lab instructions, please report them on Piazza


# Learning Goals

In this lab you will manipulate and transform images. A key focus is to give you lots of practice with using loops in your python code, as well as seeing the practical effects of working with mutable data structures. 

Your learning goals are:

* Import and export media (picture) files in PIL
* Use your programming knowledge so far to manipulate pixels in picture files
* Invent and implement algorithms to transform pictures 
* Apply concepts of data mutation


# Work Flow 

* Step 1: Create a private github repo called spis18-lab05-Name1-Name2 (following the naming convention in past labs). 

* Step 2: For each of the programming exercises in this lab come up with a solution outline by discussing with your partner. Don't be in a hurry to start coding unless you have a fairly clear idea of a solution strategy and your first steps.

* Step 3: Unit test your code as much as possible (In most cases you should be able to inspect the outcome of your code visually but we encourage you to use the unittest framework as much as possible)

* Step 4: Track your progress by committing your code frequently to git. Submit your code by pushing it to git. You may do this multiple times.


# Setting up your git repo for {{page.num}} (WITH your partner)

As in previous assignments, you will create one private repository between the two of you. Following our naming convention, your repo should be called `spis18-lab05-Name1-Name2`. There is no starter code to import. 

What comes next is the individual portion of the lab. However, sit next to your partner and feel free to help each other out when you get stuck. The goal is for each of you to get familiar with the PIL library and images, before moving on to the pair partner portion of the assignment. 


# Individual portion: Getting familiar with PIL

First, each of you should clone the private repo to their own account, following the instructions in [lab02](/lab/lab02/). You will create your own files as part of this individual portion and then at the end add them to the shared repo.

In all of the functions below, we would like you to use (nested) loops and the putpixel() function on the Image object. PIL already implements many of the things we're asking you to do below. However, we ask that you use the putpixel() function to re-implement this functionality so that you get practice implementing these more complex functions.

You should also test your functions after writing each one.  You should test them on the stone bear image, and AT LEAST ONE OTHER IMAGE. We suggest using your own picture available in one your earlier git hub repos :)


## Getting familiar with PIL

In this lab we'll work with the Python Imaging Library (PIL) which is a graphics library, like turle, but designed for working with image files. Download the "bear" picture below and save it in your github repo working directory. You can do this by right clicking on the image and selecting the option to save. Be sure to save the image as "bear.jpg".

<p align="center">

![](/images/labs/images/bear.jpg){:height="400px"}

</p>

Next, launch idle in the same directory that you stored the bear image. There, create a new file and at the top of this file put a comment with your name. Save this file as `lab05Warmup_YourName.py` where YourName is replaced with your first name.

In this file, write the following lines of code. 

```python

from PIL import Image

bear = Image.open( "bear.jpg" )

bear.show()

```

The first line instructs Python to import the Image portion of the PIL image library. Whenever you use a function from this library, it will start with `Image.`, indicating you are looking for that function in that specific library. The next line of code opens an image and stores a reference to it in the `bear` variable. If you are getting an error here it's probably because you either placed the file in the wrong place or launched IDLE from a directory different from where the image was stored. You could resolve this issue by including the path (i.e., complete location in the directory structure), or by moving the file to the correct location.

Before you move on, add comments to your file to explain each line of code.

How many pixels is your image? Find out the total number of pixels and add it as a comment at the start of your file. The following command could be helpful:

```
bear.size
```

Next, we are going to access a specific pixel from the image by using the `getpixel()` function. The arguments of this function are a picture object and the pixel's X position and its Y position; the function returns the pixel object at the coordinate(X, Y) of the image. Note that in the image grid, the axis is a little different from the usual 2D Cartesian axis, in that it counts from upper left to bottom right. For example, in the following 18 x 18 image grid, the coordinate (11, 7) is the grey block. Note the index starts at 0.

<p align="center">
![](/images/labs/images/coordinates.gif){:height="400px"}
</p>

If you make the following statement:

```
pixel = bear.getpixel( ( 100, 200) )

```

the pixel returned is a tuple representing the RGB values of the pixel on the 200th row from top, 100th column from left, in the image. In the shell, check the value:

```
>>> pixel
```

Now, let's see how to modify the colors of individual pixels in the image.  To modify a pixel use the putpixel function
```
>>> bear.putpixel( (100, 200), (0, 0, 0) )
```

The `putpixel` function takes two arguments: 

* a pixel coordinate  represented by an (x, y) tuple.  In the example below our first argument is: (100, 200) , which is a tuple representing a single pixel. Using this function, can modify one pixel at a time.

* a tuple representing the RGB color to set the pixel to.  In the example above, this color is (0, 0, 0), i.e. black.

Add the `putpixel` command to your code and check the bear image. Can you find the modified pixel? If you have a hard time seeing the modified pixel, try instead the following code to turn a range of pixels black.

```
for i in range(100):
    stonebear.putpixel( (i, 200) , (0, 0, 0) )

```

For detailed information on the functions we have used so far, you can check out the [documentation for the Image module](http://pillow.readthedocs.io/en/3.1.x/reference/Image.html)



## Inverting the colors

Now, let's try to modifying our image in an interesting way. Way back in the days of film cameras and chemical processing of photo images, one step in the processing process produced a negative image. We can achieve the negative (aka inverted effect digitally by subtracting each of the original RGB values of a pixel from 255. For example, if the pixel RGB values are (34, 67, 87), the new RGB values of that same pixel should be (221, 188, 168), basically 255-34, 255-67, and 255-87. Of course, you need to do this not only for one pixel, but for all the pixels in the image. 

In your file, create a function `invert` as shown below that does this operation for all pixels of an image. Note that this function is incomplete, so it is up to you to fill in the missing lines of codes.  

```
def invert( im ):
    ''' Invert the colors in the input image, im '''
    
    # Find the dimensions of the image
    (width, height) = im.size

    # Loop over the entire image
    for x in range(width ):
        for y in range( height ):
            (red, green, blue) = im.getpixel((x, y))
            # Complete this function by adding your lines of code here
            # to calculate the new pixel values and then to change them
            # in the image using putpixel()

```

To call this function on the bear image, you will need to add the following line of code in your file. 
```
invert(bear)
```

When you now run the code, your result should look similar to this.

<p align="center">
![](/images/labs/images/PIL/invertedbear.jpg){:height="400px"}
</p>



## Saving modified pictures

At the moment, you are only modifying a copy of the image that is stored in local memory. You are not actually changing the `bear.jpg` file. Any of the changes you make, will not be saved when you exit Python. The reason is that the Python functions you've used are not directly processing the stone bear image on the hard disk.  Rather,  when you open an image, PIL makes a duplicate of that image and loads that duplicate copy into  memory. So as a programmer, you should always have the concept of the computer memory in your mind. This technique of loading a copy of a file to memory (which is relatively fast) rather than directly handing a file on the disk (slow) is very common. 

To save changes to disk, you should use the `Image.save` function. Read the documentation to see how it works (HINT: It takes one argument, which is a string specifying where you want the file saved including its name). Give this new file a different name (i.e., don't use `bear.jpg`), as we will be using the original file throughout this lab.

Add the save function to your code and test it.



## Modifying only a part of the image
Next, create a new function in your file: 
```
def invert_block( im ):
```

Its functionality should be the same as the of `invert()`, except that it only inverts the pixels that are in the upper right quadrant of the image (so only inverts 25% of the image) and leaves the others unchanged. 

To test if it works, apply `invert_block()` to the bear image (just don't use the original `invert()` function).

Now, what happens if you apply `invert()` first and then next apply `invert_block()` to the same image? Make sure you understand why this is happening.


## Submit your code
Submit your code using the command line tools `git add`, `git commit` and `git push`. Verify that your code is pushed properly to git by navigating to your repo on github.com and viewing your latest changes.

At this point you are done with the individual portion.  If your partner is not yet done DO NOT CONTINUE. 
Instead, modify your code to include other interesting transformations on the pixels instead of the version. For example, what happens if you swap color channels (R becomes G, G becomes B, B becomes R)? What happens when you delete (set to 0) one or more of the color channels? Can you modify your code such that these transformations only apply to every other pixel rather than every pixel?


# Pair portion: Doing more with the Turtle

**STOP!  Do not start on this part of the lab until BOTH partners have completed the individual portion.  When you do start, make sure you use _pair programming_**

Now we are going to start working in a file so that we can save our work.  If you haven't done so already, create a new Python file called "imaging.py" in your repo, and place the appropriate header comment at the top that descibes the content of the file.  Don't forget your header comment. 


## Greyscale

Now that we have some experience changing the colors in a picture, we'll write functions to make greyscale and black and white (binary) images.  The concept of image luminance will help us out. In layman's terms, luminance is how bright or dark the colors in a pixel are (compared to white).

As Wikipedia calculates it, luminance is 21% red, 72% green, and 7% blue. Intuitively, this makes sense because if you think of standard red, green, and blue, green is the lightest and thus has highest positive impact luminance, while blue is darker and has a lower value for luminance. This is useful! You're going to calculate luminance for pixel operations.

Write a new function called greyscale that takes an image as a parameter and modifies it to make it greyscale. For this, you'll want to do something similar to invert, except that we will first calculate the luminance of a pixel and then set each of the three color channels to this value.  Since luminance is an indication of how white/black a pixel is, just insert the same value in each of the three color channels!


<p align="center">

![alt-bear1](/images/labs/images/PIL/originalbear.jpg){:height="400px"} 
![alt-bear2](/images/labs/images/PIL/grayscalebear.png){:height="400px"}

</p>


Hint: Getting an OverflowError: unsigned byte integer is greater than maximum? This might be because your luminance calculation results in RGB values higher than 255. Make sure that all of your percentages add up to 1. Also, if you get "integer argument expected, got float", it may mean you are trying to assign red, green or blue a floating point value. You may solve this by using a typecast c = int(a/b) or doing an integer division c = a//b versus the floating point one c = a/b (Note that this is one of the differences between Python 2, which was used last year in SPIS, and Python 3, which we are using this year. In Python 2, the / with two integer arguments resulted in an int, while it results in a float for Python 3. See also (http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html#integer-division). This is one of the challenging issues when porting between these two different versions of Python).

## Binarize

Now, write a function called `binarize( im, thresh,  startx, starty, endx, endy)`, which makes modifies a portion of im to be black and white based on a threshold luminance value (thresh) specified by the user. This threshold is a brightness value between 0 and 255 - if a pixel's RGB average is greater than the threshold value, then it should turn white, and if it is less than the threshold value, then it should turn black. It should only apply this operation to pixels that are inside a box, where startx and starty represent the \coordinates of the upper left corner of the box and endx and endy represent the x and y coordinates of the lower right corner. Your function should check that these numbers are valid. If they are not, the function should do not modify the image, but print a warning.

<p align="center">

![](/images/labs/images/PIL/binarizedbear.png){:height="400px"}

</p>

        

## Geometric transformations

The following four functions take an image as an argument and do some geometric transformations on it.  

### Vertical mirroring
Write `mirrorVert`: This function takes an image and modifies the image to mirror the photo across its horizontal axis (i.e., so that the top part is mirrored upside down on the bottom of the image). Hint: Think carefully about which pixels you need to loop over, and where each pixel in the top half needs to be copied to create the mirror effect.  Start with concrete examples. Then derive the general formula based on the pixel's location (x, y) and the height and width of the image.

<p align="center">

![](/images/labs/images/PIL/vertmirror.jpg){:height="400px"}

</p>

### Horizontal mirroring
`mirrorHoriz`: Same as above, but mirroring across the vertical axis. Hint:  Instead of replacing the bottom rows with the reversed top rows (as you did in `mirrorVert`), you'll replace the last half of the pixels in every row with the reversed first half of the pixels.

<p align="center">

![](/images/labs/images/PIL/horizmirror.jpg){:height="400px"}

</p>

### Vertical flipping
Write `flipVert`, a function which flips the image in a picture along its horizontal axis (so the result is that the bottom is on the top and the top is on the bottom). Again, think carefully about where each pixel needs to end up, how far your loop needs to run, and be careful not to overwrite the pixels in the bottom half of your image before you've copied them over into the top!

<p align="center">

![](/images/labs/images/PIL/flipvert.jpg){:height="400px"}

</p>


## Geometric transformations returning a copy of the image

The next three methods create and return a copy of the image passed in (i.e., use the return statement). They should NOT modify the original image.
The command below can be helpful. It creates a new image im, as a color image (this is what the RGB means), of a certain width and height given by the tuple.
```
    im = Image.new('RGB',(width,height))
```
### Scale
Function `scale` takes an image as a parameter and creates a copy of that image that is scaled to be half its original size.  Then return this scale copy. Hint: one way to do this is to skip every other pixel when copying from one image to the other. Be careful with your coordinates so that you do not go out of bounds in the smaller image.

### Blur
Function `blur` also returns a modified copy of the image. This copy will be a blur of the original image, created by combining neighboring pixels in some way (entirely up to you). You might consider averaging the RGB values of a designated 'square' of pixels, then changing each of these pixels' values to the average.

## Submission

Submit your code to github using the usual `git add`, `git commit`, `git push` commands


# Pair portion: Doing more with the Turtle

### Random grid
Function `randomGrid` also returns a copy of the original image.  To create this copy it divides the image into an NxN grid (where the N is up to you, or make it an argument of the function) and randomly sorts the pieces of the grid across the image - "sliding puzzle"-style. Hint: you can use the random library (just google this). 
```
    import random
```

Now it's time to create your own effects!! Please be sure to include a comment or note to the tutors explaining what you did. Be creative!  There is literally no end to this assignment. Add any creative routines that you come up with to your public repo and continue working on the joint group mashup project.


<p align="center">

![alt-art1](/images/labs/images/PIL/art1.png){:height="400px"} 
![alt-art2](/images/labs/images/PIL/art2.jpg){:height="400px"} 
![alt-art3](/images/labs/images/PIL/art3.png){:height="400px"} 
![alt-art4](/images/labs/images/PIL/art4.png){:height="400px"} 


</p>


Congratulations on finishing lab 5!!








