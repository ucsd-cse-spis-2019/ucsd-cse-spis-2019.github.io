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
**Question 1.** We want to compute the average of the CEOs' pay. Try running the statements and **You should see an error**
```
np.average(raw_compensation.column("Total Pay"))
```

Let's examine why this error occured by looking at the values in the "Total Pay" column. Use the `type` function and set `total_pay_type` to the type of the first value in the "Total Pay" column.
```
total_pay_type = ...
total_pay_type
```

**Question 2.** You should have found that the values in "Total Pay" column are `numpy.ndarray` which means it is not data, but most likely just text (string). It doesn't make sense to take the average of the text values, so we need to convert them to numbers if we want to do this. Extract the first value in the "Total Pay" column.  It's Mark Hurd's pay in 2015, in *millions* of dollars.  Call it `mark_hurd_pay_string`.
```
mark_hurd_pay_string = ...
mark_hurd_pay_string
```
**Question 3.** Convert `mark_hurd_pay_string` to a number of *dollars*.  The string method `strip` will be useful for removing the dollar sign; it removes a specified character from the start or end of a string.  For example, the value of `"100%".strip("%")` is the string `"100"`.  You'll also need the function `float`, which converts a string that looks like a number to an actual number.  Last, remember that the answer should be in dollars, not millions of dollars.
```
mark_hurd_pay = ...
mark_hurd_pay
```
To compute the average pay, we need to do this for every CEO.  But that looks like it would involve copying this code 102 times.

This is where functions come in.  First, we'll define a new function, giving a name to the expression that converts "total pay" strings to numeric values.  Later in this lab we'll see the payoff: we can call that function on every pay string in the dataset at once.

**Question 4.** Copy the expression you used to compute `mark_hurd_pay` as the `return` expression of the function below, but replace the specific `mark_hurd_pay_string` with the generic `pay_string` name specified in the first line of the `def` statement.

```
def convert_pay_string_to_number(pay_string):
    """Converts a pay string like '$100' (in millions) to a number of dollars."""
    return ...
```

