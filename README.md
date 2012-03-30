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

Set up your settings_local.py file:

        # set path
        cd <path-to-project>/
         
        # copy settings_local.py
        cp settings_local.py.ex settings_local.py
        
        # Edit settings_local.py
        vim settings_local.py
        

After you configure your local settings (database, etc.) you're ready to run `syncdb`:

        python manage.py syncdb

Once that's completed you can boot up the dev server:

        python manage.py runserver

Then open up your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000) -- if all went well you should see the "It works!" page.


## A note about humans and robots

HTML5 Boilerplate includes humans.txt and robots.txt files. I had thought about including a method for serving those files with this project but decided that the most appropriate way to do so was not through Django but through your web server (be it, Apache, nginx or what have you). They are included for your convenience in the `config/` folder, but it's up to you to ensure that they're served properly.
