---
topic: "ETS Account: Creating ~/github"
desc: "Bash shell command intro, and creating your ~/github directory"
---

# Creating ~/github
## And learning some shell commands in the process

This brief tutorial has two purposes.

1.  By the time you are finished, you should have a `github` directory immediately under the home directory of your
    SPIS ETS account, that is a directory called `~/github`
    
2.  By the time you are finished, you'll have learned about a few basic Unix commands, including the ones in the table below.

If *both* you *and* your pair partner are already thoroughly familiar with Unix command basics&mdash;that is, you know how to create
`~/github`, and you are *throughly* familiar with everything in the table below, you can just create ~/mkdir, and skip
the rest of this page. 

But if either or both of you has any doubt, you are strongly encouraged to go through this page carefully and slowly,
to learn some of the basics of working with Unix commands at the bash shell.  That is one of the most fundamental skills you'll need
throughout all of the courses that use the ETS unix accounts during your entire stay at UCSD.

# Unix commands covered in this tutorial

Here is a table of the Unix commands covered in this brief tutorial:

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
| `cd ..`       | Change directory to parent of current directory (go up)         |
| `cd ~/fum`     | Change directory to `foo` inside home directory (`~`)           |

You should also learn the following concepts:

* Home directory (`~`), directory, and subdirectory
* Unix/Linux directory tree, rooted at `/`
* Bash Shell
* Shell prompt


# Step 1: Bring up a bash terminal shell

Bring up a bash terminal shell.  As a reminder, you can do this by selecting "Applications", then "System Tools", then either "Terminal" or "Konsole" from the menu that pops up.  (Your Applications menu may have only Terminal, or only Konsole, or may have both.
For our purposes, they work equally well.)

