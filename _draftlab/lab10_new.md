---
layout: lab
num: lab10
ready: false
desc: "Functions and Visualization"
assigned: 2017-08-28 13:15:00.00-7
due: 2017-08-30 16:45:00.00-7
---


Welcome to lab 10! We'll practice functions and the table method `apply` from [this ebook description](https://www.inferentialthinking.com/chapters/07/1/applying-a-function-to-a-column.html).  We'll also learn about visualization from [a chapter in data8](https://www.inferentialthinking.com/chapters/06/visualization.html).

# First, create a lab10 repo

Go to github.com and create a new repo called spis16-lab10-Name-Name using Method 1. When creating the repo import the starter code from this git repo: https://github.com/ucsd-cse-spis-2017/lab10starter

Then use `git clone` to clone this into your `~/github` directory.

In the repo, you will see that there are three files, world_population.csv and imdb.csv. They are used in this lab for data analysis. 

# Step 2: start ipython and get into the pylab mode
Run commands in terminal

```
ipython
%pylab
```

This is where we will start to use tables to read in and analyze data. First type in
```
import numpy as np
from datascience import *
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
```
This will import the right packages. The matplotlib package will allow us to have graphing capabilities

Now let's start the lab. When turning in the lab, turn in the code that you complete for each of the questions in a python file. Clearly number the answers such as #Q2.1 etc.

## 1. Functions and CEO Incomes

Let's start with a real data analysis task.  We'll look at the 2015 compensation of CEOs at the 100 largest companies in California.  The data were compiled for a Los Angeles Times analysis [here](http://spreadsheets.latimes.com/california-ceo-compensation/), and ultimately came from [filings](https://www.sec.gov/answers/proxyhtf.htm) mandated by the SEC from all publicly-traded companies.  Two companies have two CEOs, so there are 102 CEOs in the dataset.

We've copied the data in raw form from the LA Times page into a file called `raw_compensation.csv`.  (The page notes that all dollar amounts are in millions of dollars.)
Run the following command in ipython

```
raw_compensation = Table.read_table('raw_compensation.csv')
raw_compensation
```
