# Django project site specific settings
# All non site specific settings should go into the settings.py file
# Copy this file as settings_local.py and adjust it to your site.
# The settings_local.py contains only site specific information and should not
# be part of the svn repository of the project. It should be part of the
# hosting svn repository.

DEBUG = True #TODO set to off for live, staging and preview
TEMPLATE_DEBUG = DEBUG

#TODO: replace localhost with the domain name of the site
DEFAULT_FROM_EMAIL = 'django_errors@circmanager.com'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

ADMINS = (
    ('Ross Merriam', 'rossmerriam@gmail.com'),
    ('Mitch LeBlanc', 'supermitch@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # 'postgresql_psycopg2', 'postgresql', 'mysql', 'oracle'
        'NAME': 'database.db',           # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


TIME_ZONE = 'America/Vancouver'

ROOT_URLCONF = 'urls_dev' #TODO: remove this on production

INTERNAL_IPS = ('127.0.0.1', )

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/' #TODO: on production (full URL to the media server)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Allows for certain Django apps to be installed on a local basis,
# independent of INSTALLED_APPS in the main settings.py file.
LOCAL_INSTALLED_APPS = (
)
