---
topic: Github resources
desc: "Resource for using github"
---

# Github

* Create your account at github.com.  
 - To get the educational discount (free access to private repos), use an email that ends in .edu

* Configure git on the ieng6 servers and setup your ssh key following [these instructions](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/). Refer to the next section for using github to complete lab assignments

# Using github for completing lab assignments

Git is a version control system that allows you to keep a historical record of all the changes you make to your code and have access to your programs on any computer!

Below are a set of instructions that are common to completing all of the lab assignments

## Creating your github repo

We ask that you create a new private github repo for each lab assignment.
You and your partner will share the same repo by following these instructions

1. Navigate to the [ucsd-cse-spis-2016 organization](https://github.com/ucsd-cse-spis-2016)

2. Click on the "New repository" button to create a new repo as shown below: ![new repo](/images/new-repo-begin.png)

3. Create a new repo for the lab assignment that you would like to start following the prescribed naming convention. For example, if the repo is for lab04, your name is Phill and your partner's name is Diba, then name your repo "spis16-lab04-Phill-Diba". Select the "private" option when creating your repo to make sure your repo is only visible to the collaborators (you and your partner) and the course instructors. Click on the "Create repository" button. See the screenshot below:![new repo](/images/create-new-repo.png)

4. For each lab we provide you with some starter code. To obtain the starter code, click on the "import code" button on the screen that follows right after you create a new repo. Then provide the url of the repository that contains the starter code. This url is given in the assignment writeup. As an example see the screenshot below for importing the starter code for lab04: ![new repo](/images/import-code1.png)![new repo](/images/import-code2.png)

5. Clone your repo either over https or ssh. Note to use ssh, you have to setup your ssh key. First get the https or ssh address of your git repo by navigating to your repo on github and clicking on the green "clone or download" button on the top right corner. Copy the https or ssh address of your repo. See the screenshot below: ![new repo](/images/get-repo-url.png)

6. Log into your account on ieng6 and clone your newly created repo using the git clone command. See the example below for cloning your repo over https: 

```
      $ git clone https://github.com/ucsd-cse-spis-2016/spis16-lab04-Phill-Diba.git

```



* http://zeroturnaround.com/rebellabs/git-commands-and-best-practices-cheat-sheet/

![http://zeroturnaround.com/wp-content/uploads/2016/05/Git-Cheat-Sheet-by-RebelLabs.png](http://zeroturnaround.com/wp-content/uploads/2016/05/Git-Cheat-Sheet-by-RebelLabs.png){:height="1000px" width="1000px"}
