# Django settings for climbtime project.
import mongoengine
from django.core.urlresolvers import reverse

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
     'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'climbtime'
    }
}

FACEBOOK_EXTENDED_PERMISSIONS = ['email']


SESSION_ENGINE = 'mongoengine.django.sessions' # optional

AUTHENTICATION_BACKENDS = (
    ##'mongo_auth.backends.LazyUserBackend',
    #'mongo_auth.backends.MongoEngineBackend',
    #'mongo_auth.backends.FacebookBackend',
    'mongoengine.django.auth.MongoEngineBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

#AUTH_USER_MODEL = 'mongo_auth.MongoUser'
#SOCIAL_AUTH_USER_MODEL = 'mongoengine.django.auth.User'
#MONGOENGINE_USER_DOCUMENT = 'mongoengine.django.auth.User'
#SOCIAL_AUTH_MODELS = 'social_auth.db.mongoengine_models'

#AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'


MONGODB_USER = 'lehel'
MONGODB_PASSWD = 'Kovach789'
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
_MONGODB_NAME = 'climbtime'
#_MONGODB_DATABASE_HOST = 'mongodb://localhost/climbtime'
_MONGODB_DATABASE_HOST = 'mongodb://localhost/climbtime'
    #% (_MONGODB_HOST, _MONGODB_NAME)
MONGODB_DATABASE = 'climbtime'


#mongoengine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)
mongoengine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/concepts/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = 'C:/Users/Dorian/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-2c61ba15x(eau&7f0cm1a_$0m1nayy$3hu*_^ig$g44beo!pb'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'mongo_auth.middleware.LazyUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'climbtime.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'climbtime.wsgi.application'

import os
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)

INSTALLED_APPS = (
    'django.contrib.auth',
	 'mongoengine.django.mongo_auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
	'concepts',
    'tastypie',
    'tastypie_mongoengine',
    'regme',
    'social_auth',
)

TEMPLATE_CONTEXT_PROCESSORS = (
#"django_browserid.context_processors.browserid_form",
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
'django_facebook.context_processors.facebook',
'django.core.context_processors.request',
)

ACCOUNT_ACTIVATION_DAYS = 7
SITE = {'domain': 'domain.tld', 'name': 'Climbti.me'}

SESSION_ENGINE = 'mongoengine.django.sessions'
ESSION_SERIALIZER = 'mongoengine.django.sessions.BSONSerializer'

LOGIN_URL = '/concepts/login'

MONGOENGINE_USER_DOCUMENT = 'regme.documents.User'




# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

APPEND_SLASH = True

FACEBOOK_APP_ID = '1522657234624624'
FACEBOOK_APP_SECRET = 'e980533911cf9d3c309b22e1d34f59cc'
FACEBOOK_API_SECRET = 'e980533911cf9d3c309b22e1d34f59cc'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'