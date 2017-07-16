---
layout: lab
num: lab02
ready: false
desc: "Next steps with github, Python functions, testing"
assigned: 2017-08-09 13:15:00.00-7
due: 2017-08-10 17:00:00.00-7
---

If you find typos or problems with the lab instructions, please report them on Piazza

# Overview

The first step  of this lab is something you'll take turns with your pair partner doing individually.  Each of you will 
*set up a github repo in which you'll submit your responses to APS problems* (we provide detailed instructions below).

You can also skip over this step and do it later, if you want to get started with the part you do as a pair.  Please do the APS step, though, sometime today or tomorrow, since you'll need this APS repo to work on your [APS homework aps01](/hwk/aps01/)

Then, as a pair, you'll work through some steps to practice a few skills involving Python, Unix, and github.   


# More specific Learning Objectives

The most important thing we want you to get out of this lab is the ability to
* create a solution to a Python problem for which there are test cases
* iterate until the test cases pass
* keep every step of that development process in a github repo
* then submit that solution for "automatic grading" using a system called Gradescope.

Here's a more complete list of our learning objectives:

* A few Unix commands, including:  `pwd`, `ls`, `cd`, `mkdir`
* Some new options for creating a private github repo for a lab
   * Creating it with a README.md and .gitignore for Python
   * Adding a pair partner as a collaborator.
* How to clone a private repo at the Bash (Unix) command line
* How to store a Python file in that repo
* The basic git workflow of `git add...`, `git commit...`, `git push...`
* Testing of Python functions
* Submitting a Python function for autograding using Gradescope

# Step-by-Step through {{page.num}}

## Step 1: Create a `~/github` directory on your ACMS account

The following article explains how to create a `~/github` directory on your ACMS account.

* [Creating `~/github` and learning some shell commands in the process](/topics/acms_create_github_dir/)

It also covers some basics of the commands you can use at the bash shell prompt&mdash;commands such as
`pwd`, `cd`, `mkdir`, and others that you'll need to know for SPIS (and in your later UCSD CSE courses) for working
with your ACMS account.

If *both* you *and* your pair partner are already thoroughly familiar with Unix command basics&mdash;that is, you know how to create `~/github`, and you are *throughly* familiar with everything in the table below, you can just create ~/mkdir, and skip the tutorial.

But if either or both of you has any doubt, you are strongly encourage to go through this page carefully and slowly,
to learn some of the basics of working with Unix commands at the bash shell.  That is one of the most fundamental skills you'll need throughout all of the courses that use the ACMS unix accounts during your entire stay at UCSD.

