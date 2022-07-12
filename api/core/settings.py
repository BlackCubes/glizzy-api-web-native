# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@pws2)=_mca+!qmlt@pl%ub3ir7n7kuiyma!u$2s62(2@vo6p-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []





# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}








