import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-q=ats3@75$2o$!tn#c32+$syg9os#25f^vn2x#_e6n#)8$5i5f'

DEBUG = False

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'app1',
    'robots'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
WSGI_APPLICATION = 'portfolio.wsgi.application'
ROBOTS_USE_SITEMAP = True
ROBOTS_SITEMAP_VIEW_NAME = 'cached-sitemap'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SITE_ID = 1

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    'http://localhost:3000',
    'http://192.168.43.33:3000',
    'https://api.razorpay.com',
    'http://44.202.70.45',
    'https://bitdev.live',
    'http://bitdev.live'
]
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:3000",
    'http://localhost:3000',
    'http://192.168.43.33:3000',
    'https://api.razorpay.com',
    'http://44.202.70.45',
    'https://bitdev.live',
    'http://bitdev.live'
]
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
SECURE_REFERRER_POLICY = "no-referrer-when-downgrade"

CORS_ORIGIN_ALLOW_ALL = True
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_DIRS = [os.path.join(BASE_DIR, 'media')]

# my config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "speedapibot@gmail.com"
EMAIL_HOST_PASSWORD = "shsgssjpnjyznqjk"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
