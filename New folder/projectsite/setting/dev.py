from projectsite.settings import *





# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%#_g-stl0m3$_d-pallu00av7n*$7gjw2ybc%wj(l87sef^a+l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


#INSTALLED_APPS=[]

#site frameworks
SITE_ID=2


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_URL = '/static/'
STATIC_ROOT= BASE_DIR/'static'

MEDIA_URL = '/media/'
MEDIA_ROOT= BASE_DIR/'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
