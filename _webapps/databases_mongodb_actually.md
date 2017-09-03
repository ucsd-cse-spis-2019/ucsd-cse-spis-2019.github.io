---
topic: "Databases: Implementing MongoDB"
desc: "Steps to add MongoDB to your WebApp"
indent: true
---

Make sure you have read these articles prior to beginning:

* [Webapps: Databases](/webapps/databases/)
* [MongoDB Intro](/webapps/database_mongodb)

# Now, let's go through the steps to implement a MongoDB Database

# Step 1: Install `Flask-PyMongo` Python Module 

There is a Python module called [Flask-PyMongo](http://flask-pymongo.readthedocs.io/en/latest/) that we can install with `pip install` to make working with MongoDB easier.

To install it on ACMS, use:

```
pip install --user Flask-PyMongo
```

on Windows or Mac, just:

```
pip install Flask-PyMongo
```

# Step 2: Add to your `requirements.txt`

You'll also need to make sure that you add these lines to the `requirements.txt` file for any webapp that you want to 
run on Heroku with MongoDB:

```
Flask-PyMongo==0.4.1
pymongo==3.3.0
```

# Step 3: Create an mLab account on mlab.com

Go to <https://www.mlab.com> and follow the instructions on the website to create a mLab account. The account name can be the name of your Web App project. You will also a receive an email, asking you to confirm your account.

# Step 4: Creating a Database (MongoDB Deployment)

Once you've created an account on mLab, we're create a deployment for your database. Make sure you are logged in and on your home page. 

1. Create a new database by clicking the `Create new` under the MongoDB Deployments.

2. You will then be taken to a different page to choose a provider and a plan. Make sure that the plan you choose is the one that is free, that is, the 'Sandbox' plan with up to 0.5GB of storage. For the provider, we will stick with the default of Amazon Web Services.

3. Next, you will be asked to choose a region. Select 'US East (Virginia)' and click the continue button.

4. You are then asked to choose a database name. Choose something that make sense for your application. For example, if your database is storing information about cars, call it `carsdb` or just `cars`. If you don’t have an application in mind, you can just use `testdb`. After choosing your name, click continue.

5. Finally, review all the details to make sure they're correct and click 'Submit Order'.

# Step 5: Using your MongoDB Deployment (database)

From the home screen of Mlab, you should see your database listed. Click on its name to bring up some more options, including adding a collection and adding a database user. 
 
You need to add a collection before you are ready to try any Python code that accesses the database. But, you should have your Python code ready to go before you add the database user. Both of these statements are explained in more detail below.

## Adding a Collection

The Python code for accessing an mLab database has to have certain values in it. This is very similar to all of the variables we created for OAuth. Those values are:

* dbuser
* dbpassword
* hostname (e.g. ds135912.mlab.com)
* port number (35912)
* database name

The hostname, port and database name can be found in the information at the top of the page for your MongoDB Deployment. Look for the text under “To connect using a driver via the standard MongoDB URI”. It should look a little something like this: 

```
mongodb://<dbuser>:<dbpassword>@YOURHOSTNAME.mlab.com:PORTNUMBER/DATABASE_NAME
```

Note that dbuser and dbpassword are in `<>` and not given to you yet. The dbuser and dbpassword are things you’ll create in a step below.

You also need at least one “collection” in order to do anything interesting. The first thing you’ll want to do is to add at least one collection. For simple applications, you will likely not need more than one collection. Objects inside a collection are “documents”, which is the MongoDB terminology for a single JSON (JavaScript Object Notation) object. More about JSON can be found [here](http://www.json.org).

To add a collection, click the "Add Collection Button" and choose a name for your collection.

* The collection name may very well be the same as the database name in many simple applications (e.g. cars, counties, etc.)
* Perhaps the best way to choose a name is think about what kind of “thing” in the real world is represented by each item in the collection. If it’s a collection of JSON objects representing movies, call it 'movies'.

We don't want to create our database user inside mLab because once you type in the password, you won't be able to see it. The best way to go about this is to (1) create an `env.sh` file to create environmental variables for local hosting or (2) create these variables in Heroku for your web app. We will be doing the latter. If you're interested in the env.sh and doing this locally, talk to a mentor. 

Think of a simple username such as dbuser1. Note, this is not a *human* user, but rather a "machine user", i.e. it is the user/password credentials that will be used by your Python application to connect to this database. 

Next, your password will be random characters such as weaf8jawel8f8waefjawe8fjlaw8fhalwifhaw3. We will copy-and-paste that password (not literally the one on this web page) into the mLab user creation form from Heroku. Let's get jump into this part.

On Heroku, go to your app's main page, go to 'Settings', and click the 'Reveal Config Vars' (This should be very familiar from OAuth and you should see your vars from it). 

Make sure to add the following variables to the Config Vars (MONGO_DBNAME, MONGO_HOST, MONGO_PASSWORD, MONGO_PORT, MONGO_USERNAME) with *your* corresponding values on Heroku as shown in the photo:

IMAGE HERE

For example, dbuser1 would be the value for MONGO_USERNAME. Copy the value for MONGO_PASSWORD and go back to mLab. Click the tab called 'Users' and click the 'Add database user' button. Use dbuser1 (for example) and past the password in the corresponding fields. 

Now you have mLab set up with a database and collection and your mlab is connected to your Heroku account through the variables.

# Step 6: Implement MongoDB in your Python file

This implementation assumes that you have already implemented [OAuth](/webapps/oauth_actually)

At the top of your file, we need an additional import statement for PyMongo in order to use MongoDB:

```python
from flask_pymongo import PyMongo
```

Next, include the following code in your Python file (Probably near where you defined the OAuth variables):

```python
app.config['MONGO_HOST'] = os.environ['MONGO_HOST']
app.config['MONGO_PORT'] = int(os.environ['MONGO_PORT'])
app.config['MONGO_DBNAME'] = os.environ['MONGO_DBNAME']
app.config['MONGO_USERNAME'] = os.environ['MONGO_USERNAME']
app.config['MONGO_PASSWORD'] = os.environ['MONGO_PASSWORD']
mongo = PyMongo(app)
```

Note the similar pattern we have implementing MongoDB as we do with OAuth. Heroku's Config Vars are analogous to a system's os environmental variables. When we host this on Heroku, your webapp will know to look in the Config Vars.

## Adding Documents

The code for adding documents is: 

```python
mongo.db.NAME_OF_YOUR_COLLECTION.insert( INFO_YOU_ARE_INSERTING )
```

## Finding Documents

The code for finding documents is: 

```python
mongo.db.NAME_OF_YOUR_COLLECTION.find( INFO_YOU_ARE_FINDING )
```

Here is the link to the Flask-PyMongo [documentation](https://flask-pymongo.readthedocs.io/en/latest/) where you can learn about the methods available. I highly suggest researching on your own as these are just some of the basic things you can do. 

An example web app running databases and OAuth can be found hosted on [http://fierce-citadel-23727.herokuapp.com](http://fierce-citadel-23727.herokuapp.com) and [http://young-waters-24831.herokuapp.com](http://young-waters-24831.herokuapp.com).
