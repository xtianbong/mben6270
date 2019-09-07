# WLU - CP202
This repository contains all the code and lectures for CP202 (Fall 2019).

If you have any questions, email jsandoval@wlu.ca.

# Running Locally
You need to clone the repository and run the site in your local web server. The following steps will help you set up the software required to run locally. 

<h2>Step 1</h2>

You need to clone the repository. You clone the repo using git. You may already have git installed. To verify you have git installed, run the following command:
```
$ git --version
```

If you get something that looks like the following, you already have it installed:
```
git version 2.12.2
```

If you need to isntall git, you have different options. I recommend you use the appropiate installer for your OS from https://www.atlassian.com/git/tutorials/install-git.

When you're done installing and verifying that it runs properly, clone the repository with the following command (you can choose any convinient directory):

```
$ git clone https://github.com/josefelixsandoval/wlu.git
```

<h2>Step 2</h2>
If you already have a web server installed in your machine, go to Step 4.

To run a local web server, you have multiple options. I'll give you two.

**Python Built-in Web Server**\
If you are running MacOS (or have Python installed in your Windows machine), Python comes with a built-in web server. To run the web server go to the desired directory (or folder) in a Terminal shell window and run the following command:

```
$ python -m http.server
````

You then can view your local website by going to the following address in your web browser:

```
http://localhost:8000/
```

If you don't have python installed and would like to use the built-in server, intall the latest version of Python and then run the command above. You can find the latest version here https://www.python.org/downloads/

**Node.js Web Server**\
If you have Node.js and the http-server already module installed, skip the installation part just run the http-server command as listed in item 3 here.

To install Node.js:

1. Go to https://nodejs.org/en/download/ and download and install node.
2. Open a shell terminal or command prompt (in Windows) and install http-server with the following command:

```
$ npm install http-server -g
```

3. Run the following command, after you are in your desired directory:

```
$ http-server -p 8000
```

To view your local web server, point your browser to the following URL:

```
http://localhost:8000/
```


<h2>Step 3</h2>
After you have cloned this repository, go to the root directory of the repository and run your prefered web server. For example, my local version of the site is in the following directory:

```
$ cd /User/jose/Documents/WLU
```

I then run the build-in Python web server as follows:

```
$ python -m http.server
```

If everything has been set up properly, point your web browser to:

```
http://localhost:8000/
```

You should see the homepage for the site (I'll be updating it weekly, but it should look something like this:

![Home Page](http://wlu-cp202.appspot.com/img/homepage.png)