I would encourage you to go through the entire tutorial at least once in one pair partner's account, and then repeat it briefly in the second pair partner's account so that each partner has a ~/github subdirectory.

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
| `cd `..`       | Change directory to parent of current directory (go up)         |
| `cd ~/fum`     | Change directory to `fum` inside home directory (`~`)           |

You should also learn the following concepts:

* Home directory (`~`), directory, and subdirectory
* Unix/Linux directory tree, rooted at `/`
* Bash Shell
* Shell prompt

When both partners have a `~/github` directory and are comfortable with shell basics, move on to Step 2.

## Step 2: Create your shared lab02 repo 

There are three steps involved here.  First, I'll give you an overview, and then the details:

1. One of the two pair partners should log into github.com to create an empty private repo *in a particular way*, namely,    pre-populated only with a README.md, and a .gitignore for Python.  
2. The first pair partner will then invite the second to be a collaborator with <b>Admin</b> access.   
3. Finally, the second pair partner needs to accept the invitation to be a collaborator.    


Note: it doesn't matter which pair partner creates the repo&mdash;it can be the one listed first, or the one listed second in the pair name.  For example, if the pair is listed as Alex_Chris in the <b>Pair Name</b> column on the [SPIS 2017 list of pairs](/info/pairs/), it doesn't matter whether Chris creates and then invites Alex, or Alex creates and then invites Chris.   

For purposes of the rest of these insructions, though, I'll refer to "first" as the partner
under whose github account the repo is initially created, and "second" as the partner that gets invited to collaborate.

And regardless of who creates and who invites, *please* name the repo according to the pair order that is listed in the <b>Pair Name</b> column on the [SPIS 2017 list of pairs](/info/pairs/).  That makes it MUCH easier for us to find your work!
   
### Step 2a: Create a private repo with a README.md and a .gitignore file for Python.

Choose which pair partner is going to create the repo&mdash;that pair partner should be the one that is logged into github.com.

To create the repo follow the instructions at the link: [github create repo Method 2](http://ucsd-cse-spis-2017.github.io/topics/github_create_repo/#method2).

As you follow these instructions, create:
* a private github repo under the `ucsd-cse-spis-2017` github organizaiton,
* with the name `spis17-lab02-Name1-Name2` where,
    * `Name1` is the first pair partner's preferred first name
    * `Name2` is the second pair partner's preferred first name

The <b>Pair Name</b> column in the [SPIS 2017 Pairs List](/info/pairs/) page corresponds to this `First-Second` part of your repo name.

An example correct repo name for the ficticious SPIS students Alex Triton and Chris La Jolla would be: 

`spis17-lab02-Alex-Chris`.

### Step 2b: First pair partner invites second pair partner to be a collaborator

The pair partner that created the repo will automatically have access.  That partner needs to invite the second
partner to be a collaborator with admin access.

The instructions to do that are found here: [Github: Adding collaborators](/topics/github_add_collaborators)

### Step 2c: Second pair partner accepts the invitation

The second pair partner should accept the invitation.  This is usually straightforward: there is an invitation in the second pair partner's incoming email with a link to click, and it is clear what to do.

If the email doesn't arrive, though, or anything is not clear, there are troubleshooting instructions later on the same page you accessed in the previous step to add the partner as a collaborator:  
[Github: Adding collaborators](/topics/github_add_collaborators)

## Step 3: One time steps for configurating your ACMS account for git

There are a few steps that we only have to do one time in order to get our ACMS account ready for use with git and github.

Those steps are outlined here.  Please repeat these steps under each pair partner's account.

* [ACMS Account: git/github one-time setup steps](/topics/acms_git_one_time_setup/)

<b>TIME-SAVING TIP:</b> You do not have to log "all the way out" and log back in to be able to do these steps for both pair partners.    Instead, if the first pair partner is logged in, they can just allow the second pair partner to drive for a moment, and ssh into their account from a terminal window.  This article explains how:

* [ACMS: ssh'ing to access another account](/topics/acms_ssh_into_another_account/)
 


## Step 4: Cloning a private repo at the bash (Unix) command line

Next, you need to clone your private repo into the `~/github` directory of one of your ACMS accounts (either one will do.)

The instructions to do that are here: [cloning your first repo](/topics/git_cloning_your_first_repo/).

When you've done that, we are finally ready for some Python programming!

## Step 5:  How to store a Python file in a repo

To review what you've done so far:

* You create a repo called `spis17-lab02-Name1-Name2` on github.com
* You cloned that repo into your ACMS account under the `~/github` directory.
* That means you actually have *two* repos now. 
    * The repo on github.com and the repo on your ACMS account are *separate*, but *linked*
    * More specifically, the one on ACMS points to the one on github.com as its `origin` repo
    
What you will do now is put some Python code into the local repo&mdash;or more precisely, you'll put some Python
code into the directory that corresponds to that repo.   You won't actually commit it to the repo until the next step.

So, what we want to do first is make `~/github/spis17-lab02-Name-Name` (except with your pair's names, not literally `Name-Name`) be your current directory.     Use the `cd` command to make that happen.  

When you've done it, you 
should be able to type `pwd` and see that your current directory path ends in `github/spis17-lab02-Name-Name`, just like in the example output below:

```
[spis17t3@ieng6-240]:spis17-lab02-Alex-Chris:118$ pwd
/home/linux/ieng6/spis17/spis17t3/github/spis17-lab02-Alex-Chris
[spis17t3@ieng6-240]:spis17-lab02-Alex-Chris:119$ 
```

Then, start up IDLE by typing `idle3`:

```
[spis17t3@ieng6-240]:spis17-lab02-Alex-Chris:119$ idle3
```

Once you do, use the `File -> New File` menu item twice to open *two* windows in which you can type Python code.

In the first window, enter this function definition.  This function converts Fahrenheit temperatures to Celsius.

It should make sense to you based on what you've learned about Python functions so far.

```python
# tempFuncs.py
def ftoc(fTemp):
   return (fTemp - 32)*(5.0/9.0)
