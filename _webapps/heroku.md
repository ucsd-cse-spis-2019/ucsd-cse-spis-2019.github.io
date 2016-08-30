---
topic: "Heroku"
desc: "Using Heroku to host Flask-based Python webapps"
---


# Checking the current status of things

Typing `heroku apps:info` can give you a lot of information about the app you are currently working with.

```
$ heroku apps:info
=== salty-reef-52860
Dynos:         
Git URL:       https://git.heroku.com/salty-reef-52860.git
Owner:         pconrad.cis@gmail.com
Region:        us
Repo Size:     0 B
Slug Size:     0 B
Stack:         cedar-14
Web URL:       https://salty-reef-52860.herokuapp.com/
$ 
```

# Setting the heroku remote

Suppose you try to do `git push heroku master` and you get this error message:

```
$ git push heroku master
fatal: 'heroku' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
$ 
```

The problem here is that you don't have the remote `heroku` set up in this particular app.

There are two possible solutions:

1. Find the heroku app you've already created, and link this app to that repo.
2. Use `heroku create` to create a new heroku app.

## Solution 1: Find the heroku app you've already created:

You can list all of your current heroku apps in one of two ways:

* Login to [heroku.com](http://heroku.com) and check the [Heroku Dashboard](https://dashboard.heroku.com/apps)
* OR, use the command line `heroku apps --all`

When you find the name of your app, such as `flowery-poo-23456`, you can use the following command to link it to your
currently cloned repo:

```
$ heroku git:remote -a flowery-poo-23456
set git remote heroku to https://git.heroku.com/flowery-poo-23456.git
$ 
```

This will link the github remote `heroku` to your heroku app.  Then `git push heroku master` will work just fine.

## Solution 2: Create a new heroku app

Type one of the following:

* `heroku create some-awesome-app-name` if you want to name the app yourself
* `heroku create` if you want heroku to pick a name for you, such as `sunburned-surfer-92037` 

This will create a new app, and link your app to it.  Then `git push heroku master` will work just fine.

# A trick to set up Heroku config vars easily

If you are working with OAuth, Sessions, a Database, or an API Key, you may have set up an env.sh file to
store credentials locally.   The env.sh file is typically in your .gitignore so that the confidential
credentials don't end up  being stored, accidentally, in a github repo.

At some point, if you want to run that app on Heroku, you'll have to set up all those variables on the config vars
screen.  That's really tedious.  Here's a shortcut.

Make the following script, called `heroku.sh`.  Just use any editor (could be `idle` or could be another one like `gedit`
to create the file.)

Then:
* *AFTER* running your local `. env.sh` file, THEN
* run this script with `. heroku.sh`

It will copy all of the settings from your local environment into the Heroku config vars.


```bash
#!/usr/bin/env bash

echo "Copying your local env.sh settings to heroku"
echo "You should have run . env.sh before running this script"
echo ""
echo "ALSO NOTE: OAuth CLIENT_ID and CLIENT_SECRET may need to be different for heroku"

heroku config:set  GITHUB_CLIENT_ID=${GITHUB_CLIENT_ID}   
heroku config:set  GITHUB_CLIENT_SECRET=${GITHUB_CLIENT_SECRET}
heroku config:set  APP_SECRET_KEY=${APP_SECRET_KEY}
heroku config:set  GITHUB_ORG=${GITHUB_ORG}

heroku config:set  MONGO_HOST=${MONGO_HOST}    
heroku config:set  MONGO_PORT=${MONGO_PORT}
heroku config:set  MONGO_DBNAME=${MONGO_DBNAME}
heroku config:set  MONGO_USERNAME=${MONGO_USERNAME}
heroku config:set  MONGO_PASSWORD=${MONGO_PASSWORD}
```

Note that for any OAuth credentials, if those credentials work locally, they are tied to a 127.0.0.1:5000 address for the homepage and callback urls.

You'll either have to:
* change those addresses in the OAuth credential page of the OAuth provider (e.g. github.com), (might not work
    immediately, since changes to OAuth credentials can take some time before they take effect)
* (preferred) set up a different GITHUB_CLIENT_ID and GITHUB_CLIENT_SECRET for the heroku instance, 
    and change just *those* two
    variables from what you copied over from your local setup.
