---
layout: lab
num: lab02
ready: true
desc: "Next steps with github, Python functions, testing"
assigned: 2018-08-08 13:15:00.00-7
due: 2018-08-14 17:00:00.00-7
---

If you find typos or problems with the lab instructions, please report them on Piazza.  Throughout this lab you might sometimes see accounts or directories using `spis16`.  This is leftover from 2 years ago, but shouldn't change the overall meaning of the explanations and examples.  You should expect to see and use `spis18` instead of `spis16`.  

# Overview

The main purpose of this lab is to practice, as pairs, a few skills involving Python, Unix, and github.

# Partner structure for {{page.num}}

You will work with a partner for the programming part of this lab.  However, you should work through the Unix part of this lab by yourself.  You should work next to your partner, making sure you both understand what you are doing.  

# More specific Learning Objectives

The most important thing we want you to get out of this lab is the ability to
* create a solution to a Python problem 
* iterate until your solution produces the correct behavior on a wide as possible range on inputs
* keep every step of that development process in a github repo


Here's a more complete list of our learning objectives:

* A few Unix commands, including:  `pwd`, `ls`, `cd`, `mkdir`
* Some new options for creating a private github repo for a lab
   * Creating it with a README.md and .gitignore for Python
   * Adding a pair partner as a collaborator.
* How to clone a private repo at the Bash (Unix) command line
* How to store a Python file in that repo
* The basic git workflow of `git add...`, `git commit...`, `git push...`
* Testing of Python functions


# Step-by-Step through {{page.num}}

## Step 1: Create a `~/github` directory on your ETS (i.e. "lab") account

The following article explains how to create a `~/github` directory on your ACMS account.

* [Creating `~/github` and learning some shell commands in the process](/topics/acms_create_github_dir/)

It also covers some basics of the commands you can use at the bash shell prompt&mdash;commands such as
`pwd`, `cd`, `mkdir`, and others that you'll need to know for SPIS (and in your later UCSD CSE courses) for working
with your ETS account.

If *both* you *and* your pair partner are already thoroughly familiar with Unix command basics&mdash;that is, you know how to create `~/github`, and you are *throughly* familiar with everything in the table below, you can just create `~/github`, and skip the tutorial.

But if either or both of you has any doubt, you are strongly encourage each of you to go through this page carefully and slowly,
to learn some of the basics of working with Unix commands at the bash shell.  That is one of the most fundamental skills you'll need throughout all of the courses that use the ACMS unix accounts during your entire stay at UCSD.

We would encourage you to go through the entire tutorial at least once in one pair partner's account, and then repeat it briefly in the second pair partner's account so that each partner has a ~/github subdirectory.

To help you review whether you got all of the necessary learning from the tutorial, here is a brief overview (it is contained in the tutorial as well.)

Unix shell commmands:

| Unix Command   | Brief explanation                                               |
|----------------|-----------------------------------------------------------------|
| `date`         | Show current date and time                                      |
| `history`      | Show history of recent unix commands                            |
| `pwd`          | Print working directory                                         |
| `ls `          | List files                                                      |
| `mkdir foo`    | Create subdirectory (folder) `foo` in  current directory        |
| `mkdir ~/bar`  | Create subdirectory (folder) `bar` under home directory (`~`)   |
| `cd`           | Change directory to home directory (1st option)                 |
| `cd ~`         | Change directory to home directory (2nd option)                 |
| `cd foo`       | Change directory to `foo` inside current directory              |
| `cd ..`        | Change directory to parent of current directory (go up)         |
| `cd ~/fum`     | Change directory to `fum` inside home directory (`~`)           |

You should also learn the following concepts:

* Home directory (`~`), directory, and subdirectory
* Unix/Linux directory tree, rooted at `/`
* Bash Shell
* Shell prompt

When both partners have a `~/github` directory and are comfortable with shell basics, move on to Step 2.

## Step 2: Create your shared lab02 repo 

There are three steps involved here.  First, we'll give you an overview, and then the details:

1. One of the two pair partners should log into github.com to create an empty private repo *in a particular way*, namely,    pre-populated only with a README.md, and a .gitignore for Python.  
2. The first pair partner will then invite the second to be a collaborator with <b>Admin</b> access.   
3. Finally, the second pair partner needs to accept the invitation to be a collaborator.    


Note: it doesn't matter which pair partner creates the repo&mdash;it can be the one listed first, or the one listed second in the pair name.  For example, if the pair is listed as Alex_Chris in the <b>Pair Name</b> column on the [SPIS 2018 list of pairs](/info/pairs/), it doesn't matter whether Chris creates and then invites Alex, or Alex creates and then invites Chris.   

