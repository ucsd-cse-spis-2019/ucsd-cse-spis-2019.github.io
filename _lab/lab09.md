---
layout: lab
num: lab09
ready: false
desc: "Working With Data, by Miles"
assigned: 2016-08-17 10:15:00.00-7
due: 2016-08-22 16:45:00.00-7
---

# Working With Data

In this lab you will work with some data similar to the beer data that we saw in the Facets presentation by UCSD Professor Julian McAuley.   The data he presented was about reviews of beers.   Since SPIS participants are typically under age 21, we'll focus only on the reviews of non-alcoholic beers.

# References

As you work through the steps below, you may find it helpful to refer to:

* the notes from the lecture Miles gave on Wednesday 08/17, 
    which can be found here: [Transcript of Python Shell Session](/lectures/week3/Lecture-08-17.txt){: data-ajax="false"}
* The pages on the SPIS 2016 website about:
    * [Python: Dictionaries](/topics/python_dictionaries/)
    * [Python: defaultdict](/topics/python_defaultdict/)

One more hint: the dictionary methods `.keys()` and `.values()` may come in handy.  This example illustrates how they work:

```python
>>> foo = {'a':3, 'b':3, 'c':5 }
>>> foo.keys()
['a', 'c', 'b']
>>> foo.values()
[3, 5, 3]
>>> 
```

A consequence of this is that if you want to iterate over every key in a dictionary called `foo`, 
you can just do a for loop on `foo.keys()`, e.g.

```python
   for k in foo.keys():
       # do something with key k and value foo[k]
```

# Step 1: Create a lab09 repo

Go to github.com and create a new repo called spis16-lab09-part1-Name-Name using Method 1. When creating the repo import the starter code from this git repo: https://github.com/ucsd-cse-spis-2016/lab09-startercode.git

Then use `git clone` to clone this into your `~/github` directory.

# Step 2: Work with the file `non_alcoholic_data.py` file

In the starter code, you'll find the file `non_alcoholic_data.py`.   Open this file in IDLE, and run it.

This file loads a variable into memory called `data`.  That `data` variable is list of dictionaries.

Now, you might think that the first think you'd want to do is type `data` at the Python prompt, and hit enter, but <span style="font-weight:bold; font-size: 110%; color:red;">PLEASE DON'T DO THAT</span>.  It isn't that anything awful will
happen; it is just that it will temporarily lock up your computer session, and you might have to close it and start over.

Let's explain two things right away: 
1.  What you should do instead
2.  Why typing `data` and hitting enter (which you should NOT do) is a bad idea.

## What you should do instead

Here are several things you can do after running the `non_alcoholic_data.py` file with the `data` variable that are
perfectly fine:

1. Type `type(data)`.
1. Type `len(data)`
1. Type `data[0]`
1. Type `data[42]`
1. Type `type(data[0])`
1. Type `data[-1]`

Try each of those, and see what you get.   Your purpose right now is simply to understand what the data represents by looking through it.  

For the result of `type(data[0])` you should have gotten `dict`, which stands for dictionary.

If you need a review about Python dictionaries, you can consult the lecture notes from either Phill or Miles, or you can
review this page: [Python: Dictionaries](/topics/python_dictionaries)

## Why typing `data` and hitting return is a bad idea

The reason is simple: data is a *huge* list.   It takes a very long time to convert that list into its string representation and then print it out in your IDLE Python Shell.     While it is doing that string conversion, your entire
session just locks up, and it appears that nothing is happening.  Eventually, you will get your prompt back, along with a zillion pages of output.  But that probably isn't what you wanted to see.

## Some other things you could do

Each element in the list `data` represents a single review by some reviewer of some beer.

If want to see all the pieces of data that we can access for a review, we can just look at the string representation of a single Python dictionary for a single review, like this:

```python
>>> data[0]
{'beer/style': 'Low Alcohol Beer', 'beer/ABV': 0.1, 'beer/beerId': '59239', 'review/timeStruct': {'wday': 5, 'isdst': 0, 'mday': 2, 'hour': 21, 'min': 31, 'sec': 21, 'year': 2011, 'yday': 183, 'mon': 7}, 'review/aroma': 3.0, 'review/appearance': 3.5, 'review/timeUnix': 1309642281, 'review/palate': 3.0, 'review/taste': 3.5, 'beer/name': 'Amstel Malt', 'beer/brewerId': '163', 'review/overall': 3.0, 'review/text': "I had this 'beer' at a beachbar in IJmuiden today. Had to drive back home so i needed something without alcohol. This was a good drink for that purpose.\t\tPoured in the original Amstel glass this beer looks quit ok to be honest. Smell in not spectacular but for a malt beer ok. Watery as expected.\t\tSome sweetness in this beer. Drinkable when you have to drive....", 'user/profileName': 'Brabander'}
>>> 
```

Or, if I want to see just the keys in the dictionary, I can use `data[0].keys()`

