---
layout: lab
num: lab02
ready: true
desc: "Next steps with GitHub, Python functions, testing"
assigned: 2019-08-07 13:15:00.00-7
due: 2019-08-12 17:00:00.00-7
---

If you find typos or problems with the lab instructions, please report them on Piazza.

# Overview

The main purpose of this lab is to practice, as pairs, a few skills involving Python, Linux, and GitHub.

# Partner structure for {{page.num}}

For this lab, you will work together with your pair partner. The only exception is the first task, where you familiarize yourself with Linux/Unix.

# More specific Learning Objectives

The most important thing we want you to get out of this lab is the ability to ...
* create a solution to a Python problem 
* iterate until your solution produces the correct behavior on a wide range on inputs
* keep every step of that development process in a GitHub repo


Here's a more complete list of our learning objectives:

* A few Unix commands, including:  `pwd`, `ls`, `cd`, `mkdir`
* Some new options for creating a private GitHub repo for a lab
   * Creating it with a `README.md` and `.gitignore` for Python
   * Adding a pair partner as a collaborator.
* How to clone a private repo at the Bash (Unix) command line
* How to store a Python file in that repo
* The basic git workflow of `git add...`, `git commit...`, `git push...`
* Testing of Python functions


# Workflow Step-by-Step

## Step 1: Create a `~/github` directory on your ETS (i.e. "lab") account

This step is the only part of the lab you will do individually. However, you should work next to your partner, making sure you both understand what you are doing.

