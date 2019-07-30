---
layout: lab
num: lab00
ready: true
desc: "The Basics"
assigned: 2019-08-05 08:30:00.00-7
due: 2019-08-06 17:00:00.00-7
---

If you find typos or problems with the lab instructions, please report them on [Piazza]({{site.piazza}})

# Your first lab in SPIS

For your first lab, you'll be using the computers in B230, a lab in the basement of the CSE building.

These computer run the Linux operating system, and you'll log into them with your SPIS ETS account.

While in some labs you will be doing pair programming (working at one computer on a single program, with your partner ), for this lab we would like everyone to complete the lab themselves.  However, you should work next to your partner, and work at the same speed as your partner, helping each other out.  Do not leave your partner in the dust!

# Administrative one-time tasks for {{page.num}}

During this lab you will achieve the following administrative one-time steps

* Learn what your ETS username/password for SPIS is
* Access your UCSD email account to get your invitation to Piazza
* Register your iClicker
* Create an account on [GitHub](https://github.com) using your UCSD email address
* Fill out a Google Form so that we know your GitHub username
* Accept an invitation to the [ucsd-cse-spis-2019](https://github.com/ucsd-cse-spis-2019) GitHub organization
* Activate your Piazza account

# Learning Goals

After completing this lab, you should be able to

* Login to your SPIS ETS account on the Linux Systems in B230 of the CSE Building
* Bring up a web browser on those machines
* Bring up a terminal window to access the "bash shell prompt"
* Bring up [Vim](https://en.wikipedia.org/wiki/Vim_(text_editor)) (a basic text editor) and [gVim](https://en.wikipedia.org/wiki/Vim_(text_editor)#Interface) (the graphical interface of Vim)
* Create a short Python program and run it
* Create a GitHub repository under the [ucsd-cse-spis-2019](https://github.com/ucsd-cse-spis-2019) organization
* Use the GitHub web interface to upload files and edit text in a `README.md` file

# {{page.num}}, step-by-step 

## Step 0: Obtain your ETS username and password.

Before you can even sit down and begin using a workstation in B230, even to surf the web, you need to know your ETS username and password.

And to obtain those, you'll need to be able to access a web browser.  **Catch-22!**

But if someone else (a mentor or instructor) has a web browser, then the information at this page can be used to look up your ETS username, and reset your password:

[https://ucsd-cse-spis-2019.github.io/topics/acms/](/topics/acms/)

Once you know your username and password, please sit down at a workstation next to where your partner is sitting.

## Step 1: Log in and bring up web browser and a terminal

You can open a web browser by going to the Applications menu at the top of the screen, and then going to Internet Tools and selecting Firefox from that menu.  

To open a "terminal" window (a window where you can type commands--we'll work a lot with the terminal throughout SPIS), you can select “Applications”, the "System Tools", then either “Terminal” or “Konsole” from the menu that pops up.  Alternatively, you can right-click on the desktop and select "Terminal".  

Make sure both you and your partner are logged in and have both a web browser and a terminal window open before continuing.

## Step 2: Register your iClicker

Go to [this survey](https://forms.gle/6ckwCFyTJs6SdesU9) to enter your iClicker remote ID (the number on the sticker on the back) and your PID.  If you have previously done this step, you do not need to do it again now.

## Step 3: Visit GitHub to create or update your account

Open a web browser, and navigate to [github.com](https://github.com).

At the GitHub home page, if you don't already have a GitHub account, using your UCSD email address, create one on the "free plan".   

Or, if you already have a GitHub account, log into it, and add your `@ucsd.edu` email address to the list of email addresses associated with the account.

Then, fill out the following form to let us know what your GitHub username is:
[https://forms.gle/cNv6mT7uA8z9wbKT7](https://forms.gle/cNv6mT7uA8z9wbKT7)

## Step 4:  Bringing up gVim

[Vim](https://en.wikipedia.org/wiki/Vim_(text_editor)) is the text editor we'll use to do Python programming during SPIS. Specifically, we will be using its graphical interface, [gVim](https://en.wikipedia.org/wiki/Vim_(text_editor)#Interface), but students who are interested may wish to become proficient with Vim.

To bring up gVim, type `gvim` at the bash shell prompt.  The "shell prompt" is the line where you can type commands in the terminal window you opened in step 1, and it should look something like this:

```bash
[sp19t1@ieng6-248]:~:14$ 
```

You type `gvim` after the `$` and then press `Enter`.  You should see a new window pop up called "GVIM".  This is where we will be writing our Python programs.

## Step 5: Write and run your first Python program

For this step, there is one goal: write a Python program that prints the string `Hello, World!` as its output.

In this sense, we are following a long tradition: for [more than 40 years](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) it has been a tradition to make printing `Hello, World!` be the first thing you do when learning a new programming language.

Note that, in this course, we will be using Python 3 (there are different versions of the Python language, with Python 3 being slightly different from the older Python 2).

First, we will create a new file in which we will write our program. In gVim, go to the "File" menu and select "New".  The window will go blank, and the window title will say "[No Name]".

Before we start coding, let's save this new file as `hello_world.py`. The file extension `.py` denotes that this will be Python code. In gVim, go to the "File" menu and select "Save As...". This wil bring up a pop up window that will let you choose where to save your file. Let's create a new folder for this assignment. Click on your account name (`spis19xx`), click the "Create Folder" button, replace "Type name of new folder" with `lab00`, and click the "Enter" button on your keyboard to create the folder. Once in the folder, type `hello_world.py` in the box that says "Name:", and click "Save". Now, your file will be saved on your account's desktop. In the future, to save changes this program, go to the "File" menu and select "Save".

Note that gVim has different "modes." When it is first opened, gVim starts in "Command Mode," which lets us run various commands to perform operations on the text or to navigate the file, which is not what we want to do right now. If you want to actually *edit* the file, gVim has to be in "Insert Mode," which lets us edit the text like any other text editor. In order to go from "Command Mode" to "Insert Mode," simply click the `i` key on your keyboard; the bottom of the gVim window should now say `-- INSERT --`. To go back to "Command Mode" from "Insert Mode," simply click the `Escape` key on your keyboard; the `-- INSERT --` text should now disappear. For more information about gVim's modes, see [this tutorial](https://supportweb.cs.bham.ac.uk/documentation/tutorials/docsystem/build/tutorials/gvim/gvim.html#gVim-Core-Commands-Modes).

Now, let's start actually writing our `Hello World` program. Enter "Insert Mode" (by pressing the `i` key), and type or copy/paste the code for the `Hello World` program, shown below. To paste in gVim, go to the "Edit" menu and click "Paste". In Python, this program is very short. It looks like this:

```python
print('Hello, World!')
```

That's it! Notice that different words and symbols of our code were automatically highlighted different colors. Vim (and most modern text editors) have a feature called "syntax highlighting": if you specify that you're programming in a specific language, the text editor will highlight your code based on that programming language's syntax to make your code easier to read. When we saved our program with the `.py` extension, we essentially told gVim that we will be programming in Python.

Now, you can also add, on the first line, a *comment* with your name and the reason you wrote the program.

```python
# Alex Triton for CSE SPIS 2019
print('Hello, World!')
```

You are encouraged to write this comment, because it helps someone looking at your code know that *you* wrote it.  But, comments do not affect the functionality of the program.  In general, in computer programming, a *comment* is something that is intended only for human readers of the code, and is otherwise "ignored by the system".   Nearly every programming language has some way to express comments, though the exact rules for formatting of comments -- that is, the *syntax* of comments -- differs from one language to another.

In Python, a `#` starts a comment.  Everything from the `#` to the end of that line is part of the comment (and is thus ignored when the program is run).

Now, let's save our program! Remember from before that, in gVim, you can save by going to the "File" menu and clicking "Save".

In order to run your program, go to the terminal, and navigate to the folder we created earlier. You can do so with the following command: `cd ~/lab00`

If you run the `ls` command, you'll **l**i**s**t the files in this folder; you should see our `hello_world.py` program. To run our program using Python 3, you can use the following command:

```bash
[sp19t1@ieng6-248]:~:14$ python3 hello_world.py
```

When you run the program, if everything worked correctly, you should see our message: `Hello, world!`

Note that, when we ran our program, we called `python3` instead of just `python`. Some computers have both Python 2 and Python 3 installed at the same time, and just calling `python` can potentially call Python 2 *or* Python 3 depending on how the computer was set up! Thus, for the sake of clarity and to be safe, it's best to specify which version you want to call by using `python3`.

Once both you and your partner have run your "Hello World!" programs, you are ready to move on to the next step.  Remember, check in with your partner to make sure they are ready to move on.  Do not leave your partner in the dust!


## Step 6:  Accept invitation to ucsd-cse-spis-2019 GitHub organization

The mentors/instructors should have invited you to the [ucsd-cse-spis-2019](https://github.com/ucsd-cse-spis-2019) GitHub organization (if they haven't, the invitation will come soon).

You should find a place where you can accept this invitation if you click on this link and look near the top of the page:

<https://github.com/ucsd-cse-spis-2019>

Click on the invitation so that you are part of the [ucsd-cse-spis-2019](https://github.com/ucsd-cse-spis-2019) organization.

## Step 7:  Create your first GitHub repo, a practice repo.

Your next step will be to create a GitHub *repository* (or *repo* for short).  

Your first repository will have a name that corresponds to your first name and last initial such as:

* `ucsd-cse-spis-2019/practice-alex-t`
* `ucsd-cse-spis-2019/practice-chris-l`

To create this repo:

* In your web browser, navigate to [github.com](https://github.com)

* Login to your GitHub account, and 

* Then create a new repository. You do this by pressing the green button with the words "New". Alternatively, on the menu bar on top, there is a '+' sign with a down arrow next to it. If you click it, you also get the option of creating a new repository. 

On the next screen:

* Be sure that you select to create your repository with the owner being `ucsd-cse-spis-2019`, NOT your own GitHub id.
* Put `practice-alex-t` as the name (BUT PUT YOUR OWN NAME AND FIRST INITIAL, not literally `alex-t` :-) )
* check the box to "Initialize this repository with a README"
* Select a `.gitignore` file for Python
* You don't need to select a license file.

Then, once you've entered all of this information, click to create the repository.

Periodically, check in on your partner. You are there to help each other.


## Step 8:  Add a message and a photo to your `ucsd-cse-spis-2019/practice-alex-t` repo.

For this step, please ask someone to take a photo of you, with your face and your name tag visible. We will use these pictures to create a roster, so please make sure you are easily recognizable. They can then send you the photo through email.

Once you have the photo in your email, access it from the web browser of the ETS linux machine at which you are
seated.   Save the photo (i.e., the `.png`, `.jpg`, or whatever) to a file.  Depending on the browser you are using, this 
file may end up in your "home directory", or in some other directory (e.g. `~/Downloads`, `~/Desktop`, etc.)

Once you've located it, change the name to `alex-t.jpg` or `alex-t.png` or whatever. You need to keep the `.jpg` or `.png` file extension exactly as it is, but change the first part of the filename to match your first name and last initial, in lowercase, separated by a hyphen (`-`). The naming convention is important, because the SPIS staff is going to access all of these images to create a SPIS photo album so that we can all learn your names more quickly.

Once you've located it, your next job will be to upload it to your GitHub practice repository.  We'll discuss how
in the next step.


## Step 9: Upload your photo to your `ucsd-cse-spis-2019/practice-alex-t` repo.

Navigate to the web page for your repo.  It will be something like:

`{{site.course_github_url}}/practice-alex-t`

except it will be your name instead of `alex-t`.

On the right hand side, there is a great big green button labelled "Clone or Download". Eventually, we'll be using that button a lot.  But for now, look just a few buttons to the left, and you'll find a button that says "Upload files".

Click that button, and upload your photo from the place where you saved it out of your email. Click the green "Commit changes" button.



## Step 10: Edit your README.md file to add some information about you, and a link to your photo

Navigate again to the main page for your repo, e.g. 

`{{site.course_github_url}}/practice-alex-t`

You'll see a file called `README.md`.  Click on the filename.  This should take you a page for just that file,
where you'll see, among other things, a pencil icon that allows you to make changes to the file.

In that file, add a few lines of text that introduces yourself to the SPIS 2019 instructional staff. 
Tell us where you are from, some of things you are hoping to learn during SPIS, and perhaps some
outside interests and activities you might like to participate in during our non-academic sessions
(e.g. sports, musical instruments you play, board games, etc.)

Then, add the following, on a line by itself, with a blank line before it and after it. 

Copying it exactly, except for changing the `alex-t.jpg` part to whatever the name
of your image file is:

```
![me](alex-t.jpg)
```

Save it (click the "Commit change" button), and take a look at your README.md file.  You should see your photo embedded in the `README.md` text.

If so, you are almost finished with lab00! How is your partner doing?


## Step 11: Piazza Invitation

In your UCSD email you should find an invitation to Piazza.   Please accept the invitation, if you have not done so already.

Then visit [https://piazza.com](https://piazza.com) to log in to Piazza

Find the UCSD CSE SPIS 2019 course and familiarize yourself with the Piazza site.

# A note about assignment deadlines

SPIS will use a series of deadlines to help you stay on track with your work as well as to allow us to keep track of your progress. 

Those deadlines are listed on the Calendar, which is linked to from the navigation links at the top of the [SPIS FOCS website](/), as well as from various other places on the website.

Before each of these deadlines, please submit whatever you have completed on that assignment following the instructions given.
This may mean simply having your latest changes pushed to the appropriate repo on [GitHub](https://github.com), or this may mean following an alternative set of instructions to submit your assignment.

You can also submit earlier if you like. 

However, please know that while we want to encouage you to try to complete assignments by the given deadlines, if you find that you are working at a slower pace, just keep working.  Because SPIS is not graded, it's OK if you don't get everything done, but we'd like you to do as much as you can. If you aren't finished, submit what you have, but then *keep working on the assignment* as long as it is helping you learn the material.

Periodically, you'll get feedback from your mentors and instructors about your progress on the assignments. Trying to stay ahead of the deadlines is good practice for the regular quarter, and it will help you get the most out of SPIS.  But the most important thing is to work at the pace at which you will learn the material best.

