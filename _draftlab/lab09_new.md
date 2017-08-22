---
layout: lab
num: lab09
ready: true
desc: "Working With Data"
assigned: 2017-08-22 13:15:00.00-7
due: 2017-08-25 16:45:00.00-7
---

# Tables

Welcome to lab 3!  This week, we'll learn about *tables*, which let us work with multiple arrays of data about the same things. Tables are described in [a ebook chapter](http://www.inferentialthinking.com/chapters/05/tables.html) of the text.

First, setup the coding environment and start to execute code

# First, create a lab09 repo

Go to github.com and create a new repo called spis16-lab09-part1-Name-Name using Method 1. When creating the repo import the starter code from this git repo: https://github.com/ucsd-cse-spis-2017/lab09start

Then use `git clone` to clone this into your `~/github` directory.

In the repo, you will see that there are three files, world_population.csv, imdb.csv, and farmers_markets.csv. They are used in this lab for data analysis. 

# Step 2: start ipython and get into the pylab mode
Run commands in terminal

```
ipython
%pylab
```

This is where we will start to use tables to read in and analyze data. Firs type in
```
import numpy as np
from datascience import *
```

This will import the right packages.

Now let's start the lab. 

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

**Question 2.1.** In the code below, we've created 2 arrays. Using the steps above, assign `top_10_movies` to a table that has two columns called "Rating" and "Name", which hold `top_10_movie_ratings` and `top_10_movie_names` respectively.

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
# run this cell.
top_10_movies
```
