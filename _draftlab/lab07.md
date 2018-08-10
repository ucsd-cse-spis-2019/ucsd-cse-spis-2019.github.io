---
layout: lab
num: lab07
ready: false
desc: "Working With Data"
assigned: 2018-08-22 13:15:00.00-7
due: 2018-08-25 16:45:00.00-7
---

# Working with and learning from data

This lab will give you a taste of the very hot field of machine learning.  The basic idea of machine learning is to use data to build a program/model that can geneate or make predictions about new data.  In this lab, you will:
 * use basic Python libraries and functions to read date from a file and do basic processing of data
 * build models to generate or predict data

# First, create a lab07 repo

Go to github.com and create a new empty repo called spis18-lab07-Name1-Name2. When creating the repo import the starter file from this git repo: TBA

Then use `git clone` to clone this into your `~/github` directory.

In the repo, you will see that there are XXX files. They will be used to train the machine learning models we will build in this lab.

# Lab outline (TODO)
 * Part 1: reading from files, working with dictionaries and building Markov models to predict text
 * Part 2: training and using a classifier (naive Bayes (binary) and regression (ordinal/continuous))
 
# Part 1: Markov chains and text generation
The basic idea behind machine learning (ML) is to use data to build a "model".  You can think of a model as a computer program that "knows" something about the world. In our case, the model knows how to respond to data in some kind of a human-like way.  

There are three basic steps to any ML task:
1. Select an appropriate model and an appropriate data representation
2. Train the model on some examples
3. Use the model to perform some kind of human-like task

## The task: Writing text
In the first part of lab07, we will build a model that is capable of writing text.  It can write tweets, or your English essay.  And they will seem (almost) like a human could have written them.

## Step 1 (nothing to do, but do read): Model selection and data representation
In this part, we will use a model called a Markov Chain.  The basic idea behind the Markov Chain we will build is that the probability of a word in a sentence is based only on the word that immediately precedes it.  For example, if I see the word "sunny" then there is a relatively high probability that the word "day," "disposition," or "side" (as in "sunny side up") will come next, but a much lower probability that I will next see the word "the", "down" or "shark".  So just by hearing the word "sunny", you have a pretty good idea of the words that might come next.  We will build a Markov chain that has this same knowldege.

Of course, if you heard "It's going to be a sunny..." you'd be almost certain that the next word is "day". Unfortunately, Markov Chains are not that smart.  There can only think about one word at a time.  Fortunately, though, this makes the model simple to learn.

The data representation we will use here is simple: we will represent text as words, in plain text.

## Step 2: Train the model



# Step 2: start ipython and get into the pylab mode
Run commands in terminal

```
ipython
```
Once you are in the ipython interface, run pylab by typing the following command

```
%pylab
```

This is where we will start to use tables to read in and analyze data. Firs type in
```
import numpy as np
from datascience import *
```
This will import the right packages.

Now let's start the lab. When turning in the lab, turn in the code that you complete for each of the questions in a python file. Clearly number the answers such as #Q2.1 etc.

## 1. Introduction

For a collection of things in the world, an array is useful for describing a single attribute of each thing. For example, among the collection of US States, an array could describe the land area of each. Tables extend this idea by describing multiple attributes for each element of a collection.

In most data science applications, we have data about many entities, but we also have several kinds of data about each entity.