```

In the second window, enter this code.   Don't just copy and paste it; read through it and try to understand it.

If you would like a more detailed, line-by-line explanation of this code, plus some background on unit testing in general,
read the article [Python: Unit Testing](/topics/python_unittest/).

```python
# test_tempFuncs.py

import unittest
from tempFuncs import ftoc

class Test_tempFuncs(unittest.TestCase):

   def test_ftoc_1(self):
      self.assertAlmostEqual(ftoc(212.0),100.0)

   def test_ftoc_2(self):
      self.assertAlmostEqual(ftoc(32.0),0.0)

   def test_ftoc_3(self):
      self.assertAlmostEqual(ftoc(-40.0),-40.0)

   def test_ftoc_4(self):
      self.assertAlmostEqual(ftoc(67.0),19.4444,places=3)

if __name__ == '__main__':
    unittest.main()      
```

Save each of the files by choosing 'File -> Save' from the Idle menu.  

Save them with the *exact* names: `tempFuncs.py` and `test_tempFuncs.py`.  It is important to get the upper vs. lowercase, and the punctuation correct.

When you save, the save dialog should indicate that they are being saved inside the ~/github/spis16-lab02-Name-Name folder that corresponds to your local github repo (you should see a .git directory already present).   It is important that they are saved there, and not somewhere else.   If you save them in another place, the next few steps of the lab won't work properly.

Onve you have saved both files, with IDLE still open, open a second terminal window and navigate in that window into the `~/github/spis17-lab02-Name-Name` folder, and do an ls command as shown here.  You should see both the files, with names exactly as shown here.

Note that if you also have a .pyc file, that's fine (or if you don't, that's fine too).  You don't need to worry about that one, or remove it.  Files ending in `.pyc` are "compiled Python" code. They are temporary files used to speed up the execution of your Python code.   Mostly, just leave them alone and they'll come and go as needed.  

```
[spis17t3@ieng6-240]:spis17-lab02-Alex-Chris:170$ ls
README.md  tempFuncs.py  tempFuncs.pyc  test_tempFuncs.py
[spis17t3@ieng6-240]:spis17-lab02-Alex-Chris:170$ 
```

### Now try running the test_tempFuncs.py file.

Now, in the window with the `test_tempFuncs.py` file, try selecting "Run -> Run Module" from the menu.

You should get output that looks like this:

```
>>> ================================ RESTART ================================
>>> 
....
----------------------------------------------------------------------
Ran 4 tests in 0.031s

