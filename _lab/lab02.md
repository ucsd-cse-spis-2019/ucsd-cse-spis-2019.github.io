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

* A few Unix commands: `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `rmdir`, `rm`
* How to clone a private repo at the Bash (Unix) command line
* How to store a Python file in a repo
* The basic git workflow of `git add...`, `git commit...`, `git push...`
* Testing of Python functions
* Submitting a Python function for autograding using Gradescope

# Step-by-Step through {{page.num}}

## Step 1: Bring up a bash terminal shell

Bring up a bash terminal shell.  As a reminder, you can do this by selecting "Applications", then either "Terminal" or "Konsole" from the menu that pops up.  (Your Applications menu may have only Terminal, or only Konsole, or may have both.
For our purposes, they work equally well.)

### The bash prompt, date, `~` for home directory, and `history`

On the ACMS machines the bash terminal prompt typically looks like this:

```
[spis16t3@ieng6-240]:~:32$ 
```

It is called a *prompt* because it *prompts* you to enter some a command.  One of the most basic commands you can enter is
the `date` command.  Try it: type in `date` and press return *Enter*.

```
[spis16t3@ieng6-240]:~:32$ date
Thu Aug  4 13:56:29 PDT 2016
[spis16t3@ieng6-240]:~:33$ 
```

The date is printed, and you get a new prompt.  Note that the last number in that prompt keeps increasing by 1.   These numbers refer to your "command history".  If you type the command `history`, you'll see a list of all the recent commands you have typed.  Try it:

```
[spis16t3@ieng6-240]:~:33$ history
    1  idle
    2  idle
    3  pwd
```
(I left some out here...)
```
   31  exit
   32  date
   33  history
[spis16t3@ieng6-240]:~:34$ 
```

You can see that the next command I type will be "number 34" in my history.

### Your account and machine in the prompt

There are a few others parts of the prompt.  
* The `spis16t3` part is my account name. Your's will be something like `spis16xy` where `xy` are two letters
* The `ieng6-240` part is the machine I'm logged into.  It's full name is `ieng6-240.ucsd.edu`
* Finally, the `~` part is a symbol for your *home directory*.  That home directory is a very important concept.

Your *home directory* is a folder (called a *directory* on Unix) that stores all of the information you keep on the ACMS
systems.     When you first log on, you always start in your home directory.   

### The `cd`, `mkdir`, and `ls` commands

You can return to your home directory at any time by typing `cd`, all by itself on the command line.  The letters `cd` stand for *change directory*.    Try it:

```
[spis16t3@ieng6-240]:~:34$ cd
[spis16t3@ieng6-240]:~:35$ 
```

In this case, nothing changed, because we were already in our home directory. But, we can try changing into a different directory, and then returning to our home directory.

To see what other directories exist, we can type the `ls` command, which is the *list files* command. Try it:

```
[spis16t3@ieng6-240]:~:39$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
[spis16t3@ieng6-240]:~:40$ 
```

You can see that there are eight folders (directories) under our home directory.  We are going to create one more.
We'll do that with the `mkdir` command for *make directory*.  

Type this at the bash prompt: `mkdir github` and the press enter.  Then type `ls` again and press enter:

```
[spis16t3@ieng6-240]:~:40$ mkdir github
[spis16t3@ieng6-240]:~:41$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos  github
[spis16t3@ieng6-240]:~:42$ 
```

Now you see that there is an additional directory.  Do you see it? It's called github, and its the last one listed.

Our current directory is our home directory, as we can see from the `~` in our prompt.    We can change our current directory to be the github directory by typing `cd github`, as shown here.  Try it, and try typing `ls` right after that.

```
[spis16t3@ieng6-240]:~:42$ cd github
[spis16t3@ieng6-240]:github:43$ ls
[spis16t3@ieng6-240]:github:44$ 
```

You can see that the second part of the prompt changes to `github` to show that we are our in our github directory.
Since this directory is located "under" our home directory, we sometimes call this a "subdirectory".

### The `pwd` command

The next command we are going to learn is the `pwd` command, for *print working directory*.  Try it:

```
[spis16t3@ieng6-240]:github:44$ pwd
/home/linux/ieng6/spis16/spis16t3/github
[spis16t3@ieng6-240]:github:45$ 
```

You see that this command prints out our "working directory".   *Current directory* and *working directory* are just two different ways to say the same thing.

Lets look more closely at what was printed: `/home/linux/ieng6/spis16/spis16t3/github`

This is a list of parent directories (or folders), each of which contains the one below it.

A simplified view is this:

<img src="https://docs.google.com/drawings/d/1-V6Unovl04bGPHKQF4XwyLsp5BoSfIshJFM2nxdr_Gw/pub?w=121&amp;h=571">

These files and directories, though exist in the context of a larger directory tree that contains many other directories and folders.

<img src="https://docs.google.com/drawings/d/18JSwrUBKVmKx9fIL7vX3eexCJI35AMpzIO7g_azldkM/pub?w=853&amp;h=578">

This output `/home/linux/ieng6/spis16/spis16t3/github` from the pwd command is called a *path*, since it shows the path from the root directory of the disk space on our machine, which is represented by the symbol `/`, all the way down to the directory `github` that we just created.

The path in this direct

## Step 2: Cloning a private repo at the bash (Unix) command line

TBD

## Step 3:  How to store a Python file in a repo

TBD

## Step 4:  The basic git workflow of `git add...`, `git commit...`, `git push...`

TBD

## Step 5: Testing of Python functions

TBD

## Step 6:  Submitting a Python function for autograding using Gradescope

TBD
