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

# Step 1: Create a lab09 repo

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