For purposes of the rest of these instructions, though, we'll refer to "first" as the partner
under whose github account the repo is initially created, and "second" as the partner that gets invited to collaborate.

And regardless of who creates and who invites, *please* name the repo according to the pair order that is listed in the <b>Pair Name</b> column on the [SPIS 2018 list of pairs](/info/pairs/).  That makes it MUCH easier for us to find your work!
   
### Step 2a: Create a private repo with a README.md and a .gitignore file for Python.

Choose which pair partner is going to create the repo&mdash;that pair partner should be the one that is logged into github.com.

To create the repo follow the instructions at the link: [github create repo Method 2](http://ucsd-cse-spis-2018.github.io/topics/github_create_repo/#method2).

As you follow these instructions, create:
* a private github repo under the `ucsd-cse-spis-2018` github organizaiton,
* with the name `spis18-lab02-Name1-Name2` where,
    * `Name1` is the first pair partner's preferred first name
    * `Name2` is the second pair partner's preferred first name

The <b>Pair Name</b> column in the [SPIS 2018 Pairs List](/info/pairs/) page corresponds to this `First-Second` part of your repo name.

An example correct repo name for the ficticious SPIS students Alex Triton and Chris La Jolla would be: 

`spis18-lab02-Alex-Chris`.

### Step 2b: First pair partner invites second pair partner to be a collaborator

The pair partner that created the repo will automatically have access.  That partner needs to invite the second
partner to be a collaborator with admin access.

The instructions to do that are found here: [Github: Adding collaborators](https://ucsd-cse-spis-2018.github.io/topics/github_add_collaborators)

### Step 2c: Second pair partner accepts the invitation

The second pair partner should accept the invitation.  This is usually straightforward: there is an invitation in the second pair partner's incoming email with a link to click, and it is clear what to do.

If the email doesn't arrive, though, or anything is not clear, there are troubleshooting instructions later on the same page you accessed in the previous step to add the partner as a collaborator:  
[Github: Adding collaborators](https://ucsd-cse-spis-2018.github.io/topics/github_add_collaborators)
 

## Step 3: Cloning a private repo at the bash (Unix) command line

Next, you need to clone your private repo into the `~/github` directory of one of your ACMS accounts (either one will do.)

The instructions to do that are here: [cloning your first repo](/topics/git_cloning_your_first_repo/).

When you've done that, we are finally ready for some Python programming!

## Step 4:  How to store a Python file in a repo

To review what you've done so far:

* You create a repo called `spis18-lab02-Name1-Name2` on github.com
* You cloned that repo into your ACMS account under the `~/github` directory.
* That means you actually have *two* repos now. 
    * The repo on github.com and the repo on your ACMS account are *separate*, but *linked*
    * More specifically, the one on ACMS points to the one on github.com as its `origin` repo
    
What you will do now is put some Python code into the local repo&mdash;or more precisely, you'll put some Python
code into the directory that corresponds to that repo.   You won't actually commit it to the repo until the next step.

So, what we want to do first is make `~/github/spis18-lab02-Name-Name` (except with your pair's names, not literally `Name-Name`) be your current directory.     Use the `cd` command to make that happen.  

When you've done it, you 
should be able to type `pwd` and see that your current directory path ends in `github/spis18-lab02-Name-Name`, just like in the example output below:

```
[spis18t3@ieng6-240]:spis18-lab02-Alex-Chris:118$ pwd
/home/linux/ieng6/spis18/spis18t3/github/spis18-lab02-Alex-Chris
[spis18t3@ieng6-240]:spis18-lab02-Alex-Chris:119$ 
```

Then, start up IDLE by typing `idle3`:

```
[spis18t3@ieng6-240]:spis18-lab02-Alex-Chris:119$ idle3
```

Once you do, use the `File -> New File` menu item to open a new window in which you can type Python code.

Into this window, enter this function definition.  This function uses the the gender wage gap in the United States to calculate a woman's wage based on the corresponding male wage.  The wage gap is defined as the difference between a man's salary and a woman's salary, expressed as a percentage of a man's salary.  In the United states the wage gap is 18.2%.  To calculate a woman's salary, given a man's salary using the wage gap we can multiply the man's salary by 1-wageGap.  You can learn more about the wage gap and see more data [here](https://data.oecd.org/earnwage/gender-wage-gap.htm).

It should make sense to you based on what you've learned about Python functions so far.

```python
# wageCalculator.py
def convertWageMtoW(mWage):
   wageGap = 0.182
   ratio = 1-wageGap
   return ratio*mWage
```

Save this file by choosing `File -> Save` from the Idle menu, giving it the name `wageCalculator.py`.  

When you save, the save dialog should indicate that they are being saved inside the ~/github/spis18-lab02-Name-Name folder that corresponds to your local github repo (you should see a .git directory already present).   It is important that they are saved there, and not somewhere else.   If you save them in another place, the next few steps of the lab won't work properly.

Onve you have saved your file, with IDLE still open, open a second terminal window and navigate in that window into the `~/github/spis18-lab02-Name-Name` folder, and do an ls command as shown here.  You should see your file, with the name exactly as shown here.

Note that if you also have a .pyc file, that's fine (or if you don't, that's fine too).  You don't need to worry about that one, or remove it.  Files ending in `.pyc` are "compiled Python" code. They are temporary files used to speed up the execution of your Python code.   Mostly, just leave them alone and they'll come and go as needed.  

```
[spis18t3@ieng6-240]:spis18-lab02-Alex-Chris:170$ ls
README.md  wageCalculator.py  wageCalculator.pyc
[spis18t3@ieng6-240]:spis18-lab02-Alex-Chris:170$ 
```


### Now run and test your code

So now you've got a function, but how do we know this code is correct?  We need to test it!  And in order to test it, we need to define some test cases--in other words, we need to calculate the expected output for several inputs.  The first step to testing is to define these input-output pairs.  We can use a calculator to do this, for example:

* men's wage of 100 should output 81.8
* men's wage of 76.2 should output 62.3316
* men's wage of 0 should output 0.0

It's good to try a range of inputs that are qualitatively different.  Notice in the test cases above, I have selected one non-zero integer input, one decimal number and the number 0.

Now we need to run these tests cases.  We can do this in one of two ways:

*Option 1: Running test cases in the interactive shell*
Load the Python code into the interacive Python window by selecting "Run -> Run Module" from the menu at the top of the window with the function definition you copied in above (wageCalculator.py), or simply by pressing F5 in the window with the code.  Now in the Python shell at the `>>>` prompt, run each test case one at a time, and visually verify that that the answers are correct:
```
>>> convertWageMtoW(100)
81.8
>>> convertWageMtoW(76.2)
62.3316
>>> convertWageMtoW(0)
0.0
```

You might find that your imlementation returns values that are *almost* correct, e.g. 0.000000000000000000001 for 0.0 or something similar.  This is due to imprecision in the way Python represents floating point numbers and is completely normal.  You should consider your results correct if they "very close" to the expected results.

*Option 2: write tests in a main method*
The second option for writing test cases is to write a special method, called a main method, that will be automatically run when you load your code into the interpreter using F5.  Add the following code to your `wageCalculator.py` file, below the code for your `convertWageMtoW` method:

```python
def approximatelyEqual(expected, val, epsilon):
    ''' Returns true if expected and val are equal within a difference of
        epsilon '''
    diff = abs(expected-val)
    return diff < epsilon

def main():
    epsilon = 0.001
    print("Testing convertMtoW(100)...")
    ans = convertWageMtoW(100)
    expected = 81.8
    # Make sure 
    if approximatelyEqual(ans, expected, epsilon):
        print("Correct!")
    else:
        print("Incorrect.  Expected " + str(expected) + " but got " + str(ans))

    print("Testing convertMtoW(76.2)...")
    ans = convertWageMtoW(76.2)
    expected = 62.3316
    if approximatelyEqual(ans, expected, epsilon):
        print("Correct!")
    else:
        print("Incorrect.  Expected " + str(expected) + " but got " + str(ans))

    print("Testing convertMtoW(0)...")
    ans = convertWageMtoW(0)
    expected = 0.0
    if approximatelyEqual(ans, expected, epsilon):
        print("Correct!")
    else:
        print("Incorrect.  Expected " + str(expected) + " but got " + str(ans))

if __name__ == "__main__": main()

```

Now when you run your code using F5 from the window, all the tests will run automatically.  Notice that main uses the method approximatelyEqual, which we wrote above to compare floating point numbers taking into consideration roundoff error. Make sure you understanding the code above.  What do you think the last line does?  Talk to your partner, and if you have questions, ask the tutors or instructors.

You can use either method to test your code throughut SPIS.  Or you can check out [Option 3: Unit Testing](https://docs.python.org/3.7/library/unittest.html).

Ok, so now you have a Python file with a function definition in it, and you have some test cases.

What's next?  We want to get this Python code into your local git repo, and then push the changes up to github.com.


## Step 5:  The basic git workflow of `git add...`, `git commit...`, `git push...`

So, having the code in the directory isn't enough to get it into the git repo.

You actually have to go through a series of two steps to get the code into your local repo, and then
a third step to update the `origin` repo on github.com with that code.

The process is described in two articles: 

* a longer version that goes into more detail: [Git: basic workflow](/topics/git_basic_workflow/)
* a shorter version that is more handy reference: [Git: worflow explained](/topics/git_workflow_explained/)

Essentially, though here's what you are going to do:

1.  Make sure you are in your ~/github/spis18-lab02-Name-Name directory
2.  Type `git status` and read what it says
3.  Type `git add wageCalculator.py` to *stage* this file (get it ready to be added to the repo)
4.  Type `git status` and read what it says
5.  Type `git commit -m "wageCalculator functions and tests"` to commit the changes and provide an explanation of what you did
6.  Type `git status` and read the messages
7.  Type `git push origin master` to push the changes from your local repo to the origin repo (on github.com)
8.  Type `git status` and read the messages
9.  Navigate to your repo's page at https://github.com and see that the two files now appear there, along
    with your commit message. You may need to refresh the page if you were already on it.

Congratulations, you've just done your first of many dozens of git commits you'll do during SPIS, and the first
of hundreds or thousands you'll do during your four years at UCSD.

## Step 6: Adding (and testing) additional functionality to your wage converter

Finally, it's time for you to write your own code.  

Extend the functionality of your wageCalculator function so that:
* It takes at least one additional parameter
* It uses an if-statement (or if-else statement, or if-elif-else statement, etc) in its functionality

You can use the data on [this page](https://data.oecd.org/earnwage/gender-wage-gap.htm), or any other data you find on the web in your functions.

Exactly what your extended function does is up to you and your partner, but it should still be focused on calculating salaries based on the gender wage gap.  Here are some ideas for extensions, but feel free to come up with your own:
* Add race/ethnicity information to the calculator.  For example, the calculator might take an additional parameter, which is race, and calculate the salary of a woman of that race, assuming the wage input is for a man of that same race (or alternatively the wage of a white man).
* Add a country parameter, and calculate salaries differently based on wage gaps in different countries.

### Comment your code
In a comment above your modified function, make sure you describe what it does.  Include a description of what each parameter means, and what is returned.

### Test your code
Come up with several test cases, and then run your code on these test cases using one of the two testing methods described above.  If any of your test cases fail, fix your code so that they pass.  Make sure you test enough cases so that you are confident your code works in all cases.  For example, if you take a country name as one of your parameters, what happens if the user enters a country your code does not know about?  Does it behave as you expect?

If you chose Option 1 for your testing strategy (entering tests at the interactive prompt), please _copy and paste_ your test runs (including the output) into comments in your wageCalculator.py file so we can see how you tested your code.

If you get part-way done, and *some* of your tests pass, but not others, or you are in the middle of working
when it is time for a break, that is STILL a good time to do a commit.   Add the letters "WIP" to the start of your
commit message so you know that this is not a finished product.  "WIP" stands for "Work in Progress".  For example:

```
git status
git add wageCalculator.py
git status
git commit -m "WIP CL/AT  Some tests passing, others failing"
git status
git push origin master
```

* As a reminder, the `CL/AT` is used to indicate that you were working as a pair, with `CL` (Chris La Jolla) driving, 
    and `AT` (Alex Triton) navigating.

When you have *all* the tests passing, do one more commit with the commit message `"CL/AT all tests passing"`. 
* Of course, you should use your own initials, not `CL/AT`

### A note about the exclamation point (`!`) in commit messages 
One note: You may be tempted to put exclamation points in your commit messages, because getting the tests to pass is so 
very, very exciting.  If you do, though, you'll have to remember to put a backslash in front of them, like this:
   
```
git commit -m "CL/AT All tests passing \!"
```
    
Otherwise, the bash shell may get confused about the meaning of the `!` symbol, and you'll get this error:

```
[spis16t3@ieng6-240]:spis16-lab02-Alex-Chris:140$ git commit -m "CL/AT All tests passing!"
-bash: !": event not found
[spis16t3@ieng6-240]:spis16-lab02-Alex-Chris:141$
```

We can go into why that's the case some other time (what is this "event" that is not found?)    

For now, though it may be better to just avoid the `!` symbol in your commit messages unless you remember the backslash.

### All tests passing? Then you are done!

Congratulations!  If you still have time, explore [unit testing](https://docs.python.org/3.7/library/unittest.html), extend your code in some other way, read more about the wage gap, or anything else related to this lab!
