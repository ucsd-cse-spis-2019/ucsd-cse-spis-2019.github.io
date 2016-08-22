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

Let's create a new file called `car_analysis.py'.

In that file, put this code:





Now that we see how to look at the data, we might want to actually calculate some things from this data.

For example:



In order to be able to answer these types of questions, we need to be able to work with the data in various ways.  One of our most basis tools is to reduce the data down to a simpler form: for example, instead of a list of dictionaries, just a list of numbers.

Your task is to write functions that will take as their parameter, `data` and return various things

Here is a list of the functions you should write.  Add each of these to your `car_analysis.py` file.

You are also encouraged to write a file `test_car_analysis.py`, containing tests for your functions.

To test these functions, you'd make your own values for `cardata`, that contain probably far fewer reviews than the
real value of `cardata`, so that you can predict, by hand, what the results of the functions would be.

You can then write test cases for the functions, following the examples of test cases that you saw in [lab06](/lab/lab06).

1. `def beerUserRating(data):` returns a list of Python tuples, where each tuple
   consists of three values: the `beer/name`, `user/profileName`, and the `review/overall` value for each review in the list `data`.

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
