"""
Django settings for robosats project.

Generated by 'django-admin startproject' using Django 4.0.
WATCH OUT RoboSats backend was later downgraded to Django 3.2 (compatibility with existing plugins!)

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
import textwrap
from pathlib import Path

from decouple import config

from .celery.conf import *  # noqa

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = "/static/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

DEBUG = False
STATIC_URL = "static/"
STATIC_ROOT = "/usr/src/static/"


# SECURITY WARNING: don't run with debug turned on in production!
if config("DEVELOPMENT", default=False):
    DEBUG = True
    STATIC_ROOT = "frontend/static/"

AVATAR_ROOT = STATIC_ROOT + "assets/avatars/"

ALLOWED_HOSTS = [
    config("HOST_NAME"),
    config("HOST_NAME2"),
    config("I2P_ALIAS"),
    config("I2P_LONG"),
    config("LOCAL_ALIAS"),
    "127.0.0.1",
    "localhost",
]

CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = [
    f'http://{config("HOST_NAME")}',
    f'http://{config("HOST_NAME2")}',
    f'http://{config("I2P_ALIAS")}',
    f'http://{config("I2P_LONG")}',
    f'http://{config("LOCAL_ALIAS")}',
    "http://localhost",
    "http://*.onion",
    "http://*",
    "https://*.com",
    "https://*",
]

# Allows Session Cookie to be read by Javascript on Client side.
SESSION_COOKIE_HTTPONLY = False

# Logging settings
if os.environ.get("LOG_TO_CONSOLE"):
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "WARNING",
        },
        "loggers": {
            "api.utils": {
                "handlers": ["console"],
                "level": "WARNING",
            },
        },
    }

# Application definition

INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "channels",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "django_celery_beat",
    "django_celery_results",
    "import_export",
    "api",
    "chat",
    "control",
    "frontend.apps.FrontendConfig",
    "drf_spectacular",
    "drf_spectacular_sidecar",  # required for Django collectstatic discovery
]

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "RoboSats REST API v0",
    "DESCRIPTION": textwrap.dedent(
        """
        REST API Documentation for [RoboSats](https://learn.robosats.com) - A Simple and Private LN P2P Exchange

        <p style='background-color:#fff0f0;padding:16px;border-radius:6px;border:2px solid #ffd3d3'>
        <span style='color:#f31f1f;font-weight:bold'>Note:</span>
        The RoboSats REST API is on v0, which in other words, is beta.
        We recommend that if you don't have time to actively maintain
        your project, do not build it with v0 of the API. A refactored, simpler
        and more stable version - v1 will be released soon™.
        </p>

        """
    ),
    "VERSION": "0.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",  # shorthand to use the sidecar instead
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_UI_SETTINGS": {
        "expandResponses": "200,201",
    },
    "EXTENSIONS_INFO": {
        "x-logo": {
            "url": "https://raw.githubusercontent.com/Reckless-Satoshi/robosats/main/frontend/static/assets/images/robosats-0.1.1-banner.png",
            "backgroundColor": "#FFFFFF",
            "altText": "RoboSats logo",
        }
    },
    "REDOC_DIST": "SIDECAR",
}


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "robosats.urls"
IMPORT_EXPORT_USE_TRANSACTIONS = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "robosats.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST"),
        "PORT": config("POSTGRES_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
ASGI_APPLICATION = "robosats.routing.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [config("REDIS_URL")],
        },
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config("REDIS_URL"),
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