```python
>>> data[0].keys()
['beer/style', 'beer/ABV', 'beer/beerId', 'review/timeStruct', 'review/aroma', 'review/appearance', 'review/timeUnix', 'review/palate', 'review/taste', 'beer/name', 'beer/brewerId', 'review/overall', 'review/text', 'user/profileName']
>>> 
```

If I wanted to see a list of the names, overall scores, and the review name for the first 10 beers in the list, I could use this:

```
>>> for i in range(10):
	print data[i]['beer/name'],data[i]['review/overall'],data[i]['user/profileName']

	
Amstel Malt 3.0 Brabander
Amstel Malt 3.5 kingcrowing
Harboe Den Glada Danskens Lättöl 2.0 gnoff
Harboe Den Glada Danskens Lättöl 2.0 bark
Bernard S &#269;istou Hlavou 2.0 philipquarles
Juleøl 4.5 jreitman
Mørkt Hvidtøl 3.5 bark
Buckler 3.0 drabmuh
Buckler 4.5 McStagger
Buckler 3.0 jifigz
>>> 
```

However, very quickly, doing this kind of thing at the command line is going to get very tedious.

You are going to get very tired of typing these long strings over and over. You'll want to define some convenient
functions to work with this data.   

So, using IDLE, create a new file called `my_analysis.py'.

In that file, put this code:

```python
from non_alcoholic_data import parseData

def reviewSummary(review):
    return "beer name: " + review['beer/name'] + \
           " overall: " + str(review['review/overall']) + \
           " reviewer: " + review['user/profileName']


if __name__ == "__main__":

  print "Reading Data..."
  data = list(parseData("http://jmcauley.ucsd.edu/cse255/data/beer/non-alcoholic-beer.json"))

  for i in range(10):
    print reviewSummary(data[i])

  print "done"
```

The function definition `reviewSummary` provides a way to print out three particular fields, in this case:
* `beer/name`
* `review/overall`
* `user/profileName`

And, it customizes the label that appears next to each of those so that we can make more sense of the data
we are looking at.   

```
Reading Data...
review                                          beer name             reviewer
beer name: Amstel Malt overall: 3.0 reviewer: Brabander
beer name: Amstel Malt overall: 3.5 reviewer: kingcrowing
beer name: Harboe Den Glada Danskens Lättöl overall: 2.0 reviewer: gnoff
beer name: Harboe Den Glada Danskens Lättöl overall: 2.0 reviewer: bark
beer name: Bernard S &#269;istou Hlavou overall: 2.0 reviewer: philipquarles
beer name: Juleøl overall: 4.5 reviewer: jreitman
beer name: Mørkt Hvidtøl overall: 3.5 reviewer: bark
beer name: Buckler overall: 3.0 reviewer: drabmuh
beer name: Buckler overall: 4.5 reviewer: McStagger
beer name: Buckler overall: 3.0 reviewer: jifigz
done
```

However, it is still a bit messy.  To make it neater, we can decide that we want the data
to show up in some nicely aligned columns.  Here is some code that prints a few fields from the first ten review in some nice columns:

```python
def niceReviewSummary(review):
    return str(review['review/overall']).rjust(5) + \
           review['beer/name'].rjust(50) + \
           review['user/profileName'].rjust(20)


if __name__ == "__main__":

  print "Reading Data..."
  data = list(parseData("http://jmcauley.ucsd.edu/cse255/data/beer/non-alcoholic-beer.json"))

  print  "review".rjust(5), "beer name".rjust(50), "reviewer".rjust(20)
  for i in range(10):
    print niceReviewSummary(data[i])

  print "done"
```

Now the output looks like this:

```
Reading Data...
review                                          beer name             reviewer
  3.0                                       Amstel Malt           Brabander
  3.5                                       Amstel Malt         kingcrowing
  2.0                Harboe Den Glada Danskens Lättöl               gnoff
  2.0                Harboe Den Glada Danskens Lättöl                bark
  2.0                      Bernard S &#269;istou Hlavou       philipquarles
  4.5                                           Juleøl            jreitman
  3.5                                   Mørkt Hvidtøl                bark
  3.0                                           Buckler             drabmuh
  4.5                                           Buckler           McStagger
  3.0                                           Buckler              jifigz
done
```

Now that we see how to look at the data, we might want to actually calculate some things from this data.

For example:

* We might want to be able to filter out reviews based on whether or not we know the age of the reviewer.
* We might want to make a list of just the ages of the reviewers.  
   * Once we have just *that* list, we might want to do some things with it.
* We might want to know what highest rated and lowest rated beers are.
* etc.

In order to be able to answer these types of questions, we need to be able to work with the data in various ways.  One of our most basis tools is to reduce the data down to a simpler form: for example, instead of a list of dictionaries, just a list of numbers.

Your task is to write functions that will take as their parameter, `data`, the result that is returned by the `parseData` function, and then return various things.

Here is a list of the functions you should write.  Add each of these to your `my_analysis.py` file.

You are also encouraged to write a file `test_my_analysis.py`, containing tests for your functions.

To test these functions, you'd make your own values for `data`, that contain probably far fewer reviews than the
real value of `data`, so that you can predict, by hand, what the results of the functions would be.

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
