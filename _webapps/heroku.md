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
