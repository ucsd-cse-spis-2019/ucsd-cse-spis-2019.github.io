---
layout: lab
num: lab09
ready: false
desc: "Data analysis and plotting"
assigned: 2016-08-17 13:15:00.00-7
due: 2016-08-22 16:45:00.00-7
---

# Data analysis and plotting

In this lab you will work with some data about some cars. You will learn how to plot the data, make a histogram, find correllations between two sets of values.

# References

As you work through the steps below, you may find it helpful to refer to:

* the notes from the lecture Miles gave on Wednesday 08/17, 
    which can be found here: [Transcript of Python Shell Session](/lectures/week3/Lecture-08-17.txt){: data-ajax="false"}
* The pages on the SPIS 2016 website about:
    <Fill this in>


# Step 1: Create a lab10 repo

Go to github.com and create a new repo called spis16-lab10-Name-Name using Method 1. When creating the repo import the starter code from this git repo: FILL THIS IN

Then use `git clone` to clone this into your `~/github` directory.

# Step 2: Work with the file `cardata.py` file

In the starter code, you'll find the file `cardata.py`.   Open this file in IDLE, and run it.

This file loads a variable into memory called `cardata`.  That `cardata` variable is list of dictionaries.

Now, you might think that the first thing you'd want to do is type `cardata` at the Python prompt, and hit enter, but <span style="font-weight:bold; font-size: 110%; color:red;">PLEASE DON'T DO THAT</span>.  It isn't that anything awful will
happen; it is just that it will temporarily lock up your computer session, and you might have to close it and start over.

Let's explain two things right away: 
1.  What you should do instead
2.  Why typing `cardata` and hitting enter (which you should NOT do) is a bad idea.

## What you should do instead

Here are several things you can do after running the `cardata.py` file with the `cardata` variable that are
perfectly fine:

1. Type `type(cardata)`.
1. Type `len(cardata)`
1. Type `cardata[0]`
1. Type `cardata[42]`
1. Type `type(cardata[0])`
1. Type `cardata[-1]`

Try each of those, and see what you get.   Your purpose right now is simply to understand what the data represents by looking through it.  

For the result of `type(cardata[0])` you should have gotten `dict`, which stands for dictionary.

If you need a review about Python dictionaries, you can consult the lecture notes from either Phill or Miles, or you can
review this page: [Python: Dictionaries](/topics/python_dictionaries)

## Why typing `cardata` and hitting return is a bad idea

The reason is simple: cardata is a *huge* list.   It takes a very long time to convert that list into its string representation and then print it out in your IDLE Python Shell.     While it is doing that string conversion, your entire
session just locks up, and it appears that nothing is happening.  Eventually, you will get your prompt back, along with a zillion pages of output.  But that probably isn't what you wanted to see.

## Some other things you could do

Each element in the list `cardata` represents a dictionary of attributes about a specific type of car.

If we want to see all the pieces of data that we can access for a car, we can just look at the string representation of a single Python dictionary for a single car, like this:

```python
>>> cardata[0]
{'Engine Information': {'Transmission': '6 Speed Automatic Select Shift', 'Engine Type': 'Audi 3.2L 6 cylinder 250hp 236ft-lbs', 'Engine Statistics': {'Horsepower': 250, 'Torque': 236}, 'Hybrid': False, 'Number of Forward Gears': 6, 'Driveline': 'All-wheel drive'}, 'Identification': {'Make': 'Audi', 'Model Year': '2009 Audi A3', 'ID': '2009 Audi A3 3.2', 'Classification': 'Automatic transmission', 'Year': 2009}, 'Dimensions': {'Width': 202, 'Length': 143, 'Height': 140}, 'Fuel Information': {'Highway mpg': 25, 'City mph': 18, 'Fuel Type': 'Gasoline'}}
>>> 
```

Or, if I want to see just the keys in the dictionary, I can use `cardata[0].keys()`

```python
>>> cardata[0].keys()
['Engine Information', 'Identification', 'Dimensions', 'Fuel Information']
>>> 
```

Note here that each entry of cardata is actually a dictionary of dictionaries.

1. Type `type(cardata[0])`.
1. Type `type(cardata[0]['Engine Information'])`.
1. Type `cardata[0]['Engine Information'].keys()')`.
1. Type `type(cardata[0]['Engine Inoformation']['Engine Statistics']['Horsepower'])`.

For the last one, you should get type int. If we are interested in Horsepower, we must
look through each dictionary until we find it.

