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

**NOTE**, we do **NOT** want to include `env.sh` in our git repository. If it is, it will get pushed to your Github repos, with the keys and values online and available for anybody to see. This will compromise the security of your webapp.

Create a file called `env.sh` on the same level as your `webapp.py`. The file should have: 

```
export GITHUB_CLIENT_ID=clientidhere
export GITHUB_CLIENT_SECRET=clientsecrethere
export GITHUB_ORG=ucsd-cse-spis-2017
export APP_SECRET_KEY=randomcharactersyoutype
```

Replace it with your correct and corresponding Client ID and Client Secret. Save and go back to the command line. There, to run this script, type `. env.sh` and hit enter. Note the period and space in between. If everything worked correctly, you should be able to type this command with the variable to print out its corresponding value:

```
echo $GITHUB_ORG
echo $GITHUB_CLIENT_ID
echo $GITHUB_CLIENT_SECRET
echo $APP_SECRET_KEY
```

Let's add the file to the `.gitignore`. On the same level as your `webapp.py`, run the command `vim .gitignore`. VIM is a great editor located inside your terminal. There are a lot of keyboard commands that let you fly through your code once you get some practice. It'll be used in your classes and a favorite among the mentors.

Next, scroll all the to the bottom and hit the `a` key. You should now be in insert mode. At the bottom of the file, add a line that says `*.sh`. The asterisk means to include all files that end in `.sh`. This way, we tell Git to ignore all the files that have the `.sh`. Press the `esc` key and you should be out of insert mode. Type `:wq` and hit enter to return to the terminal.

Did it work? Use the `git status` command and we should see that the `.gitignore` got updated and that we should not be able to git add `env.sh`. Make sure you you git add and push the `.gitignore`.

# Step 3: Modifying `webapp.py`

We're almost done! We have to modify `webapp.py`. Don't forget to change these back when you're ready for Heroku again. Find your `login()` method and remove the https scheme. It should look like this:

```python
@app.route('/login')
def login():
    return github.authorize(callback=url_for('authorized', _external=True))
```

At the very bottom of the file, update your `app.run()` with the parameter, `port` to match the port number that you chose when registering your application with Github. 

```python
if __name__ == "__main__":
        app.run(port=YOUR_PORT_NUMBER)
```

# Step 4: Ready to go!

You should be all set to host it locally now! Remember, every time you want to host it locally, run these commands in your project directory:

1. ```. env.sh```
2. ```python3 webapp.py```

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
