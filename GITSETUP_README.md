# WLU - CP202 - GitHub and Git - Part 2 of Quiz 1
This guide will help you create your first local Git repository and push all your changes to GitHub.

Note that setting up a GitHub account and local Git repository counts ast 2.5% of your total mark as part 2 of Quiz 1 (the total weight of Quiz 1 is 5%).

# Setup GitHub
If you already have a GitHub account, create a repository with your WLU username as the name of the repo and continue with Steps 3 and 4. For example, my repo would be named 'jsandoval.'

Note that you only need to do Steps 1 and 2 if you *do not* have a GitHub account.

## Step 1
Signup for a GitHub account at https://github.com/. Make sure to signup for the free version. Your signup option should look as follows:

![](http://wlu-cp202.appspot.com/img/GitHubSignUp.png)

## Step 2
When you verify your email address, you'll get the chance to create a new repository. Use your WLU username as the name for your first repository and make sure the repo is public. Your first repo creation form should look similar to the following image (for example, my repo would be named 'jsandoval'):

![](http://wlu-cp202.appspot.com/img/GitHubFirstRepo.png)

## Step 3
In your command line, type in the following commands. On the first 'push' you will need the email address and password you provided in Step 1; also note you can create a new directory for your repo. In my case, my commands look as follows:

**Note that wherever you see references of Jose in the commands, you must use your own credentials and names you used to create your account and repo.**

```
$ mkdir wlu
$ cd wlu
$ echo "# [THIS SHOULD BE YOUR WLU USERNAME]" >> README.md
$ git init
$ git add README.md
$ git commit -m "first commit"
$ git remote add origin https://github.com/wlu-josesandoval/jsandoval.git
$ git push -u origin master
```
Note that these are the same commands shown during your setup process. The screen shot looks as follows:

![](http://wlu-cp202.appspot.com/img/GitHubFirstPush.png)

## Step 4
Copy the link of your repository and submit here https://forms.gle/t55Aiw4bvBpHPtNy8