assign a variable to cardata[0] like this

```python
>>> car0 = cardata[0]
```

*What would you write to output the year of this particular car?

## What to do with a list of integers

Let's create a new file called `car_analysis.py'.

In order to be able to answer these types of questions, we need to be able to work with the data in various ways.  One of our most basis tools is to reduce the data down to a simpler form: for example, instead of a list of dictionaries, just a list of numbers.

Your task is to write functions that will take as their parameter, `cardata` and return various things

Here is a list of the functions you should write.  Add each of these to your `car_analysis.py` file.

You are also encouraged to write a file `test_car_analysis.py`, containing tests for your functions.

To test these functions, you'd make your own values for `cardata`, that contain probably far fewer reviews than the
real value of `cardata`, so that you can predict, by hand, what the results of the functions would be.

You can then write test cases for the functions, following the examples of test cases that you saw in [lab06](/lab/lab06).

Write a function `def Horsepower(cardata):` that returns a list of integers of horsepowers for each car in the list `cardata`.

Set HP_list = Horsepower(cardata). It should be a list of integers. Try the following commands:

type(HP_list)

min(HP_list)

max(HP_list)

Do those seem like reasonable values? If not, maybe you should try your list again.

## Plotting Data

The next thing we will do is plot the data HP_list. We are going to use the library matplotlib. It can do a variety 
of visualizations, you may remember in Miles's class last week some of the uses of matplotlib. For example, 
you can plot a scatter plot, a line plot and a bar chart among other things. In this lab, we will be plotting all of those things.

Type this into your car_analysis.py file:

``` python
import matplotlib.pyplot as plt
```

This is a way of giving a nickname to a library so that whenever you call matplotlib.pyplot, you only have to write plt.
This is a standard convention for this specific library. If you are interested in more applications of
matplotlib.pyplot, most of the literature will use this convention.

Let's plot HP_list as a scatter plot.

The scatter plot plt.scatter(xs,ys) takes two lists of numbers (integers or floats) where each list is of equal length 
and it plots a point at each coordinate xs[i],ys[i].

HP_list is only one list so we are going to have to make up another list so that we can plot it.
The other list we will use is the list `range(len(HP_list))`. This is a list of integers [0,1,...,len(HP_list)-1].
We put in the `len` function to be sure that it will have the same length as HP_list.

So, in your python shell write

```python
plt.scatter(HP_list,range(len(HP_list)))
```

It should output something like

```python
<matplotlib.collections.PathCollection object at 0x00000000096B4EB8>
```

This is just saying that it has built your plot but it hasn't actually shown you yet because you may add
things to the plot if you like. for example, you could write

```python
plt.title('Horsepower of cars in cardata')
```

and it will add a title to the plot.
Let's view the plot that we made

```python
plt.show()
```

This will generate a scatter plot with your title. Notice that in your idle, the >>> hasn't reappeared. 
To get back to that, you must close the picture. If you would like to save that picture for later, then you
could click the little disk image on the bottom of the picture.

There is another way to save the image. That is to write
```python
plt.savefig('filename')
```
and it will save the plot as the 'filename' in the same repo that you started in.

Both plt.show() and plt.savefig('filename') "reset" the plot and it will start fresh the next time you define a plot.

What happens if you write plt.show() again?
Nothing! It is because now the plot has been erased. You must build another plot every time.

* Go ahead and make the plot again on your own, and instead of writing plt.show(), write plt.savefig('scatter_HP') and it will
save it as that name.



## Histograms

This scatter plot that we made is kind of a mess. There is a much better way to visualize a list of numbers as an image.
It is called a Histogram. Basically, a histogram is a bar chart of ranges where the height of the bar is based on how many 
data points fall into that range.

add this function into your car_analysis.py file

```python
from collections import defaultdict

def histogramify(data,bins):
	M = max(data)
	m = min(data)
	interval = (M-m)/bins
	hist = defaultdict(int)
	for d in data:
		for i in range(bins):
			if d>m+i*interval:
				f=m+i*interval
		hist[f]+=1
	return hist
```

This is a function that takes as an input a list of data `data` and the number of bins `bins`. The number of bins will
evenly divide the set of values into that many ranges. For example, if the maximum of your list is 200 and the minimum is
100 and bins is ten, then histogramify will split your data range into 10 equal "bins" i.e. 100-110,111-120,121-130,...etc.
Then it will output a defaultdict where the keys and values are both integers. The keys are the lower bound of each "bin"
and the values are how many data points fall in that "bin".

