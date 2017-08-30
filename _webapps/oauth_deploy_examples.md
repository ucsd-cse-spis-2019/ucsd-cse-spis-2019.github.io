---
topic: "OAuth: Deploy"
desc: "Deploying the OAuth Code on localhost, and Heroku"
indent: True
---

This page describes how to deploy OAuth Code on localhost and Heroku.
After you follow these steps, you should be able to access your wep application through the heroku URL and log users in/out.

**NOTE: If you are working on your local machine, make sure to install heroku before using it in the command line. Simply type this in the command line to install heroku.
```
brew install heroku
```

# Step 1
First make sure you are in the directory with all your web app files.
1. heroku login
2. heroku create
   * You only need to do “heroku create” once for your web app. You are basically initializing the connection between your web application and heroku.
   * Save the link that ends with herokuapp.com. This heroku URL will be used to register your OAuth. 
3. git push heroku master
   * Do this step every time you want to push your code, so basically whenever you make changes to your code