OK
>>> 
```

### What if the names are not exactly right? `mv` and `rm` to the rescue

If the names of your `tempFuncs.py` and `test_tempFuncs.py` are not exactly right, you can use the unix `mv` command, which functions both as a *move* command as as a *rename* command.    The syntax is:

```
mv oldname newname
```

For example to change `temp_funcs.py` to `tempFuncs.py`, you would type:

```
mv temp_funcs.py tempFuncs.py
```

If you end up with extra files, you can use the rm command to delete files you dont want.  For example, to remove the file `temp_Fenks.py` that you perhaps saved by mistake, you can type:

```
rm temp_Fenks.py
```

Ok, so now you have a Python file with a function definition in it, and you have some test cases.

What's next?  We want to get this Python code into your local git repo, and then push the changes up to github.com.


## Step 6:  The basic git workflow of `git add...`, `git commit...`, `git push...`

So, having the code in the directory isn't enough to get it into the git repo.

You actually have to go through a series of two steps to get the code into your local repo, and then
a third step to update the `origin` repo on github.com with that code.

The process is described in two articles: 

* a longer version that goes into more detail: [Git: basic workflow](/topics/git_basic_workflow/)
* a shorter version that is more handy reference: [Git: worflow explained](/topics/git_workflow_explained/)

Essentially, though here's what you are going to do:

1.  Make sure you are in your ~/github/spis16-lab02-Name-Name directory
2.  Type `git status` and read what it says
3.  Type `git add tempFuncs.py test_tempFuncs.py` to *stage* these two files (get them ready to be added to the repo)
4.  Type `git status` and read what it says
5.  Type `git commit -m "ftoc function and tests"` to commit the changes and provide an explanation of what you did
6.  Type `git status` and read the messages
7.  Type `git push origin master` to push the changes from your local repo to the origin repo (on github.com)
8.  Type `git status` and read the messages
9.  Navigate to your repo's page at https://github.com and see that the two files now appear there, along
    with your commit message. You may need to refresh the page if you were already on it.

Congratulations, you've just done your first of many dozens of git commits you'll do during SPIS, and the first
of hundreds or thousands you'll do during your four years at UCSD.

## Step 7: Testing of Python functions

Now, in this case, we had some code that already worked right out of the gate.   But the normal case is that we 

1. Start with a *stub*, and some test cases and make sure they fail.
2. Replace the stub with working code so that the test cases pass.
3. See if there is any way to refactor the code to improve it.

In this step, you'll:

* add a stub for a second function to the `tempFuncs.py` file
    * after doing so, you'll commit this change to practice the sequence:
        ```
        git add ... ; git commit -m "message"; git push origin master
        ```
* add some additioal test cases
    * you'll commit this change too with the same sequence:
        ```
        git add ... ; git commit -m "message"; git push origin master
        ```
* see the test cases fail
    * you won't have to commit at this step, because you won't have changed anything
* then add code to make the tests cases pass
    * You guessed it: yet another round of
        ```
        git add ... ; git commit -m "message"; git push origin master
        ```

Ok, so let's get started:



## Step 7a: Add a stub for `ctof(cTemp)` to `tempFuncs.py`

Add a stub for a second function to the `tempFuncs.py` file by adding this code to the file:

```
def ctof(cTemp):
   return "stub"
```

This code is "always" the wrong answer, so it should fail every test.  That's what we want from a stub. It helps us
"test the test" to make sure that it is successful at detecting bad code.

After adding this code, save the file `tempFuncs.py`.  Then at the command prompt, inside the ~/github/spis16-lab02-Name-Name` direcory, type:

* `git status`
* `git add tempFuncs.py`
* `git status`
* `git commit -m "stub for ctof"`
* `git status`
* `git push origin master`
* `git status`
 
Then check the repo's page on github.com to see that the changes appear.

## Step 7b: Add import, and test cases for `ctof` to `test_tempFuncs.py`
        
Next, edit the `test_tempFuncs.py` file in IDLE3, and after the line

```
from tempFuncs import ftoc
```

add this line:

```
from tempFuncs import ctof
```

This line is needed so that we can pull the definition of `ctof` from the file `tempFuncs.py` and run our tests
on it.    

Now add some test cases for the cToF function.   
* You simply add the function definitions for these test cases immediately below the ones for
fToC.    
* Be sure they are indented inside the `class`, just like the ones for `ftoc`.
* Also, be sure that each one has a different name from all of the others.

I'll give you the first one, but the rest you must come up with on your own:

```
   def test_ctof_1(self):
      self.assertAlmostEqual(ctof(100.0),212.0)
```