The following article explains how to create a `~/github` directory on your ACMS account. Note that the name of the directory you create actually does not need to be `github`. The entire process of creating git repos and pushing these to github is not impacted by the name of the directory where the repos are in. Instead of `~/github`, you could have created, for example, `~/SPISlabs` and use that as the directory to store your lab files in. If you are confident or adventurous (and yes, who doesn't want to be confident or adventurous), we recommend you actually pick a different name, to force you to think more about what you are doing, rather than simply copying our directions (as you need to really understand *why* you are doing things).


* [Creating `~/github` and learning some shell commands in the process](/topics/acms_create_github_dir/)

It also covers some basics of the commands you can use at the bash shell prompt&mdash;commands such as
`pwd`, `cd`, `mkdir`, and others that you'll need to know for SPIS (and in your later UCSD CSE courses) for working
with your ETS account.

If *both* you *and* your pair partner are already thoroughly familiar with Linux/Unix command basics&mdash;that is, you know how to create `~/github`, and you are *throughly* familiar with everything in the table below, you can just create `~/github`, and skip the tutorial.

But if either or both of you has any doubt, we strongly encourage each of you to go through this page carefully and slowly,
to learn some of the basics of working with Linux/Unix commands at the bash shell.  That is one of the most fundamental skills you'll need throughout all of the courses that use the ACMS Unix accounts during your entire stay at UCSD.

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

For the remainder of this lab, you will be working directly with your pair partner. Follow the driver-navigator model and switch roles frequently.

For step 2 of our workflow, there are three tasks.  We will explain each of these in detail shortly. But to give you an idea of the process at a high level, we've listed the three tasks you will be asked to do, below:

1. One of the two pair partners should log into [GitHub](https://github.com) to create an empty private repo *in a particular way*, namely, pre-populated only with a `README.md`, and a .`gitignore` for Python.  
2. The first pair partner will then invite the second to be a collaborator with **Admin** access.   
3. Finally, the second pair partner needs to accept the invitation to be a collaborator.    


Note: it doesn't matter which pair partner creates the repo—it can be the one listed first, or the one listed second in the pair name.  For example, if the pair is listed as Alex_Chris in the **Pair Name** column on the [SPIS 2019 list of pairs](/info/pairs/), it doesn't matter whether Chris creates and then invites Alex, or Alex creates and then invites Chris.   

For purposes of the rest of these instructions, though, we'll refer to "first" as the partner
under whose GitHub account the repo is initially created, and "second" as the partner that gets invited to collaborate.

And regardless of who creates and who invites, *please* name the repo according to the pair order that is listed in the **Pair Name** column on the [SPIS 2019 list of pairs](/info/pairs/).  That makes it MUCH easier for us to find your work!
   
### Step 2a: Create a private repo with a `README.md` and a `.gitignore` file for Python.

Choose which pair partner is going to create the repo&mdash;that pair partner should be the one that is logged into github.com.

To create the repo follow the instructions at the link: [GitHub create repo Method 2](http://ucsd-cse-spis-2019.github.io/topics/github_create_repo/#method2) (make sure the repo you create is a private repo).

As you follow these instructions, create:
* a **private** github repo under the `ucsd-cse-spis-2019` GitHub organization,
* with the name `spis19-lab02-Name1-Name2` where,
    * `Name1` is the first pair partner's preferred first name
    * `Name2` is the second pair partner's preferred first name

The **Pair Name** column in the [SPIS 2019 Pairs List](/info/pairs/) page corresponds to this `First-Second` part of your repo name.

An example correct repo name for the ficticious SPIS students Alex Triton and Chris La Jolla would be: 

`spis19-lab02-Alex-Chris`.

### Step 2b: First pair partner invites second pair partner to be a collaborator

The pair partner that created the repo will automatically have access.  That partner needs to invite the second
partner to be a collaborator with admin access.

The instructions to do that are found here: [GitHub: Adding collaborators](https://ucsd-cse-spis-2019.github.io/topics/github_add_collaborators)

### Step 2c: Second pair partner accepts the invitation

The second pair partner should accept the invitation.  This is usually straightforward: there is an invitation in the second pair partner's incoming email with a link to click, and it is clear what to do.

If the email doesn't arrive, though, or anything is not clear, there are troubleshooting instructions later on the same page you accessed in the previous step to add the partner as a collaborator:  
[GitHub: Adding collaborators](https://ucsd-cse-spis-2019.github.io/topics/github_add_collaborators)
 

## Step 3: Cloning a private repo at the bash (Linux/Unix) command line

Next, you need to clone your private repo into the `~/github` directory of one of your ACMS accounts (either one will do.)

The instructions to do that are here: [cloning your first repo](/topics/git_cloning_your_first_repo/).

When you've done that, we are finally ready for some Python programming!

## Step 4:  How to store a Python file in a repo

To review what you've done so far:

* You created a repo called `spis19-lab02-Name1-Name2` on GitHub
* You cloned that repo into your ACMS account under the `~/github` directory.
* That means you actually have *two* repos now. 
    * The repo on GitHub and the repo on your ACMS account are *separate*, but *linked*
    * More specifically, the one on ACMS points to the one on GitHub as its `origin` repo
    
What you will do now is put some Python code into the local repo—or more precisely, you'll put some Python
code into the directory that corresponds to that repo.   You won't actually commit it to the repo until the next step.

So, what we want to do first is go into the `~/github/spis19-lab02-Name-Name` (except with your pair's names, not literally `Name-Name`) directory.     Use the `cd` command to make that happen.  

When you've done it, you 
should be able to type `pwd` and see that your current directory path ends in `github/spis19-lab02-Name-Name`, just like in the example output below:

```
[spis19t3@ieng6-240]:spis19-lab02-Alex-Chris:118$ pwd
/home/linux/ieng6/spis19/spis19t3/github/spis19-lab02-Alex-Chris
[spis19t3@ieng6-240]:spis19-lab02-Alex-Chris:119$ 
```

Then, launch gVim by typing `gvim`:

```
[spis19t3@ieng6-240]:spis19-lab02-Alex-Chris:119$ gvim
```

Now create a new file and in it paste the Python code below. This process was explained in lab00. If you don't remember exactly how you did it, just have another look at that lab assignment. 

```python
# The goal of this program is to practice Python constructs
def sumTwo(a,b):
   c = a + b
   return c

x = sumTwo(3,5)
print(x)
```

Save the file as `testSum.py`. When you save the file, make sure you save it inside the `~/github/spis19-lab02-Name-Name` folder that corresponds to your local GitHub repo. It is important that it is saved there, and not somewhere else.  If you save it in another place, the next few steps of the lab won't work properly.

Have a look at the code. It consists of a function that returns the sum of two input arguments; this function is called and the result is printed. This should make sense to you based on what you've learned about Python so far.

Now let's run the program. Open a second terminal window and navigate to the `~/github/spis19-lab02-Name-Name` folder. Before we run the code, however, let's quickly double check the file is indeed there. Run the `ls` command as shown below.  You should see your file.


```
[spis19t3@ieng6-240]:spis19-lab02-Alex-Chris:170$ ls
README.md  testSum.py
[spis19t3@ieng6-240]:spis19-lab02-Alex-Chris:170$ 
```

In the same terminal window, run your code by calling `python testSum.py` (or using `python3` instead of `python`). Is your output what you expect?

What's next?  We want to get this Python code into your local git repo, and then push the changes up to GitHub.




## Step 5:  The basic git workflow of `git add...`, `git commit...`, `git push...`

So, having the code in the directory isn't enough to get it into the git repo.

You actually have to go through a series of two steps to get the code into your local repo, and then
a third step to update the `origin` repo on GitHub with that code.

The process is described in two articles: 

* a longer version that goes into more detail: [Git: worflow explained](/topics/git_workflow_explained/)
* a shorter version that is more handy reference: [Git: basic workflow](/topics/git_basic_workflow/)

Essentially, here's what you are going to do:

1.  Make sure you are in your `~/github/spis19-lab02-Name-Name` directory
2.  Type `git status` and read what it says
3.  Type `git add testSum.py` to *stage* this file (get it ready to be added to the repo)
4.  Type `git status` and read what it says
5.  Type `git commit -m "testSum added; functionality verified"` to commit the changes and provide an explanation of what you did (you can modify the text between " " as you see fit)
6.  Type `git status` and read the messages
7.  Type `git push origin master` to push the changes from your local repo to the origin repo (on github.com)
8.  Type `git status` and read the messages
9.  Navigate to your repo's page on [GitHub](https://github.com) and see that the two files now appear there, along
    with your commit message. You may need to refresh the page if you were already on it.

Congratulations, you've just done your first of many dozens of git commits you'll do during SPIS, and the first
of hundreds or thousands you'll do during your four years at UCSD.



# Python Challenges

Now that you have gone through the workflow (creating a repo, cloning it, adding files, committing those to git and then pushing them to github), it is time to do some more coding.

Since we are still doing lab02, we will be putting all our files in the same directory as before. So make sure you are still in  `~/github/spis19-lab02-Name-Name`. Remember, you can check this using the `pwd` command. If you are not in this folder, navigate there using `cd`.


## Adding another function

Open your existing file, `testSum.py`, in gVim. You can do this by launching gVim as before, and then go to File -> Open. Alternatively, you can type `gvim testSum.py` on the commnand line to open gVim with this file automatically loaded.
Once you have opened the file, add a new function: `getNumber`, as shown below (you keep all the other text that you already have in this file; just add this new function at the top). 


```python
def getNumber():
   symbols = input("Enter a digit: ")
   number = int(symbols)
   return number

```

Let's go over this code together. The first line inside `getNumber()` uses the built-in Python function `input()` to ask the user to type in something.  This could be a single symbol (e.g., 'a'), a word (e.g., 'apple') or even an entire novel. You can keep typing until you hit the Return/Enter key. We will assume the user only types in a single decimal digit (so one of '0','1', ... '9'), as this is what we asked the user to do (in the text that is between " " in the `input`-function). 

However, Python interprets whatever is returned by the `input`-function as a *string*. A string is basically a collection of symbols. Since we only entered a single character ('0', '1', .. '9'), this string would be a single symbol. The `int()`-function is used to convert this symbol to a corresponding number (if this is possible). For example, the symbol (letter) '1' gets converted to the number 1. Why is this necessary? Well, even though they look the same to us, a computer needs to know whether you are talking about a symbol or a number, as it treats those differently. For example, it can multiply the number 1 by two, but what would it even mean to multiply the symbol '1' by two? This is why we had to use the `int`-function to convert from a symbol to a number. Finally, now that we have a number, it is returned by the function.

Now, your task is to modify the `getNumber` function. It should repeatedly ask the user to enter a single digit, instead of only once. This means that you probably want to put the bit of code that asks for a user input in some kind of loop (remember `while` from lecture?) The number that is returned at the end of the function should be the combination of these individual digits. For example if the user enters 4, then 7, then 0 and then 9, the function should return the **number** 4709.
You may wonder, if we are putting the user input inside a loop, how do we know when to stop? We will assume that as soon as the user answers with a number that is negative, you can stop asking (and ignore this negative number). So in the example above, the user would really enter 4, then 7, then 0, then 9 and then -1 (or any other number). 

When you think you have your function, or even part of it, written, you should also test it. To do this, call the function in your code. This is similar how we called `sumTwo` in `testSum`. Test your function thoroughly to convince yourself it works correctly. Once this is done, you are ready to "push" your changes to github.  

1.  Type `git status` and read what it says. You have made changes to a file. Did git notice? What is it telling you?
2.  We saw earlier that the first step in the git workflow was to execute a `git add`. However, in this case, you have modified a file that was already added to git tracking, so you don't need to do it again. You only need to do a `git add` on a file that you did not track before. However, it won't hurt if you do it again, so you might as well, just to be sure.
3.  Type `git status` and read what it says. Did it change? Why/why not?
4.  Type `git commit -m "xxx"` to commit the changes. However, replace xxx by a brief explanation of the additions/changes you made to the code (e.g., "new function bar added to file foo"). Remember, you want to make these git commit messsages meaningful. 
5.  Type `git status` and read the messages
6.  Type `git push origin master` to push the changes from your local repo to the origin repo (on github.com)
7.  Type `git status` and read the messages
8.  Navigate to your repo's page on [GitHub](https://github.com) and see that the two files now appear there, along with your commit message. You may need to refresh the page if you were already on it.




## Adding yet another function

You are going to add one more function to `testSum.py`, called `sumDigits`. This function should take a single parameter, which is a multi-digit number. The result it returns is the sum of the digits of this number. For example `sumDigits(236)` should return 11.

```python
def sumDigits(x):
   # You will need to complete this function
   return sum
```

Complete the code for this function. Two useful operations here are `%` (modulo; which returns the remainder of a division) and `//` (integer division; which divides the number and rounds it to the nearest integer). For example, 11//2 is 5 and 11%2 is 1. 

Now you need to come up with an algorithm that lets you extract each individual digit from a number, so you can add these together. We will give you some hints, but it's good to try and figure out the algorithm without them. Brainstorm with your partner. Don't think about it on your own and then explain to the other person. Just start talking ... let the ideas flow and see if you can really think together. This is a good exercise to get you in the habit to do this throughout your pair programming exercises. If one partner already knows the answer (maybe you've seen it somewhere before), don't simply tell the other person. Let them figure it out gradually.

After you've realy thought about it and you need some help, here are some hints. First, think about how you can use division and/or modulo to get the *least significant* (i.e., right-most) digit of a number. So, how can you extract 6 from 236? It is helpful to consider that our number system uses base 10 (hence the name "decimal"). Once you have that, how can you get the number that would result from chopping of the least significant digit? So, how can you get 23 from 236? If you are able to do this, how can you get the next digit? Is there a repeating pattern here? This would suggest once again ... a loop.

Once you have figured out the answer, test your function for a few different values to convince yourself it works correctly. When you are done and your code works correctly, push the updated file to github (as we did for the previous function you added). Verify on github that indeed all your updates got pushed online!



# More Python Practice

For this last part, we are going to explore a bit more how you can approach testing your Python code ... and give you a few more open ended coding challenges. 

## Exploring our base code

Create a new file in gVim and type (or copy/paste) this function definition. Save the file as `wageCalculator.py`. Again, make sure you save it in the `~/github/spis19-lab02-Name-Name` folder.

```python
# wageCalculator.py
def convertWageMtoW(mWage):
   wageGap = 0.182
   ratio = 1-wageGap
   return mWage/ratio
```

This function uses the the gender wage gap in the United States to calculate a woman's wage based on the corresponding male wage.  The wage gap is defined as the difference between a man's salary and a woman's salary, expressed as a percentage of a man's salary.  In the United States the wage gap is 18.2%.  To calculate a woman's salary, given a man's salary using the wage gap we can multiply the man's salary by 1-wageGap.  You can learn more about the wage gap and see more data [here](https://data.oecd.org/earnwage/gender-wage-gap.htm).


To verify our code is correct, we need to test it, as we did before. More formally, this means that we need to define test cases. A test case is a combination of an input and the expected output. The first step to testing is to define these input-output pairs.  We can use a calculator to do this, for example:

* men's wage of 100 should output 81.8
* men's wage of 76.2 should output 62.3316
* men's wage of 0 should output 0.0

It's good to try a range of inputs that are qualitatively different.  Notice in the test cases above, we have selected one non-zero integer input, one decimal number and the number 0.

Add code to the program to verify these cases, and make sure  the output is as you expect. If the cases do not give you the correct expected output, figure out what is wrong.

Now add two more test cases of your own.

When doing this testing, you might find that your implementation returns values that are *almost* correct, e.g. 0.000000000000000000001 for 0.0 or something similar.  This is due to imprecision in the way Python represents floating point numbers and is completely normal.  You should consider your results correct if they "very close" to the expected results.

What's next? As before, you need to get this Python code into your local git repo, and then push the changes up to GitHub. Again, follow the procedure you've learned. Note that when doing a "`git add`" followed by the filename, you can instead do "**`git add .`**", where the dot signifies "all the files". This is a very convenient shortcut. When you have pushed your changes, verify that they indeed appear in your online github repo!


## Adding (and testing) additional functionality to your wage converter

Now, extend the functionality of your wageCalculator function so that:

* It takes at least one additional parameter
* It uses an if-statement (or if-else statement, or if-elif-else statement, etc) in its functionality

You can use the data on [this page](https://data.oecd.org/earnwage/gender-wage-gap.htm), or any other data you find on the web in your functions.

Exactly what your extended function does is up to you and your partner, but it should still be focused on calculating salaries based on the gender wage gap.  Here are some ideas for extensions, but feel free to come up with your own:
* Add race/ethnicity information to the calculator.  For example, the calculator might take an additional parameter, which is race, and calculate the salary of a woman of that race, assuming the wage input is for a man of that same race (or alternatively the wage of a white man).
* Add a country parameter, and calculate salaries differently based on wage gaps in different countries.

### Comment your code
In a comment above your modified function, make sure you describe what it does.  Include a description of what each parameter means, and what is returned.

### Test your code
Come up with several test cases.  If any of your test cases fail, fix your code so that they pass.  Make sure you test enough cases so that you are confident your code works in all cases.  For example, if you take a country name as one of your parameters, what happens if the user enters a country your code does not know about?  Does it behave as you expect?

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
[spis19t3@ieng6-240]:spis19-lab02-Alex-Chris:140$ git commit -m "CL/AT All tests passing!"
-bash: !": event not found
[spis19t3@ieng6-240]:spis19-lab02-Alex-Chris:141$
```

We can go into why that's the case some other time (what is this "event" that is not found?)    

For now, though it may be better to just avoid the `!` symbol in your commit messages unless you remember the backslash.

### All tests passing? Then you are done (kind of) ..

Congratulations! You are done with this lab, but consider some of the additional challenges below ...


# Challenge Problem: Implement the Hangman game 
Even though you just started learning Python, you already have all the knowledge required to implement a fun little game, such as [hangman](https://www.coolmathgames.com/0-hangman). The goal of this game is to guess a word or phrase, by asking if a letter appears in it. You win by guessing all the letters before you made 7 mistakes (i.e., asked for a letter that did not appear). You can try out the game [here](https://www.coolmathgames.com/0-hangman).




# Additional Challenges 
If you still have time, you can explore [unit testing](https://docs.python.org/3.7/library/unittest.html), which is a more formal testing strategy. You can also extend your code in some other way, read more about the wage gap, or anything else related to this lab!
Or do some more picobot ...



