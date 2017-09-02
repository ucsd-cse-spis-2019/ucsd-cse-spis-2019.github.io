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

# Step 6: Implement MongoDB in your Python file