Add at least four more so that you have a total of five tests.

Once you are done and saved the file, its time to commit the changes:

* `git status`
* `git add test_tempFuncs.py`
* `git status`
* `git commit -m "tests for ctof"`
* `git status`
* `git push origin master`
* `git status`

Then check the repo's page on github.com to see that the changes appear.

## Step 7c: See the test cases fail

Now, run the test cases by selecting "Run -> Run Module" from the menu in the window for `test_tempFuncs.py`.

What you want to see is that the test cases for ftoc passed, but that the ones you added for ctof fail.
In general, test cases where you have a "stub" function should fail either because:

* the expected output didn't equal "stub", or
* in the case of `assertAlmostEqual`, a message like this:
    ```
    TypeError: unsupported operand type(s) for -: 'float' and 'str'
    ```
The second type of error comes because the `assertAlmostEqual` function tries to subtract the expected result from the actual result, and then take the absolute value.  It can't subtract from a string value such as `"stub"`, hence the error.

You could also use a stub with a value of something like `return -99999.999` if you like; then you'll get a slightly
different error, but the test will still fail&mdash;which is want you want for a stub. Note that this case is reported as a 'failure' rather than an 'error'.

### Are the tests *failing* the expected way?

If the tests are failing in the way we are *hoping for*, you can move on to the next step.

If on the other hand, there were *errors of another kind* (e.g. indentation errors, missing :, etc.) then you'll want to 
fix those.  And if that involves change either, or both of the two files, you'll want to do another round of the steps to do a commit.

If the commit involves changes to both files, you can combine those into a single commit.  Here's how:

* EITHER:  `git add tempFuncs.py` followed by a separate `git add test_tempFuncs.py` 
* OR: `git add *.py` which adds all files ending in .py from the current directory to the next commit (but only if they      are new or have changed.)
* Then continue with the `git status`, git commit...` as before.

## Step 7d: Replace the stub in `ctof` with correct code so that the tests pass

Now, you should write a correct version of the ctof function so that tests pass.

That will be a line of code that starts with `return` and ends with an expression involving the variable
`cTemp`, and some math operations to convert that to an equivalent Fahrenheit value. 

Try running the tests, and when all of your tests pass, you are ready to commit.  What you are looking for is this:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```

If you get part-way done, and *some* of your tests pass, but not others, or you are in the middle of working
when it is time for a break, that is STILL a good time to do a commit.   Add the letters "WIP" to the start of your
commit message so you know that this is not a finished product.  "WIP" stands for "Work in Progress".  For example:

```
git status
git add tempFuncs.py
git status
git commit -m "WIP CL/AT  Some ctof tests passing, others failing"
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

### All tests passing? Then you are almost done!

Congratulations!  You are *almost* finished.   The last step involves submitting your code for "automatic grading".
This way, you can be (reasonably) sure that you did the assignment correctly.

## Step 8:  Submitting a Python function for autograding using Gradescope

### Step 8a: Login to gradescope and find lab02

The first step is to open up Gradescope, and find lab02.

Navigate to gradescope.com and login.

Your login id is your `____@ucsd.edu` email address, with the full `@ucsd.edu` at the end.

You may have received an email to retrieve your password, or you might need to ask that the password reset email
be resent.

Once you are logged in, locate the place to submit lab02.  It should ask you to upload a .zip file with your submission.

### Step 8b: Generate a .zip file for your submission

As long as you have pushed all of your changes to github.com, generating a .zip file for your submission is easy.

Just navigate to the page for your repo, use the "Clone or download" button, and then the "Download zip" button, as shown in the image below:

![Download zip](github-download-zip-for-gradescope-50.png)

### Step 8c: Upload the zip, and wait for the results

Upload the zip and wait for the results: hopefully a perfect 100%.

And that's it for lab02!


If you have difficulties with the Gradescope submission, ask a mentor or instructor for assistance.
