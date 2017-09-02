---
topic: "Databases: MongoDB"
desc: "NoSQL database system"
indent: true
---

For an introduction to Databases, and their role in webapps, see the article:

* [Webapps: Databases](/webapps/databases/)

# MongoDB on mLab

MongoDB is a particular implementation of a NoSQL database. It creates a Database, which contains Collections, which contains Documents. This is an image of an example: 

There are multiple hosting providers that offer MongoDB implementations "in the cloud" as a service.

The particular one we'll be using for SPIS 2016 is called mLab (<https://www.mlab.com>).  We are using mLab because:

* there is free tier
* using the free tier does not require entering a credit card

# Use mLab.com *directly*, not via the Heroku mLab add-on

Note that we *NOT* using mLab MongoDB Add-On for Heroku&mdash;instead, we are using mLab directly through its own console at <https://www.mlab.com>. 

# Wait, why aren't we using the mLab add-on.

Although it is slightly more convenient to use the Heroku mLab add-on, that add-on requires entering a credit card into Heroku (even though it is free).      What using the Heroku add-on buys you is that with one click, you can:

* Automatically create the database
* Automatically fill in the five parts of the configuration info for the database directly into Heroku's configuration variables
     * For the record, those are: (host, port, database name, database username, database password) 

When you use mLab directly, you have to do those steps manually.  Fortunately, that isn't very difficult.  It's just slightly tedious, but you typically only have to do it once per application, and then you never have to worry about it again (at least not for that app.)

# As an aside, what *is* free on Heroku?

In fact, the only free services on Heroku that do not require entering a credit card are:

* Up to five running applications (but no more than that)
* The Heroku Postgres add-on (which is for an SQL-based database)
    * We certainly could use Postgres, but its a bit more complicated.
* The Heroku Connect add-on 
    (which is for integration with Salesforce.com, something not of particular interest to us in SPIS.)

# Now, let's go through the steps to implement a MongoDB Database

## Step 1: Install `Flask-PyMongo` Python Module 

There is a Python module called [Flask-PyMongo](http://flask-pymongo.readthedocs.io/en/latest/) that we can install with `pip install` to make working with MongoDB easier.

To install it on ACMS, use:

```
pip install --user Flask-PyMongo
```

on Windows or Mac, just:

```
pip install Flask-PyMongo
```

## Step 2: Add to your `requirements.txt`

You'll also need to make sure that you add these lines to the `requirements.txt` file for any webapp that you want to 
run on Heroku with MongoDB:

```
Flask-PyMongo==0.4.1
pymongo==3.3.0
```

## Step 3: Create an mLab account on mlab.com

Go to <https://www.mlab.com> and follow the instructions on the website to create a mLab account. The account name can be the name of your Web App project. You will also a receive an email, asking you to confirm your account.

## Step 4: Creating a Database (MongoDB Deployment)

Once you've created an account on mLab, we're create a deployment for your database. Make sure you are logged in and on your home page. 

1. Create a new database by clicking the `Create new` under the MongoDB Deployments.

2. You will then be taken to a different page to choose a provider and a plan. Make sure that the plan you choose is the one that is free, that is, the 'Sandbox' plan with up to 0.5GB of storage. For the provider, we will stick with the default of Amazon Web Services.

3. Next, you will be asked to choose a region. Select 'US East (Virginia)' and click the continue button.

4. You are then asked to choose a database name. Choose something that make sense for your application. For example, if your database is storing information about cars, call it `carsdb` or just `cars`. If you don’t have an application in mind, you can just use `testdb`. After choosing your name, click continue.

5. Finally, review all the details to make sure they're correct and click 'Submit Order'.

## Step 5: Using your MongoDB Deployment (database)

## Step 6: Implement MongoDB in your Python file

# References

* <http://blog.dwyer.co.za/2013/10/a-basic-web-app-using-flask-and-mongodb.html>
* <https://mlab.com>
* MongoDB Collection operations from pymongo module: <https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection>
