---
layout: post
title: UCSD CSE SPIS 2016: projects: webapps
---

# UCSD CSE SPIS 2016

Projects: Web Applications (webapps) in Python using Flask


## Intro to webapps with Flask, in four parts


* Part 1: Getting Started with Flask 
* Part 2: Input from URL/pass to function, creating your Heroku Account
* Part 3: Deploying Code on Heroku
* Part 4: Using Templates with your Flask App


## Learning More about HTML

Some useful example webapps:

| Description | Link |
|-------------|------|
| This one illustrates basic templates for pages, CSS, and basic navigation |  https://github.com/pconrad/flask-practice-web-app |
| This one illustrates how to use session |  https://github.com/ucsd-cse-spis-2015/flask-webapp-session-example |
| This one illustrates uploading files | https://github.com/pconrad/heroku-try-file-upload |

## Steps to making an app from scratch—the summary (details elsewhere)
* Make a github repo
* Make subdirectories for templates and static
* Create layout.html, home.html, page1.html and page2.html using patterns on this page: http://flask.pocoo.org/docs/0.10/patterns/templateinheritance/ or this example repo: https://github.com/pconrad/flask-practice-web-app
* Set up static/style.css
* Create the hello.py file that runs it all
* Run and test locally with python hello.py

Example: https://github.com/pconrad/flask-practice-web-app

## To run on Heroku:

* First, you should have a heroku account (create one at heroku.com)
* Add and commit a Procfile and a requirements.txt file to github repo:
* Procfile consists of one line that tells heroku what to do with the repo: 
`web: gunicorn hello:app --log-file=-`
* requirements.txt lists needed Python modules and is created with one command:
`pip freeze > requirements.txt`
* Inside the github repo, run: `heroku login`
* Then run:  `heroku create`
* Then do: `git push heroku master`
* The log messages will contain the URL of your app, which is now deployed.
* You can manipulate the app at the dashboard at heroku.com

## Advanced stuff 

There may or may not be time for this during SPIS.  If not, these are some topics for further study if you want to take your web app further after SPIS is concluded.

### Flask in general:

* The main Flask website: http://flask.pocoo.org/
* Book: Flask Web Development By: Miguel Grinberg Publisher: O'Reilly Media, Inc. Pub. Date: May 8, 2014  Print ISBN-13: 978-1-4493-7262-0
** Full text from on campus at UCSD: http://proquest.safaribooksonline.com/book/programming/python/9781491947586
** From off campus, use the VPN
* The flask Mega-tutorial  http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

## Database stuff:
* You can run sqlite3 by running ~spis15t7/bin/sqlite3
** NOTE: That was installed for SPIS 2015, but would have to be reinstalled for SPIS 2016.

* You can also download precompiled binaries for sqlite3 for windows, mac, linux

* On Heroku, you need Postgres.  
** Info is here: https://devcenter.heroku.com/articles/heroku-postgresql
** To bring up the cli, you type heroku db:psql

## OAuth Stuff (e.g. to login with your Google, Facebook, or Twitter account...)

* http://blog.miguelgrinberg.com/post/oauth-authentication-with-flask

## Web Scraping (getting data from other sites)

Web Scraping with Python By: Ryan Mitchell Publisher: O'Reilly Media, Inc. Pub. Date: July 14, 2015 Print ISBN-13: 978-1-4919-1029-0
Available to read online, on UCSD campus, for free, at:
* http://proquest.safaribooksonline.com/book/programming/python/9781491910283
* To read from off campus, use the VPN
