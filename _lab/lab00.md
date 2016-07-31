---
layout: lab
num: lab00
ready: false
desc: "lab00 on basics, by Phill"
assigned: 2016-08-01 09:30:00.00-7
due: 2016-08-03 17:00:00.00-7
---

If you find typos or problems with the lab instructions, please report them on [Piazza]({{site.piazza}})

# Your first lab in SPIS

For your first lab, you'll be using the computers in B230, a lab in the basement of the CSE building.

These computer run the Linux operating system, and you'll log into them with your SPIS ACMS account.

# Administrative one-time tasks for lab00

During this lab you will acheive the following administrative one-time steps

* Learn what your ACMS username/password for SPIS is
* Access your UCSD email account to get your invitation to Piazza
* Activate your Piazza account
* Create an account on github.com using your UCSD email address
* Ask a mentor to invite you to the UCSD-CSE-SPIS-2016 organization
* Accept the invitation

# Learning Goals

After completing this lab, you should be able to

* Login to your SPIS ACMS account on the Linux Systems in B230 of the CSE Building
* Bring up a web browser on those machines
* Bring up a terminal window to access the "bash shell prompt"
* Use a few basic Unix commands 
* Create a Github repository under the UCSD-CSE-SPIS-2016 organization, and clone it to your ACMS account
* Work with the `git add`, `git commit`, `git push` commands
* Bring up IDLE, the programming environment for Python
* Create a short Python program and run it
* Submit that program for testing on Gradescope.com
* Access the test results to know that your submission was successful.

# {{page.num}}, step-by-step 

## Step 1: Sit down at a workstation with your SPIS pair partner

You will share a single workstation with your pair partner, and alternate being the "driver" and the "navigator".

The "driver" is the one typing, and the "navigator" provides guidance to the driver as to what to do.

## Step 2: Obtain your ACMS username and password.

There are some online tools for doing this.    You may need to go to a workstation where a mentor or instructor has already logged into the system, because you can't even *get* to web browser without a username and password.

But if someone else (a mentor or instructor) has a web browser, then the following tools can be used to lookup your account information:

* [ACMS Account Lookup](https://sdacs.ucsd.edu/~icc/index.php)
* [ACMS Account Password Change](https://acms.ucsd.edu/students/gpasswd.html)

## Step 3: Log in and bring up web browser and a terminal

This step should be straightforward, but if you need assistance, ask a mentor or instructor for help.

(TODO: consider adding some more detail or screenshots here.)

## Step 4: Open a web browser, and access your UCSD Email

Each pair partner should take a turn doing this step a

In your UCSD email you should find an invitation to Piazza.   Please accept the invitation.

Then visit [https://piazza.com](piazza.com) to log in to Piazza

Find the UCSD CSE SPIS 2016 course.  There is a thread on Piazza where you'll be asked to post your github.com id.    (NOT your password, just your login id.)  Find this thread.    

If you already have a github.com id, post that id here.  If you don't have one, create one--the next step tells you how.

## Step 5: Visit github.com

Open a web browser, and navigate to github.com

At the github.com page, if you don't already have a github.com account, using your UCSD email address, create one on the "free plan".   

Or, if you already have a github.com account, log in to it, and add your ucsd.edu email address to the list of email addresses associated with the account.

## Step 6: Post your github id to the thread on Piazza

Now, make a post on Piazza with your github.com id.   A mentor or instructor will need to add you to the UCSD-CSE-SPIS-2016 organization on github.com.  Being a part of that organization allows you to share your work with the instructional team so that we can give you feedback.

Once you've made the post, it may be several minutes before the mentors get around to noticing it and inviting you to the team.  In the meantime, we'll work with some other tools available to you via your ACMS account.

## Step 7:  Bringing up IDLE

IDLE is the program we'll use to do Python programming during SPIS.

In IDLE, you you create, edit, and run Python code.

To bring up idle, type `idle` at the bash shell prompt.

It should look something like this:

* TODO INSERT ACMS IDLE SCREENSHOT HERE.

* TODO: INSERT STEPS TO MAKE HELLO WORLD IN IDLE HERE

## Step 8:  Accept invitation to UCSD-CSE-SPIS-2016 github organization

By now, the mentors/instructors should have inivited you to the UCSD-CSE-SPIS-2016 github organization.

You should find an place where you can accept this invitation if you click on this link and look near the top of the page:

<https://github.com/organizations/ucsd-cse-spis-2016>


# A note about pair programming

Throughout SPIS you will be working closely with a partner.  This is something you will be asked to do repeatedly in your courses at UCSD, as well as in your career.  At first this might be uncomfortable.  You might feel like your partner is holding you back, or like you are holding your partner back.  This is natural--different people work at different speeds, and someone who works a little faster is not "better" or "smarter" than someone who works a little slower.   Even in the face of these differences, we want you to work together.   In particular, it is not OK to abandon your partner and simply work on your own.  If you and your partner both agree, you can do small pieces of the project individually, but you must synch up again regularly, and we discourage this style of work.

If you find that you and your partner work at vastly different speeds or have styles that simply cannot work together, we will reassign you to work with someone else.  However, this should be a last resort.  Remember, in your post-school life you will necessarily have to work with others, and you will not always get to choose who these people are.  Learning to work productively with others (in particular with anyone else, not just people you choose to work with) is difficult, but it is also an essential skill that you cannot be successful without.  

For your project work, you need not work with the same partner you use for labs.  But for at least the first two weeks of lab work, you'll be with your same partner, so you might as well get to know each other!

To "learn the do’s and don’ts" of pair programming and to see pairs in action, view this entertaining (if a bit corny/cheesey) video about pair programming from North Carolina State University: [An Introduction to Pair Programming for Students](https://www.youtube.com/watch?v=rG_U12uqRhE).

# A note about assignment deadlines

SPIS will use a series of deadlines to help you stay on track with your work as well as to allow us to keep track of your progress. 

Those deadlines are listed on the [Calendar](/info/calendar/) which is linked to from the navigation links at the top of the SPIS FOCS website (<ucsd-cse-spis-2016.github.io>), as well as from various other places on the website.

Before each of these deadlines, please submit whatever you have completed on that assignment, following the instructions given.  Sometimes this means submission via [Gradescope]({{site.gradescope}}).  Other times, it may mean simply having your latest changes pushed to the appropriate repo on [github.com](https://github.com).

You can also submit earlier if you like. 

However, please know that while we want to encouage you to try to complete assignments by the given deadlines, if you find that you are working at a slower pace, just keep working.  Because SPIS is not graded, it's OK if you don't get everything done, but we'd like you to do as much as you can.   If you aren't finished, submit what you have, but then *keep working on the assignment* as long as it is helping you learn the material.

Periodically, you'll get feedback from your mentors and instructors about your progress on the assignments.     Trying to stay ahead of the deadlines is good practice for the regular quarter, and it will help you get the most out of SPIS.  But the most important thing is to work at the pace at which you will learn the material best.
