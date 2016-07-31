---
topic: Github resources
desc: "Resource for using github"
---

# Github

* Create your account at github.com.  
 - To get the educational discount (free access to private repos), use an email that ends in .edu

* Configure git on the ieng6 servers and setup your ssh key following [these instructions](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/). Refer to the next section for using github to complete lab assignments

# Using github to complete lab assignments

Git is a version control system that allows you to keep a historical record of all the changes you make to your code and have access to your programs on any computer!

Below are a set of instructions that are common to completing all of the lab assignments

## Creating your github repo

We ask that you create a new private github repo for each lab assignment.
You and your partner will share the same repo by following these instructions

1. Navigate to the [ucsd-cse-spis-2016 organization](https://github.com/ucsd-cse-spis-2016)

2. Click on the "New repository" button to create a new repo as shown below: 

   ![new repo](/images/new-repo-begin.png)

3. Create a new repo for the lab assignment that you would like to start following the prescribed naming convention. For example, if the repo is for lab04, your name is Phill and your partner's name is Diba, then name your repo "spis16-lab04-Phill-Diba". Select the "private" option when creating your repo to make sure your repo is only visible to the collaborators (you and your partner) and the course instructors. Click on the "Create repository" button. See the screenshot below:
	
	![new repo](/images/create-new-repo.png)

4. For each lab we have provided you with some starter code. To obtain the starter code, click on the "import code" button on the screen that follows right after you create a new repo. Then provide the url of the repository that contains the starter code. This url should be specified in the assignment writeup. The screenshot below shows what you should expect to see if you were importing the starter code for lab04: 
	
	![new repo](/images/import-code1.png)![new repo](/images/import-code2.png)

5. Set up your ssh key. You need to do this step only once and should not repeat it for each assignment. Log into your account on ieng6 and setup your ssh key by following these tutorials in order: a) [Generate a new ssh key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) Note: Don't enter a passphrase for now b) [Copy your ssh key to github](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)

6. Its now time to make a copy of your repo on the computer where you intend to work. We strongly recommend that you create this copy on one of the ieng6 servers (e.g. ieng6-240.ucsd.edu). The process of creating a copy of your repo is called cloning because you not only get a replica of your code on a difference machine but can reflect changes made in one clone repo to any other clone using the mechanisms that Git provides. This is a key feature that essentially allows you to work on the same version of your code from any computer. For now, we are interested in working on the ieng6 servers, so that's where you will create the clone. To clone your repo navigate to your repo on github and click on the green "clone or download" button on the top right corner. Clicking on this link gives you either an ssh or https address that you will need in the cloning process clone. Copy the ssh address with starts with a `git@`. See the screenshot below: 
	
	![new repo](/images/get-repo-url.png) 
	Log into your account on ieng6 and clone your newly created repo using the git clone command as in the following example:

	```
      $ git clone git@github.com:ucsd-cse-spis-2016/spis16-lab04-Phill-Diba.git

	```
	Make sure you provide the address to your repo instead of the one provided above. To check if your repo has been cloned correctly, type `ls` on the command prompt and you should see a directory with your repo name. Navigate into that directory using the `cd` command. For example if the directory name is `spis16-lab04-Phill-Diba`, at the command prompt type `cd spis16-lab04-Phill-Diba`


## Submitting your code via github

We recommend that you keep your repo on the git server up to date with the latest version of your code. This allows your mentor to give you timely feedback as you progress through the assignments. To do this follow these steps:

1. Stage all the files that have changed using the command `git add .`. 

2. Commit your changes using the command `git commit -m "Customize this message that summarizes your latest changes" `. 

3. Push your changes to github by typing the command `git push`. Your changes will not be visible to your mentor unless you do this final step.

## Git cheatsheet

For more information on git commands refer to [this resource](http://zeroturnaround.com/rebellabs/git-commands-and-best-practices-cheat-sheet/) and the cheat sheet given below:

![http://zeroturnaround.com/wp-content/uploads/2016/05/Git-Cheat-Sheet-by-RebelLabs.png](http://zeroturnaround.com/wp-content/uploads/2016/05/Git-Cheat-Sheet-by-RebelLabs.png){:height="1000px" width="1000px"}