For now, we can use the following terms to mean more or less the same thing.  (There are fine-grained distinctions among these terms, but those won't be important until later in your studies)

* A "terminal session" on your ETS account
* The "unix command line"
* The "bash shell prompt"

Let's also establish that while "Unix" and "Linux" refer to different things, for our purposes
in SPIS, it is enough to know that "Linux" is a particular flavor of the "Unix" family of operating
systems.   The systems we are running use Linux, in contradistiction to running Windows or Mac OS.

So, during SPIS, when we refer to Unix or Linux, these are, again more
or less interchangable terms.  The fine grained distinctions between
the two can be saved for later.

# Step 2: Learn about the bash prompt, date, `~` for home directory, and `history`

When you open up a terminal session on the lab machines the bash terminal prompt typically looks like this:

```
[spis18t3@ieng6-240]:~:32$ 
```

It is called a *prompt* because it *prompts* you to enter some a command.  One of the most basic commands you can enter is
the `date` command.  Try it: type in `date` and press return *Enter*.

```
[spis18t3@ieng6-240]:~:32$ date
Thu Aug  4 13:56:29 PDT 2016
[spis18t3@ieng6-240]:~:33$ 
```

The date is printed, and you get a new prompt.  Note that the last
number in that prompt keeps increasing by one (1) each time you enter a command.  Try entering
the `date` commmand and pressing enter several times to see this.

These numbers refer to your "command history".  If you type the
command `history`, you'll see a list of all the recent commands you
have typed.  Try it:

```
[spis18t3@ieng6-240]:~:33$ history
    1  idle
    2  idle
    3  pwd
```
(I left some out here...)
```
   31  exit
   32  date
   33  history
[spis18t3@ieng6-240]:~:34$ 
```

You can see that the next command I type will be "number 34" in my history.

# Step 3: Your account and machine in the prompt

There are a few others parts of the prompt.  

* The `spis18t3` part is my account name. Your's will be something like `spis18xy` 
    where `xy` are two letters
* The `ieng6-240` part is the machine I'm logged into.  It's full name is `ieng6-240.ucsd.edu`
* Finally, the `~` part is a symbol for your *home directory*.  That home directory is a 
    very important concept.

Your *home directory* is a folder (called a *directory* on Unix) that
stores all of the information you keep on the ETS systems.  When you
first log on, you always start in your home directory.

# Step 4:  The `cd`, `mkdir`, and `ls` commands

You can return to your home directory at any time by typing `cd`, all
by itself on the command line.  The letters `cd` stand for *change
directory*.  Try it:

```
[spis18t3@ieng6-240]:~:34$ cd
[spis18t3@ieng6-240]:~:35$ 
```

In this case, nothing changed, because we were already in our home
directory. But, we can try changing into a different directory, and
then returning to our home directory.

To see what other directories exist, we can type the `ls` command,
which is the *list files* command. Try it:

```
[spis18t3@ieng6-240]:~:39$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
[spis18t3@ieng6-240]:~:40$ 
```

You can see that there are eight folders (directories) under our home
directory.  We are going to create one more.  We'll do that with the
`mkdir` command for *make directory*.

# Step 5: The `mkdir` command

Type this at the bash prompt: `mkdir github` and the press enter.  Then type `ls` again and press enter:

```
[spis18t3@ieng6-240]:~:40$ mkdir github
[spis18t3@ieng6-240]:~:41$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos  github
[spis18t3@ieng6-240]:~:42$ 
```

Now you see that there is an additional directory.  Do you see it? It's called github, and its the last one listed.

# Step 6: More on `cd` and `ls`

Our current directory is our home directory, as we can see from the
`~` in our prompt.  We can change our current directory to be the
github directory by typing `cd github`, as shown here.  Try it, and
try typing `ls` right after that.

```
[spis18t3@ieng6-240]:~:42$ cd github
[spis18t3@ieng6-240]:github:43$ ls
[spis18t3@ieng6-240]:github:44$ 
```

You can see that the second part of the prompt changes to `github` to
show that we are our in our github directory.  Since this directory is
located "under" our home directory, we sometimes call this a
"subdirectory".

# Step 7: The `pwd` command, and Unix paths

The next command we are going to learn is the `pwd` command, for *print working directory*.  Try it:

```
[spis18t3@ieng6-240]:github:44$ pwd
/home/linux/ieng6/spis18/spis18t3/github
[spis18t3@ieng6-240]:github:45$ 
```

You see that this command prints out our "working directory".   *Current directory* and *working directory* are just two different ways to say the same thing.

Lets look more closely at what was printed: `/home/linux/ieng6/spis18/spis18t3/github`

This is a list of parent directories (or folders), each of which contains the one below it.

A simplified view is this:

<img src="https://docs.google.com/drawings/d/1-V6Unovl04bGPHKQF4XwyLsp5BoSfIshJFM2nxdr_Gw/pub?w=121&amp;h=571">

These files and directories, though exist in the context of a larger directory tree that contains many other directories and folders.

<img src="https://docs.google.com/drawings/d/18JSwrUBKVmKx9fIL7vX3eexCJI35AMpzIO7g_azldkM/pub?w=853&amp;h=578">

This output `/home/linux/ieng6/spis18/spis18t3/github` from the pwd command is called a *path*, since it shows the path from the root directory of the disk space on our machine, which is represented by the symbol `/`, all the way down to the directory `github` that we just created.

Our home directories for spis this year are all located inside `/home/linux/ieng6/spis18`.   They are, for example:

* /home/linux/ieng6/spis18/spis18aa
* /home/linux/ieng6/spis1/spis18ab
* /home/linux/ieng6/spis18/spis18ac
* /home/linux/ieng6/spis18/spis18ad
* /home/linux/ieng6/spis18/spis18ae
* etc...

Each of you has your own home directory.  

# Step 8: Various directory navigation commands

As a reminder:

* The command `pwd` tells us where we are by printing the current working directory.
* The command `ls` lists the files in the current directory

You can change the current working directory in a variety of ways.  Try changing your directory in various ways,
exploring the directory tree shown in the diagram above, and using `pwd` and `ls` to show the effect.

* `cd ~` or `cd` to go your home directory
* `cd ~spis18t1` or `cd ~spis18t2` to go to a specific user's home directory
* `cd ..` to go *up one level in the tree* from where you are now.  
* `cd /` to go to the root of the directory
* `cd foo` to go into a directory foo that is located in the current directory

You should be able to use the `pwd` command at each level 

Note that `cd /foo` does NOT go one level down from the current
directory. Instead, it goes into the foo directory directly under the
root directory.

# Step 8: Finishing up in `~/github`

When you are all finished, cd into your `~/github` directory.  Note that you can do this
from anywhere with a single command: `cd ~/github`, as shown here:

```
[spis18t3@ieng6-240]:~:79$ cd ~/github
[spis18t3@ieng6-240]:github:80$ pwd
/home/linux/ieng6/spis18/spis18t3/github
[spis18t3@ieng6-240]:github:81$ 
```

As shown above, use `pwd` to verify that you are indeed in your `~/github directory`.

Your output won't say `spis18t3`, but instead will show your own ETS username in place of that.

If you were doing these steps as part of SPIS 2017 lab02,<br>
you can use this link to return there now: [SPIS 2017 lab02](/lab/lab02/)
