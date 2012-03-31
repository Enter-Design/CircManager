# Django HTML5 Boilerplate

## Introduction

This is a starting template for Django website projects using (a slightly modified version of)
[HTML5 Boilerplate](http://html5boilerplate.com).



## Features

* A Django project skeleton
* A slightly now less modified version of the HTML5 Boilerplate
* django.contrib.staticfiles url conf set up for serving static media
* A `settings_local.py.ex` template file that allows you to set environment-specific settings
* Requirements files for pip (details below)


## How to use the template
### For setup on local.
Set up your settings_local.py file:

        # set path
        cd <path-to-project>/

        python manage.py syncdb

Once that's completed you can boot up the dev server:

        python manage.py runserver

Then open up your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000) -- if all went well you should see the "It works!" page.


## A note about humans and robots

HTML5 Boilerplate includes humans.txt and robots.txt files. I deleted them as managing these files were outside of my intended scope.