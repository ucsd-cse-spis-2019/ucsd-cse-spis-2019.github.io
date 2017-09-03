---
topic: "OAuth: Testing Locally"
desc: "Test without Heroku"
indent: True
---

# WIP

So you followed the instructions from this [article](/webapps/oauth_actually), but when you got your Heroku app link, nothing shows up. Or you were wondering what the `env.sh.sample` file was or did in some of the example repos. Or you just wanted to know how to be able to run your webapp locally with OAuth.

In this article, we'll go over how to set up your local workstation to be able to run your webapp locally with OAuth. In doing so, we can hopefully debug our webapp easier to be able to figure out why it's not working properly on Heroku. In addition, we'll cover how to have print statements in Flask, giving us another tool in debug toolbox.

# Step 1: Registering the app with Github

Follow the instructions found [here](/webapps/oauth_github) *with a few changes*.

* Make sure that `http://127.0.0.1:portnumber` is your base url and *not* your heroku url. 
* Make sure that the links use http, and *not* https.

# Step 2: Creating env.sh

Now that we have your application's Client ID and Client Secret, we need to tell your webapp where to find it. To maintain the security of our webapp, we don't want anybody to know what the values of these keys are. What we will do is create environmental variables that are saved locally on your current workstation and not available anywhere else. We will create a file called `env.sh` and write a small script that will create and set our environmental variables. As an aside, environmental variables on our local workstations are analogous to Heroku's Config Vars.

**NOTE**, we do **NOT** want to include `env.sh` in our git repository. If it is, it will get pushed to your Github repos, with the keys and values online and available for anybody to see. This will compromise the security of your webapp. We add `env.sh` to our .gitignore, a file that tells Git which files to not add. 


# Print Statements

Sometimes, when debugging, it is very helpful to insert print statements at certain points of the code to see where the program is running, what a certain value of a variable is, and give other useful information. You might want to include some print statements to help you debug.

At the very TOP of your file, include this import statement:

```python
from __future__ import print_function
```

Now, all wherever you want a print statement, you can use this line of code:

```python
print("YOUR_MESSAGE", file=sys.stderr)
```

YOUR_MESSAGE will now be print to your terminal to help you debug!
