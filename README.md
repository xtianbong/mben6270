# WLU - CP202
This repository contains all the code and lectures for the Fall 2019 CP202 class.

If you have any questions, email jsandoval@wlu.ca.

# Running Locally
Before you are able to run the site locally, you will need to install a web server in your machine. If you already have a local web server skip Step 1.

<h2>Step 1</h2>

You have multiple options to set up a web server locally. 

**Python Built-in Web Server**

If you are running MacOS (or have Python installed in your Windows machine), Python comes with a built-in web server. To run the web server go to the desired directory (or folder) in a Terminal shell window and run the following command:

```
python -m http.server
````

You can view your local website by going to the following address in your web browser:

```
http://localhost:8000/
```

If you are using a Windows machine and you would like to use Python's web server, you can install the latest version of Python and then run the command above (if you already have Python installed in your Windows machines, just run the command above).

**Node.js Web Server**

1. Go to https://nodejs.org/en/download/ and download and install node.
2. Open a shell terminal or command prompt (in Windows) and install http-server with the following command:
```
npm install http-server -g
```
3. Run the following command, after you are in your desired directory:
```
http-server -p 8000
```
To view your local web server, point your browser to the following URL:
```
http://localhost:8000/
```

<h2>Step 2</h2>
1. Clone this repository.
2. Run your local web server in the directory of the cloned repository.
3. Go to:
```
http://localhost:8000/
```

At this point, you should see the homepage for the site (I'll be changing the homepage from time to time, but it should look something like this:

![Home Page](http://wlu-cp202.appspot.com/img/homepage.png)



