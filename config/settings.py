"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os, sys
import datetime
# mysql을 사용하기 위해 추가함
# import pymysql
# pymysql.install_as_MySQLdb()

import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# # for Angular
# CLIENT_DIR = os.path.join(os.path.join(BASE_DIR, '../ys_angular_test/'), 'my-view')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9drsi=_reh-0umq6@i$&kqkz)%^uy52%rd(x-=&3*8+h@c39q7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['localhost', '192.168.0.134']
ALLOWED_HOSTS = ['*']


# Application definition
DJANGO_APPS = [
    'jet',
    'jet.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'django_countries',
    'django_seed',
    'django.contrib.sites',
]

INSTALLED_DJANGO_APPS = [
    'whitenoise.runserver_nostatic',

    'rest_framework',
    'rest_framework.authtoken',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',

    'rest_auth',
    'rest_auth.registration',
    'corsheaders',
]

PROJECT_APPS = [
    'core.apps.CoreConfig',
    'users.apps.UsersConfig',
    'freeboards.apps.FreeboardsConfig',
    'movies.apps.MoviesConfig',
    'rooms.apps.RoomsConfig',
    'reviews.apps.ReviewsConfig',
    'reservations.apps.ReservationsConfig',
    'lists.apps.ListsConfig',
    'conversations.apps.ConversationsConfig',

    'app.reference',
    'app.test_app'
]

INSTALLED_APPS = DJANGO_APPS + INSTALLED_DJANGO_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        # 'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb',
        'USER': 'root',
        'PASSWORD': 'bcg062817!',
        'HOST': '192.168.0.20',
        'POST': '3306',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'trans',
#         'USER': 'root',
#         'PASSWORD': 'ysnam007!*!',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

AUTH_USER_MODEL = 'users.User'

MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")

MEDIA_URL = "/media/"

# for Angular
# STATICFILES_DIRS = [
#     os.path.join(CLIENT_DIR, 'dist/my-view'),
# ]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # 포맷터
    # 로그 레코드는 최종적으로 텍스트로 표현됨
    # 이 텍스트의 포맷 형식 정의
    # 여러 포맷 정의 가능
    'formatters': {
        'format1': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
        'format2': {
            'format': '%(levelname)s %(message)s'
        },
    },

    # 핸들러
    # 로그 레코드로 무슨 작업을 할 것인지 정의
    # 여러 핸들러 정의 가능
    'handlers': {
        # 로그 파일을 만들어 텍스트로 로그레코드 저장
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/logfile'),
            'formatter': 'format1',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },

    # 로거
    # 로그 레코드 저장소
    # 로거를 이름별로 정의
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',

        },
    }
}


CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = [
#    "http://127.0.0.1:4200",
# ]

# CORS_ORIGIN_REGEX_WHITELIST = [
#     r"^https://\w+\.example\.com$",
# ]

# CORS_ALLOW_METHODS = [
#     'DELETE',
#     'GET',
#     'OPTIONS',
#     'PATCH',
#     'POST',
#     'PUT',
# ]

# CORS_ALLOW_HEADERS = [
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
# ]

# # This combines automatic compression with the caching behaviour provided by Django’s ManifestStaticFilesStorage backend.
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# #  If you want to apply compression but don’t want the caching behaviour then you can use:
# # STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'



JET_DEFAULT_THEME = 'light-gray'
JET_SIDE_MENU_COMPACT = False


REST_SESSION_LOGIN = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

REST_USE_JWT = True


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    )
}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'users.serializers.UserDetailSerializer'
}

JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=48),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(hours=48),

    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}