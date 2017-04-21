---
topic: "Webapps Intro, Part 3"
desc: "Getting started with Heroku on ACMS"
---

# Getting started with Heroku on ACMS.

Outline:

* Create a free Heroku account
* Clone a repo with a basic flask app
* Run it locally first
* Use the Heroku toolbelt on ACMS to get it set up

# Step 1: Create a free Heroku Account

Please visit heroku.com and signup for a free account.  You just have to provide your name, and email, nothing more.  

You can leave "company name" blank.

It is probably a good idea to sign up with your ucsd.edu email, because companies such as Heroku sometimes give discounts for folks at .edu addresses, but its up to you.

Once you've created your account, there will be "getting started" options.  

* If you are completing part three on ACMS: 
    * DO NOT FOLLOW THOSE "getting started" options from the Heroku site yet.
    * Those are appropriate for using Heroku on your own machine, and they are appropriate for using Heroku with Django on Python.  WE AREN'T DOING EITHER OF THOSE YET!
    
* But if you are doing the lab *directly* on your own machine:
    * Then you will want to install the Heroku toolbelt for [Windows](https://toolbelt.heroku.com/windows), [Mac](https://toolbelt.heroku.com/osx) or [Linux](https://toolbelt.heroku.com/), as appropriate
    * You'll also need to make sure you have [Python 2.7 on your Windows, Mac or Linux box](https://www.python.org/downloads/), and
    * Also install git (for [Windows](Git-2.9.3-32-bit), [Mac](https://git-scm.com/download/mac) or [Linux](https://git-scm.com/download/linux).
    * Finally, be sure that you have set up an ssh key *for your laptop* (this is separate from when you did it for your
        ACMS acccount), and upload that key to github.com.  Instructions are here: 
        [git one time setup](http://ucsd-cse-spis-2016.github.io/topics/acms_git_one_time_setup/), but do these
        directly on your laptop at the shell prompt, not on ACMS (all the same steps.)
    * At that point, return to these instructions
    



# Step 2:  Clone our starting code github repo

`cd` into the `~/github` directory of your ACMS account and clone this repo:

```
git@github.com:pconrad/heroku-flask-try-one.git
```

That should look like this:
```
[spis15t7@ieng6-240]:tryHeroku:528$ git clone git@github.com:pconrad/heroku-flask-try-one.git
Cloning into 'heroku-flask-try-one'...
remote: Counting objects: 100, done.
remote: Compressing objects: 100% (89/89), done.
remote: Total 100 (delta 53), reused 7 (delta 2), pack-reused 0
Receiving objects: 100% (100/100), 9.54 KiB | 0 bytes/s, done.
Resolving deltas: 100% (53/53), done.
Checking connectivity... done.
[spis15t7@ieng6-240]:tryHeroku:529$ 
```

Then, cd into this repo:

```
$ cd heroku-flask-try-one
```  
  
# Step 3: Try running the app locally.

You should be able to run this "Hello World" type Flask app in the normal way by either:

* Loading it in IDLE and choosing Run, OR
* `cd`'ing into the directory that contains `hello.py` and typing `python hello.py`

You'll test by visiting your `localhost:5000` URL (or if you need to change the port, whatever you change it to).

Make sure that works.  If so, you are ready to try running on Heroku.




# Step 4: Login to Heroku

You should be able to type the command heroku login at the ACMS Unix prompt and enter your heroku login credentials.  Try that now:

```
[spis15t7@ieng6-240]$ heroku login
Enter your Heroku credentials.
Email: pconrad.cis@gmail.com
Password (typing will be hidden): 
Authentication successful.
[spis15t7@ieng6-240]$ 
```

# Step 5: Set up a new Heroku Application using the heroku command (at the Linux prompt on ACMS)

Next, make sure you are inside your repo folder by using ls and pwd to check your current directory.

If you are not in the repo folder, cd into it. 

Doing this next command while you are in the folder for your github repo automatically associates this github repo with your Heroku application.

Now do:

```
heroku create
```

A random name consisting of two words followed by a 4-digit number will be generated.  In the example below, the name is pure-peak-4027.

It should look like this:

```
[spis15t7@ieng6-240]:heroku-flask-try-one:532$ heroku create
Creating pure-peak-4027... done, stack is cedar-14
https://pure-peak-4027.herokuapp.com/ | https://git.heroku.com/pure-peak-4027.git
Git remote heroku added
[spis15t7@ieng6-240]:heroku-flask-try-one:533$ 
```

# Step 6: Deploy your code: `git push heroku master`


Now you can deploy your code by doing:

`git push heroku master`

* This is similar to, but different from when we do `git push origin master`
* When we type `git push heroku master` we are pushing our code to heroku
    * On heroku, it will be run on a cloud-based web server.
* When we type  `git push origin master`, we are pushing our code to github
    * On github, it is just sitting there, being stored so we have a record of our code changes over time.

After you press "enter" on the git push heroku master command, you'll see a LOT of output.  This is the log of heroku doing everything necessary to put your application on the web.  You might get errors, and if so, you'll need to figure out what's wrong.  But, you will likely get some "warnings" that can be safely ignored (e.g. stuff about upgrading pip, etc.).

Near the end of the output, what you hope to see is something such as this:
```
remote: -----> Compressing... done, 39.2MB
remote: -----> Launching... done, v3
remote:        https://pure-peak-4027.herokuapp.com/ deployed to Heroku
remote: 
remote: Verifying deploy.... done.
To https://git.heroku.com/pure-peak-4027.git
 * [new branch]      master -> master
[spis15zz@ieng6-240]:heroku-flask-try-one:55$ 
```

Once we push, we can visit our application by going to the URL for it.  

For example, if our application is `pure-peak-4027`, the URL is `https://pure-peak-4027.herokuapp.com`

You'll find this in the output above, in the part that reads:

```
remote:        https://pure-peak-4027.herokuapp.com/ deployed to Heroku
```

So, visit that URL and see if the web app is there.

# NEXT STEPS:

Converting a Flask app you already developed that does NOT YET use Heroku into one that does use Heroku.

Fortunately, this is not difficult. It involves, pretty much, just creating two files: Procfile and requirements.txt ,and including those in the root directory of your github repo.

We'll discuss how to do that in our next lesson, [Web Apps Intro (part 4)](/webapps/webapps-intro-part-4/)