For example, in the cell below we have two arrays. The first one contains the world population in each year (as [estimated](http://www.census.gov/population/international/data/worldpop/table_population.php) by the US Census Bureau), and the second contains the years themselves (in order, so the first elements in the population and the years arrays correspond).
Next, we will read in the world population by executing the following command

```
population_amounts = Table.read_table("world_population.csv").column("Population")
years = np.arange(1950, 2015+1)
print("Population column:", population_amounts)
print("Years column:", years)
```
Suppose we want to answer this question:

> When did world population cross 6 billion?

You could technically answer this question just from staring at the arrays, but it's a bit convoluted, since you would have to count the position where the population first crossed 6 billion, then find the corresponding element in the years array. In cases like these, it might be easier to put the data into a *`Table`*, a 2-dimensional type of dataset. 

The expression below:

- creates an empty table using the expression `Table()`,
- adds two columns by calling `with_columns` with four arguments,
- assignes the result to the name `population`, and finally
- evaluates `population` so that we can see the table.

The strings `"Year"` and `"Population"` are column labels that we have chosen. Ther names `population_amounts` and `years` were assigned above to two arrays of the same length. The function `with_columns` (you can find the documentation [here](http://data8.org/datascience/tables.html)) takes in alternating strings (to represent column labels) and arrays (representing the data in those columns), which are all separated by commas.

Create the population table by executing the following python statements
```
population = Table().with_columns(
    "Population", population_amounts,
    "Year", years
)
population
```
Now the data are all together in a single table! It's much easier to parse this data--if you need to know what the population was in 1959, for example, you can tell from a single glance. We'll revisit this table later.

## 2. Creating Tables

**Question 2.1.** In the code below, we've created 2 arrays. Using the steps above, assign `top_10_movies` to a table that has two columns called "Rating" and "Name", which hold `top_10_movie_ratings` and `top_10_movie_names` respectively. You can copy and paste the following code into the ipython shell and complete the `top_10_movies` statement

```
top_10_movie_ratings = make_array(9.2, 9.2, 9., 8.9, 8.9, 8.9, 8.9, 8.9, 8.9, 8.8)
top_10_movie_names = make_array(
        'The Shawshank Redemption (1994)',
        'The Godfather (1972)',
        'The Godfather: Part II (1974)',
        'Pulp Fiction (1994)',
        "Schindler's List (1993)",
        'The Lord of the Rings: The Return of the King (2003)',
        '12 Angry Men (1957)',
        'The Dark Knight (2008)',
        'Il buono, il brutto, il cattivo (1966)',
        'The Lord of the Rings: The Fellowship of the Ring (2001)')

top_10_movies = ...
# We've put this next line here so your table will get printed out when you
# run this complete this question
top_10_movies
```
#### Loading a table from a file
In most cases, we aren't going to go through the trouble of typing in all the data manually. Instead, we can use our `Table` functions.

`Table.read_table` takes one argument, a path to a data file (a string) and returns a table.  There are many formats for data files, but CSV ("comma-separated values") is the most common.

**Question 2.2.** The file `imdb.csv` contains a table of information about the 250 highest-rated movies on IMDb.  Load it as a table called `imdb`.

```
imdb = ...
imdb
```
Notice the part about "... (240 rows omitted)."  This table is big enough that only a few of its rows are displayed, but the others are still there.  10 are shown, so there are 250 movies total.

Where did `imdb.csv` come from? Take a look at your current folder. You should see a file called `imdb.csv`.

Open up the `imdb.csv` file in that folder and look at the format. What do you notice? The `.csv` filename ending says that this file is in the [CSV (comma-separated value) format](http://edoceo.com/utilitas/csv-file-format).

## 3. Using lists

A *list* is another Python sequence type, similar to an array. It's different than an array because the values it contains can all have different types. A single list can contain `int` values, `float` values, and strings. Elements in a list can even be other lists! A list is created by giving a name to the list of values enclosed in square brackets and separated by commas. For example, `values_with_different_types = ['data', 8, ['lab', 3]]`

Lists can be useful when working with tables because they can describe the contents of one row in a table, which often  corresponds to a sequence of values with different types. A list of lists can be used to describe multiple rows.

Each column in a table is a collection of values with the same type (an array). If you create a table column from a list, it will automatically be converted to an array. A row, on the ther hand, mixes types.

Here's a table. (Run the statements below.)

```
# Run this cell to recreate the table
flowers = Table().with_columns(
    'Number of petals', make_array(8, 34, 5),
    'Name', make_array('lotus', 'sunflower', 'rose')
)
flowers
```
**Question 3.1.** Create a list that describes a new fourth row of this table. The details can be whatever you want, but the list must contain two values: the number of petals (an `int` value) and the name of the flower (a string). How about the "pondweed"? Its flowers have zero petals. Create the list for pondweed and insert it into the original flowers table. The new table's name is my_flower

```
pondweed = 
my_flower = ...
my_flower
```
## 4. Analyzing datasets
With just a few table methods, we can answer some interesting questions about the IMDb dataset.

If we want just the ratings of the movies, we can get an array that contains the data in that column:
```
imdb.column("Rating")
```
The value of that expression is an array, exactly the same kind of thing you'd get if you typed in `make_array(8.4, 8.3, 8.3, [etc])`.

**Question 4.1.** Find the rating of the highest-rated movie in the dataset.

*Hint:* Think back to the functions you've learned about for working with arrays of numbers in the numpy package.  Ask for help if you can't remember one that's useful for this.

```
highest_rating = ...
highest_rating
```

That's not very useful, though.  You'd probably want to know the *name* of the movie whose rating you found!  To do that, we can sort the entire table by rating, which ensures that the ratings and titles will stay together.
```
imdb.sort("Rating")
```
Well, that actually doesn't help much, either -- we sorted the movies from lowest -> highest ratings.  To look at the highest-rated movies, sort in reverse order:

```
imdb.sort("Rating", descending=True)
```
(The `descending=True` bit is called an *optional argument*. It has a default value of `False`, so when you explicitly tell the function `descending=True`, then the function will sort in descending order.)

So there are actually 2 highest-rated movies in the dataset: *The Shawshank Redemption* and *The Godfather*.

Some details about sort:

1. The first argument to `sort` is the name of a column to sort by.
2. If the column has strings in it, `sort` will sort alphabetically; if the column has numbers, it will sort numerically.
3. The value of `imdb.sort("Rating")` is a *copy of `imdb`*; the `imdb` table doesn't get modified. For example, if we called `imdb.sort("Rating")`, then running `imdb` by itself would still return the unsorted table.
4. Rows always stick together when a table is sorted.  It wouldn't make sense to sort just one column and leave the other columns alone.  For example, in this case, if we sorted just the "Rating" column, the movies would all end up with the wrong ratings.

**Question 4.2.** Create a version of `imdb` that's sorted chronologically, with the earliest movies first.  Call it `imdb_by_year`.
```
imdb_by_year = ...
imdb_by_year
```
**Question 4.3.** What's the title of the earliest movie in the dataset?  You could just look this up from the output of the previous cell.  Instead, write Python code to find out.

*Hint:* Starting with `imdb_by_year`, extract the Title column to get an array, then use `item` to get its first item.
```
earliest_movie_title = ...
earliest_movie_title
```
## 5. Finding pieces of a dataset
Suppose you're interested in movies from the 1940s.  Sorting the table by year doesn't help you, because the 1940s are in the middle of the dataset.

Instead, we use the table method `where`.
```
forties = imdb.where('Decade', are.equal_to(1940))
forties
```
Ignore the syntax for the moment.  Instead, try to read that line like this:

> Assign the name **`forties`** to a table whose rows are the rows in the **`imdb`** table **`where`** the **`'Decade'`**s **`are` `equal` `to` `1940`**.

**Question 5.1.** Compute the average rating of movies from the 1940s.

*Hint:* The function `np.average` computes the average of an array of numbers.
```
average_rating_in_forties = ...
average_rating_in_forties
```
Now let's dive into the details a bit more.  `where` takes 2 arguments:

1. The name of a column.  `where` finds rows where that column's values meet some criterion.
2. Something that describes the criterion that the column needs to meet, called a predicate.

To create our predicate, we called the function `are.equal_to` with the value we wanted, 1940.  We'll see other predicates soon.

`where` returns a table that's a copy of the original table, but with only the rows that meet the given predicate.

**Question 5.2.** Create a table called `ninety_nine` containing the movies that came out in the year 1999.  Use `where`.
```
ninety_nine = ...
ninety_nine
```
So far we've only been finding where a column is *exactly* equal to a certain value. However, there are many other predicates.  Here are a few:

|Predicate|Example|Result|
|-|-|-|
|`are.equal_to`|`are.equal_to(50)`|Find rows with values equal to 50|
|`are.not_equal_to`|`are.not_equal_to(50)`|Find rows with values not equal to 50|
|`are.above`|`are.above(50)`|Find rows with values above (and not equal to) 50|
|`are.above_or_equal_to`|`are.above_or_equal_to(50)`|Find rows with values above 50 or equal to 50|
|`are.below`|`are.below(50)`|Find rows with values below 50|
|`are.between`|`are.between(2, 10)`|Find rows with values above or equal to 2 and below 10|

**Question 5.3.** Using `where` and one of the predicates from the table above, find all the movies with a rating higher than 8.5.  Put their data in a table called `really_highly_rated`.
```
really_highly_rated = ...
really_highly_rated
```
**Question 5.4.** Find the average rating for movies released in the 20th century and the average rating for movies released in the 21st century for the movies in `imdb`.

*Hint*: Think of the steps you need to do (take the average, find the ratings, find movies released in 20th/21st centuries), and try to put them in an order that makes sense.
```
average_20th_century_rating = ...
average_21st_century_rating = ...
print("Average 20th century rating:", average_20th_century_rating)
print("Average 21st century rating:", average_21st_century_rating)
```
**Question 5.5.** Here's a challenge: Find the number of movies that came out in *even* years.

*Hint:* The operator `%` computes the remainder when dividing by a number.  So `5 % 2` is 1 and `6 % 2` is 0.  A number is even if the remainder is 0 when you divide by 2.

*Hint 2:* `%` can be used on arrays, operating elementwise like `+` or `*`.  So `make_array(5, 6, 7) % 2` is `array([1, 0, 1])`.

*Hint 3:* Create a column called "Year Remainder" that's the remainder when each movie's release year is divided by 2.  Make a copy of `imdb` that includes that column.  Then use `where` to find rows where that new column is equal to 0.  Then use `num_rows` to count the number of such rows.
```
num_even_year_movies = ...
num_even_year_movies
```
**Question 5.6.** Check out the `population` table from the introduction to this lab.  Compute the year when the world population first went above 6 billion.
```
year_population_crossed_6_billion = ...
year_population_crossed_6_billion
```
## 7. Summary

For your reference, here's a table of all the functions and methods you may find useful for table related functions.

|Name|Example|Purpose|
|-|-|-|
|`Table`|`Table()`|Create an empty table, usually to extend with data|
|`Table.read_table`|`Table.read_table("my_data.csv")`|Create a table from a data file|
|`with_columns`|`tbl = Table().with_columns("N", np.arange(5), "2*N", np.arange(0, 10, 2))`|Create a copy of a table with more columns|
|`column`|`tbl.column("N")`|Create an array containing the elements of a column|
|`sort`|`tbl.sort("N")`|Create a copy of a table sorted by the values in a column|
|`where`|`tbl.where("N", are.above(2))`|Create a copy of a table with only the rows that match some *predicate*|
|`num_rows`|`tbl.num_rows`|Compute the number of rows in a table|
|`num_columns`|`tbl.num_columns`|Compute the number of columns in a table|
|`select`|`tbl.select("N")`|Create a copy of a table with only some of the columns|
|`drop`|`tbl.drop("2*N")`|Create a copy of a table without some of the columns|
|`take`|`tbl.take(np.arange(0, 6, 2))`|Create a copy of the table with only the rows whose indices are in the given array|

<br/>

More information about Tables can be found [here](http://data8.org/datascience/tables.html)

Alright! You're finished with lab 09!

