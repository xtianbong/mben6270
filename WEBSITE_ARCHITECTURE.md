# Website Architecture

In our class we'll cover mainly what a website looks like locally, i.e., HTML files, images, css, JavaScript, etc. However,
website architecture is a major field in software engineering.

# Folder structure

Folder structure matters for web design and development. It aligns with good software engineering concepts.

The details of software engineering concepts are out of the scope of this class, however, we will study **coupling** and
**cohesion** and they apply to CP202.

Our understanding of coupling and cohesion will help us understand why separating code into a well structure and well named
directories and files leads to the successful deployment and maintenance of a website.

For example, we'll answer, more technically, why we don't just put all the files in one directory and why we can't just name
files arbitrarily.

**Coupling**
Coupling relates to the interdependence of modules that make up a program. **Our aim is low coupling**.

In the context of this class it means that sections of a website are not inter-related.

For example, if one CSS style definition is used in the main section, changing it won't affect any of the sub sections
in the site.

Similarly, if JavaScript code used in one of the subsections changed, low coupling guarantees that other sections won't break.

**Cohesion**
In simple terms it refers to how closely related all the elements of a module are. **We are aiming for high cohesion**.

For our class it means that sections of a website that belong together **must** stay together.

For example, if one snippet of code that is used for a menu in one subsection, that snippet of code **must not** be located
in a different subsection's directory.

For example, consider we have 2 subsections in a website, one name *jobs* and the other *projects* and the
code looked like this:

```
www/jobs/index.html
        /jobs_menu.html
        /right_column.html

www/projects/index.html
            /projects_menu.html
            /right_column.html
```

Nothing from section *jobs* should be using code from *projects* and vice versa. More important, **nothing**
from section *jobs* should be located in the directory for *projects* and vice versa.

In the context of this class, these must be our main tenet:

> Low coupling, high cohesion.

Simplistically, files for a section must stay in the same directory and they should be only related to that section.

# Larger Example
Assume 3 sections in a site, namely, 'jobs', 'preview', and 'projects'. Our tree structure would look something like this:

```
www/
   /index.html
   /css
      /styles.css
      /special_styles.css
      /imgage_styles.css
   /img
      /header.jpg
      /footer.jpg
      /left_image.jpg
      /right_image.jpg
   /js
     /app.js
     /math.js
     /spelling.js
   /video
        /intro_video.webm
        /main_video.webm
        /end_video.webm
   /jobs/
        /index.html
        /1.html
        /2.html
        /3.html
        /css/
            /jobs_styles.css
        /img
            /jobs_left_image.jpg
            /jobs_right_image.jpg
        /js
        /video
        /jobs_future
                   /img
                      /jobs_future_left_colum.png
   /projects
           /index.html
           /css
              /projects_styles.css
           /img
              /projects_footer.png
           /js
             /projects_app.js
           /video
           /projects_current/
                            /index.html
                            /css
                            /img
                            /js
                            /video
                                 /projects_current_cp202
                                                       /index.html
```

Can you use a different structure? Yes, for your own work. **BIG NO** for this class.

Use the guidelines I'm giving you. They are more or less industry standards and
if someone sees your well structured site, they will know you mean business.

But in the wild, you can have your own naming and structure standards, however, you'll have to adhere to whatever
software development standards are in place.

If you do what I suggest here, chances are you will fit right in.

# Bad Example

Imagine having all your files in the same directory. For example, take a 'jobs' and 'projects' directory. Each directory
contains and index.html file. Let's collapse the structure.

If 'jobs' has an index.html file and 'projects' has an index.html file, what does it look like with the two files in one
directory?

If they both live in the same directory, which is which?
index.html
index.html

Now you have to name one of them to something else. But which one would you rename?

What if you had 6 section and each section had 10 files each. Now you'd have 60 files in the same directory and you don't
know which file is for which section, unless you look inside of the file.

# Friendly URLs and Vanity URLs
In practice your directory structure should give you the context and a logical breakdown of your site.

Your directory structure is the architecture of your site.

In most cases, the directory structure gives URL friendly names. Let's say my website is wlustudent.com. And I have 3
sections: 'classes', 'resume', 'interests'.

I would breakdown my site following the guidelines above and it would look as follows:

Note that each subfolder will have its own index.html file.

```
www/
   /index.html
   /css
   /js
   /img
   /classes
          /index.html
   /interests
            /index.html
   /resume
         /index.html
```

Accessing each section of the site already has a friendly URL and an SEO friendly URL.

Easy to remember: you can easily tell someone, "My resume is at wlustudent.com/resume."

Aside note: web servers can be configured to generate SEO and readable URLs. They are called vanity URLs.

Vanity URLs are outside of the scope of this class, but you can request your website administrator (they used to be called web
master) to configure a vanity URL for you. As a web designer you must have this option.

For example, let's say your interest are painting and you want to promote yourself as a painter, then you'd
prefer to have a URL called *wlustudent.com/painter* and not *wlustudent.com/interests*.

As a proper developer and designer, you **will not** go to your website and rename the directory *interest* to *painter*.
Changing the name changes the site, and it changes the code, and that means you need to refactor code and test all over again.

What you do, is request a mapping to your desired URL.

In the background, inside the web server, there's some configuration that maps the real URL to a virtual one.
Something like this (this will not be in exams):

```
 RewriteRule ^interest(/)?$ /painter/ [R]
```

* This would be a line inside some configuration of the Apache web server.

# Naming Conventions For This Class
In theory, you can name your files and directories whatever you want. However, for this class and for your future sanity,
use the following naming convention:

- Assume a sub section called *resume*

| Item                             |      Name     |
| -------------------------------- | -------------- |
| Main directory                   | **www**        |
| Main file                        | **index.html** |
| Directory name for sub section   | **resume**     |
| Main file inside of sub section  | **index**.html |
| CSS directory                    | **css**        |
| JavaScript directory             | **js**         |
| Image directory                  | **img**        |

# References
https://httpd.apache.org/docs/trunk/rewrite/remapping.html
