---
topic: "OAuth"
desc: "Delegating username/password authentication to Github, Facebook, Google, etc."
---

# What is OAuth, and why do we need it?

If you've ever seen a webapp that allows you to "Login with Facebook", "Login with Google", etc. as in the images below, then you've seen an example of a webapp that is probably using OAuth.

![OAuth sample icons](/webapps/oauth/oauth_login_with_icons.png) 
![OAuth sample buttons](/webapps/oauth/oauth_login_with_buttons.png) 

OAuth allows one web application to delegate the function of "username/password" checking, and account management (creating, updating, verifying and deleting accounts) to some other service, such as Google, Facebook, Github, Twitter, etc.

These other services are called *OAuth Providers* and the webapp that users the service is called an *OAuth Client*.

The  version of OAuth (as of Summer 2016, when this lesson is being written) that is most current and should be used for new applications is OAuth2.

# Why not implement a username/password account feature from scratch?

You *could* do that.  This article explains an approach to implementing do-it-yourself account creation (usernames, passwords, email verifiction, password reset, etc.) using Flask and an SQL database: [http://exploreflask.com/en/latest/users.html](http://exploreflask.com/en/latest/users.html).

*HOWEVER*, that would probably take you at least a week, and it would probably be the only thing your webapp would be able to do.  It is a classic case of "reinventing the wheel".    

During SPIS 2016, we have just about a week (from Thursday of Week 4 to Thursday of Week 5) to implement a full web app from start (initial brainstorming) to finished product (demos on Friday of Week 5.)   It doesn't make sense to spend time
doing something that is a "commodity feature" like account management, especially when delegating that to an OAuth provider
is *much* more straightforward.

# Do I even need user logins in my SPIS 2016 webapp project

Maybe&mdash;maybe not.  There is a below section that will ask a few questions to see whether you need authentication (user login/logout functionality) or not.  It will also check to see what level of user authentication you might need.

There are a few simple questions to determine whether your web app needs user logins or not

1.  <b>Do you need to save any information between sessions</b>?    
    * If the answer is yes, then that means your web app will need a [Database](/_webapps/databases.md).  
    * And if you need a database, <b>you'll need user logins, so you'll need OAuth</b>
    * This is true even if you don't think you need to save any particular information about individual users.
    * The reason has to do with security and accountability.  Any webapp that let's users upload content 
         without authentication quickly becomes a cesspool of spam, left by bots and trolls.
    * Requiring logins&mdash;and tracking which users have uploaded which content&mdash;gives 
        you some degree of control over this.  
    * It doesn't entirely prevent abuse, but
        it does slow down the process, and give you some way to ban specific abusive accounts.
    * An even better way is to require not only a login, but an "approved" account.   
    * The sample code we are providing shows a particular way of doing this, levering the Github *organization* 
         feature.  More on that later.

2.  <b>Do you want users to be able to save personalized information and preferences on your site</b>?
    * If the answer is yes, then <b>you'll need user logins, so you'll need OAuth</b>
    * You'll also need a database of some kind in which to store those user preferences.   
    * While your app will not be storing the username/password information, your app *will* update a 
        a table/dictionary of users, keyed by the username.
    * Each time a user logs in, you'll be told by the OAuth provider what that user's login username is; 
        you'll look up the user in that table.  If that user doesn't already exist, you'll create a new
        entry in the table for that user.   

3.  Is your application one that can
    *  give answers *entirely* based on information the user enters during a 
        single session of use, *AND*
    * does *NOT* need to remember anything from one session to the next (only from one page to the next), *AND*
    * respond to user queries based on information that is either freely available online with no authentication, OR
        can be hard-coded in a static file that you keep with your application?
    
    If so, then <b>you probably do NOT need user logins, or OAuth</b>.  You don't need to read the rest of of this page.
    But there are very few webapps for which that is true.
    
# We'll use Github as our OAuth provider, at least initially

If you do need user authentication, I highly recommend using OAuth based on Github as the way to proceed, at least initially.  You can switch to Facebook, Google, Twitter, etc. or add them as additional options later if you so choose.  (There is section below that explains why we are using Github as our initial OAuth provider below.)

# Why Github as our OAuth provider?

Here's why we are using Github as the OAuth provider for our sample applications:

* Everyone in SPIS 2016 has a github account, so everyone in SPIS 2016 will be able to test your application
* For certain applications, we can use the class organization, `ucsd-cse-spis-2016` as a way to further restrict logins 
    only to people that we know (e.g. if we are using personal data or pictures that have been shared with the SPIS 2016
    community, but that members of that community may not wish to be available to the general "github account having" public.)
* Focusing on a single provider for our initial documentation of the process makes things *much* easier.
* The instructional staff has more experience with Github's OAuth system than with the other OAuth providers out there.
 



# Example code: 

Below are two example repos with code for using OAuth Authentication with Github in a Flask Applicaiton.

Each of the repos below requires a bit more explanation---the code won't just "run" without these important configuration steps:

1.  Creating a client_id and client_secret specific to your instance of this application.
    * You have to do this from scratch each time you move the application to a different host or port number
    * That means you have to do this step once for running on your local machine (e.g. `http://127.0.0.1:4000` and 
        a second time if/when you run on Heroku
    * Instructions for creating those are here: [Github OAuth Setup](http://ucsd-cse-spis-2016.github.io/webapps/oauth_github/)
    
2.  Putting the client_id and client_secret, along with perhaps other configuration, into either:
    * an appropriate `env.sh` file (if running locally on ACMS or your own computer), OR
    * the Heroku Config Vars screen (if running on Heroku)
    * Adding an explanation of these two steps to the website is still a TODO ITEM.
    * In the meantime, an instructor or mentor may be able to walk you through it.

Here are the code examples:

* Simple github oauth: <https://github.com/ucsd-cse-spis-2016/spis16-webapps-oauth-example>
    * If you have a github account, you can log in.
    * This app only works with sessions; no connection to a database
    * No ability to store user preferences, or any other persistent data
* Github OAuth based on organization membership: <https://github.com/ucsd-cse-spis-2016/spis16-webapps-oauth-github-org-example>
    * Checks is you have a github account, AND if you are a member of specific github organization specified by the application (e.g. `ucsd-cse-spis-2016`, for example.)
    * Like preceding one, this app only works with sessions; no connection to a database
    * No ability to store user preferences, or any other persistent data

# Using Flask-OAuthlib

[Flask-OAuthlib](https://flask-oauthlib.readthedocs.io/en/latest/index.html) is a Python module that you can use to add 
authentication to your webapp via any OAuth provider.  

In this section, we'll discuss how to use Github as our OAuth provider, since every SPIS 2016 participant has a github account.

## `pip install Flask-OAuthlib`

First, on any system where you want to use this library, you need to install it.

On ACMS, that's 

```
pip install --user Flask-OAuthlib
```

On Mac or Windows, it's probably just

```
pip install Flask-OAuthlib
```

If you run into problems with that, ask a mentor or instructor for assistance.


## Example code


# References

* <https://github-flask.readthedocs.io/en/latest/>


