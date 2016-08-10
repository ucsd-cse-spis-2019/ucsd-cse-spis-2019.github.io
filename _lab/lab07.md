---
layout: lab
num: lab07
ready: false
desc: "Python skill builder (functions, types, if/else, strings, recursion)"
assigned: 2016-08-16 08:45:00.00-7
due: 2016-08-18 14:45:00.00-7
starter-code-url: https://github.com/FILL-IN-THIS-URL-WITH-STARTER-CODE-URL
---

If you find typos or problems with the lab instructions, please report them on Piazza

# What you'll do in this lab

This lab is intended to be an opportunity to review, reinforce, and build your confidence with basic programming
skills.

Before we move into more advanced labs and projects, we want to give you an opportunity to be sure that your
understanding of the following is solid.

* Simple python functions
* Working with if/else
* Working with types in Python
* Python Strings
* Loops
* Recursion

So, we've set up a series of files that contain stubs for various Python functions, along with
tests for those functions.

Your job is very simple: see if you replace each of the stubs with code that passes the tests that go along with that
file.

When you are finished, you can submit your solution to Gradescope for automatic "grading".  (Keep in mind that in SPIS, 
all so-called "grades" are just a way to get feedback on how you are doing.  They don't "count" on your permanent record in any way.  Treat them as "practice" grades.)

# Overview 

The basic structure of the lab is similar to [lab02](/lab02), except for the one-time steps from that lab, and the 
fact that the repo you create will begin with some starter code (so that step will look a little different than before.)

After creating the repo, you'll `git clone ... ` the repo, and then start editing Python code, trying to get
test cases to pass.

Each time you get one more test case to pass, or each time you need to take a break from coding, be sure to do the
`git add file.py ; git commit -m "AB/CD message"; git push origin master` steps.   

The instructions below will give you some additional hints about each of the functions that you'll be writing,
including hints, references to help articles on the website, and/or suggestions of relevant passages in the text.

When all done, and all test cases are passing, you'll download your project as a `.zip` file and submit to
Gradescope for automatic checking of all your test cases.

Ok, let's get started!

# Step-by-Step Instructions

# Step 1: Create your repository.

The way that you create the repo will be a little different, since we have "starter code" available for you.

Instead of creating the repo from scratch, you'll set up the repo with [Method 1](http://ucsd-cse-spis-2016.github.io/topics/github_create_repo/#method1),
importing the starter code from this link:  {{page.starter-code-repo}}

The name of your repo should be `spis16-`<tt>{{page.num}}</tt>`-Name1-Name2` where the `Name1-Name2` part matches the *Pair Name* column of the [Pairs table from the SPIS FOCS Website](http://ucsd-cse-spis-2016.github.io/info/pairs/)

# Step 2: Invite the "other" pair partner as a collaborator with admin access

The pair partner that created the repo needs to invite the second pair partner to be a collaborator on the repo with Admin access.   That process is explained here: [Github: Adding Collaborators](http://ucsd-cse-spis-2016.github.io/topics/github_add_collaborators/)

# Step 3: cd into the ~/github directory of your 

You should have created a `~/github` directory during a previous lab.

So use `cd ~/github` to cd into this directory.  If it works, skip down to the next step.

## What if that directory doesn't exist yet?

It is possible, if you are working in the 
other pairs ACMS account, that they don't have one yet.

The fastest way to create that directory and `cd` into is to simply type these commands.  

```bash
$ mkdir -p ~/github
$ cd ~/github
```

Two notes on this:

* Here the `$ ` is standing in for the bash shell prompt, which on ACMS machines is typically something
    long such as `[spis16t3@ieng6-240]:~:179$ `.   Since
    the exact content of the bash shell prompt differs from system to system, or even user to user, it is traditional
    to just show it as `$` in documentation.  (By the way, you can customize your shell prompt, but that's a 
    story for another time.)

* The `-p` after `mkdir` stands for *path*.   When you use `mkdir -p path` instead  of just `mkdir path` you get two
    benefits:
    1.  If the path you are creating, e.g. `~/github` already exists, `mkdir -p` doesn't complain
    2.  You can create a long path all at once, e.g. `mkdir -p ~/foo/bar/fum/fiddle` will create that entire
        chain of directories with one command.  Without the `-p`, you can only create one directory at a time,
        so it would have to be `mkdir ~/foo`, then ``mkdir ~/foo/bar`, then `mkdir ~/foo/bar/fum`, etc.

# Step 4: Use `git clone repos-clone-ssh-url` to clone your repo

Use the command `git clone ` *repos-clone-ssh-url* to clone your new repo.

If you've forgetting where to get the *repos-clone-ssh-url*, consult the page: [git: cloning your first repo]/topics/git_cloning_your_first_repo/)

# Step 5: cd into your repo's directory, and open idle

If you type `cd ~/github/spis16-`<tt>{{page.num}}</tt>` and then press the *tab* button, the bash shell should
auto-complete the name of your repo (i.e. automatically finish the `-Name1-Name2` part.  You can then press enter
and be in the correct directory.

Use the commands `pwd`, `ls`, and `git status` to be sure you are in the right spot.

Then, open idle by typing `idle &` at the bash command prompt.  The extra `&` at the end allows you to get your
command prompt back so that you can use it to type git commands.  You may see messages from time to time from 
IDLE&mdash;if so, just press enter to get a bash prompt back again.

If you forget the `&`, no worries.  You can also just open a second terminal window for typing your `git` commands.

# Step 6: Python coding.

In this step you will work, one file at a time, trying to replace the function stubs in each file with running code.

The process consists of:
* choosing a Python file to work on, e.g `pyfuncs01.py`
* running its tests e.g. `test_pyfuncs01.py`
* seeing the tests fail
* then replacing the stubs in `pyfuncs01.py` with correct code so that the tests pass
* doing the git workflow to commit your changes, e.g. for `pyfuncs01.py`:
    * `git status`
    * `git add pyfuncs01.py`
    * `git status`
    * `git commit -m "AT/CL tests passing for pyfuncs01.py`
    * `git status`
    * `git push origin master`
    * `git status`
    
You'll repeat this process for each of the files pyfuncs01.py, pyfuncs02.py, etc.

* As a reminder, the `CL/AT` is used to indicate that you were working as a pair, with:
    * `CL` (Chris La Jolla) driving (driver's initials first)
    * `AT` (Alex Triton) navigating (navigator's initials second).
    * Of course, you should use your own pair's initials, not `CL/AT`
    
* When you have *all* the tests passing,<br> do one more commit with the commit message `"CL/AT all tests passing"`. 

For each, there some additional hints below.

# TODO: Insert additional hints here


# Step 7: Final check of all your tests

As one last check, run all of your tests in IDLE, or at the command line.

TODO: Insert instructions

# Step 8: Submit your solution on Gradescope

Navigate to gradescope.com and login.

Your login id is your `____@ucsd.edu` email address, with the full `@ucsd.edu` at the end.

You may have received an email to retrieve your password, or you might need to ask that the password reset email
be resent.

Once you are logged in, locate the place to submit  {{page.num}}.  It should ask you to upload a .zip file with your submission.

### Step 8b: Generate a .zip file for your submission

As long as you have pushed all of your changes to github.com, generating a .zip file for your submission is easy.

Just navigate to the page for your repo, use the "Clone or download" button, and then the "Download zip" button, as shown in the image below:

![Download zip](github-download-zip-for-gradescope-50.png)

IMPORTANT: If your browser give you the option to: either (a) open the downloaded .zip file or (b) save it to disk,
you *need to select SAVE TO DISK*.   

If you open the downloaded .zip file, it may change the structure to one that the Gradescope autograder is not expecting.

The Gradescope autograder expects a .zip file with the name `spis16-`<tt>{{page.num}}</tt>`-Name-Name-master.zip` that contains the Python files that were in your starter code repo.    If you change the names of functions, or of the files,
things may not work correctly.

### Step 8c: Upload the zip, and wait for the results

Upload the zip and wait for the results: hopefully a perfect 100%.

And that's it for {{page.num}}!





