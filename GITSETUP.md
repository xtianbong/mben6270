# WLU - CP202 - GitHub and Git
This guide will help you create your first local Git repository and push all your changes to GitHub.

If you have any questions, email jsandoval@wlu.ca.

# Setup GitHub
If you already have a GitHub account, create repository with your WLU username as the name of the repo and go to number 3. For example, my repo would be named:

```
jsandoval
```

## Step 1
Gignup for a GitHub account at https://github.com/. Make sure you to sign up for the free version. You're sign up option should look as follows:

GitHubSignUp.png

## Step 2
When you verify your email address, you'll get the chance to create a new repository. Use your WLU username as the name for your first repository and make sure the repo is public. Your first repo creation form should look similar to the following image:

GitHubFirstRepo.png

## Step 3
In your command line, type in the following commands (on the first 'push' you will need the email address and password you provided in Step 1):

```
echo "# jsandoval" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/wlu-josesandoval/0001_JoseSandoval.git
git push -u origin master
```
Note that these are the same commands shown during your setup process. The screen shot looks as follows:

GitHubFirstPush.png

## Step 4
Copy your repository's link and submit it. 
