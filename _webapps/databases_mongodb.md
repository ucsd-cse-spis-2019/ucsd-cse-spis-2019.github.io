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

# Let's get started

Click [here](/webapps/databases_mongodb_actually) to go to the article where we will walk you through the steps needed to implement a MongoDB database in your web app!

# References

* <http://blog.dwyer.co.za/2013/10/a-basic-web-app-using-flask-and-mongodb.html>
* <https://mlab.com>
* MongoDB Collection operations from pymongo module: <https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection>