We are going to use histogramify to plot a histogram of the horsepower data.
Assign 
```python
hist_HP = histogramify(HP_list,25)
```

We are going to plot a bar chart, plt.bar(xs,ys) takes two lists of data, each the same length where the height of the bar at 
xs[i] is ys[i].

I am going to show you how to make the lists.
```python
xs = range(min(HP_list),max(HP_list))
```
The x axis represents the actual horsepower values so we want xs to range through each value.
The y axis represents the number of cars with horsepower in a specific range. hist_HP holds all of that data 
in a defaultdict format so if you input a key that hasn't been assigned, it will give you a value of 0.
However all other keys that have been assigned will give you the amount of cars that have horsepower in that range.

```python
ys = [hist_HP[x] for x in xs]

plt.bar(xs,ys)
plt.show()
```

If you have done it right, you should get something that looks like

FILL IN PICTURE

Notice that the bars are really thin. The default width is set to 1. So let's change the width. The way to do that is to add another
argument to plt.bar

So now call

```python
plt.bar(xs,ys,20)
plt.show()
```
It should have made the bars wider.

Now, let's make a histogram with a title and labels for the x-axis and y-axis

```python
plt.bar(xs,ys,20)
plt.title('Histogram of Horsepower Data')
plt.ylabel('Number of cars')
plt.xlabel('Horsepower')
plt.savefig('Histogram_HP')
```
Save this picture by 

2. `def beersRatedFive(data):` returns a list of strings, which are the names of the beers that 
    are rated 5.0 (exactly).   Ideally, your function should NOT include any duplicates.  That is, if a particular beer
    has been rated 5.0 by more than one reviewer, the beer should still appear in the list only once.

3. `def reviewerToAgeInSeconds(data):` returns a dictionary (the regular kind, not a `defaultdict` where
    the keys are the `user/profileName` values from `data`, and the values are the `user/ageInSeconds` values for each of those users.   Note that a user may appear more than once if they wrote more than one review.  We are going to
    assume that the ages are all the same, even if that isn't the case.  And, note that a dictionary already gets
    rid of duplicates, since if you update a value for a key that already exists, it just overwrites the old value,
    rather than creating a duplicate entry. Note, though, that not every review has a value for age.  So, if you encounter
    a review where the user/ageInSeconds is not present, you'll need to set the value for that user to the special
    Python value `None`.

4. `def ageInSecondsToAgeInYears(seconds)` should convert age in seconds to age in years.  Note that with age, we
     don't round up.  If you are 20 years and 355 days old, you are still "age 20", not "age 21".

5.  `def reviewerToAgeInYears(data):` should provide a dictionary that maps reviewer name (those are the keys) to 
    reviewer age in years.  In your solution, please make use of the `ageInSecondsToAgeInYears(seconds)` function 
    that you wrote in a previous step.

6.  `def averageReviewerAge(reviewerAgeDict)` should take, as its parameter, the result of calling `reviewerToAgeInYears`,
     that is, a dictionary that maps reviewer names to reviewer ages.   It should return the average age, in years, of
     a reviewer, as a floating point number (that is, the average age could be `27.6` years, for example.)  As a hint:
     if you have a dictionary foo, you can get a list of all of its value by 

7.  `def beerToNumReviews(data)` should return a `defaultdict(int)` where the keys are `beer/name`, 
    and the values are a count
    of how many reviews appear for that beer.   

8.  `def beerToListOfReviews(data)` should return a `defaultdict(list)` where the keys are `beer/name`, 
    and the value for each key is a list of all of the individual `review/overall` values for that beer.  These lists
    may indeed contain duplicates if multiple reviewers rated a beer the same.

9.  `def beerToAvgReview(data)` should return a dictionary (the regular kind)
    where they keys are `beer/name`, and each value is average
    rating for that beer.  You should make use of the `beerToNumReviews(data)` and `beerToListOfReviews(data)`


When you have written definitions for each of these functions, you can test them in either, or preferably both, of the following ways:

* running the test cases you came up with in your `test_my_analysis.py` file
* call the functions on the value `data`, inside your `if __name__ == '__main__'` block, and print out the results.
* call the functions interactively on the value `data` using the Python shell prompt.

For each function, when you are satisfied that *that* function is working, do the steps to commit your changes to github:

* `git add my_analysis.py`
* `git commit -m "AB/CD describe which function you worked on here"`
* `git push origin master`

When they all work, you are done with lab09!
