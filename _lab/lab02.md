---
layout: lab
num: lab02
ready: false
desc: "lab02, Next steps with github, Python functions, testing"
assigned: 2016-08-05 08:45:00.00-7
due: 2016-08-09 15:45:00.00-7
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
| `cd ~/fum`     | Change directory to `foo` inside home directory (`~`)           |

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


Note: it doesn't matter which pair partner creates the repo&mdash;it can be the one listed first, or the one listed second in the pair name.  For example, if the pair is listed as Alex_Chris in the <b>Pair Name</b> column on the [SPIS 2016 list of pairs](/info/pairs/), it doesn't matter whether Chris creates and then invites Alex, or Alex creates and then invites Chris.   

For purposes of the rest of these insructions, though, I'll refer to "first" as the partner
under whose github account the repo is initially created, and "second" as the partner that gets invited to collaborate.

And regardless of who creates and who invites, *please* name the repo according to the pair order that is listed in the <b>Pair Name</b> column on the [SPIS 2016 list of pairs](/info/pairs/).  That makes it MUCH easier for us to find your work!
   
### Step 2a: Create a private repo with a README.md and a .gitignore file for Python.

Choose which pair partner is going to create the repo&mdash;that pair partner should be the one that is logged into github.com.

To create the repo follow the instructions at the link: [github create repo Method 2](http://ucsd-cse-spis-2016.github.io/topics/github_create_repo/#method2).

As you follow these instructions, create:
* a private github repo under the `ucsd-cse-spis-2016` github organizaiton,
* with the name `spis16-lab02-Name1-Name2` where,
    * `Name1` is the first pair partner's preferred first name
    * `Name2` is the second pair partner's preferred first name

The <b>Pair Name</b> column in the [SPIS 2016 Pairs List](/info/pairs/) page corresponds to this `First-Second` part of your repo name.

An example correct repo name for the ficticious SPIS students Alex Triton and Chris La Jolla would be: 

`spis16-lab02-Alex-Chris`.

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

TBD

## Step 5:  How to store a Python file in a repo

TBD

## Step 6:  The basic git workflow of `git add...`, `git commit...`, `git push...`

TBD

## Step 7: Testing of Python functions

TBD

## Step 8:  Submitting a Python function for autograding using Gradescope

TBD
