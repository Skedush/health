"""
Django settings for Health project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

# 不用命令行启动项目部署想不与该配置文件无关

import datetime
import os
import sys
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kz^6p_(@0(le-40zfh^7!99!l7w3qf%-hkez@)w5hr+pivoj!_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

AUTH_USER_MODEL = 'user.User'


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # 使用DRF
    'django_filters',
    'rest_framework.authtoken',  # 设置token
    'rest_framework_swagger',  # 使用swagger
    'drf_yasg',

    # 部署时注释
    'corsheaders',

    'user',
    'title',
    'category',
    'dicEntry',
    'userEntry',
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # 部署时注释
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Health.urls'

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

WSGI_APPLICATION = 'Health.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'health',  # 连接数据库的名称
        'USER': 'root',  # 连接数据库的用户名

        # 部署时换
        'PASSWORD': 'root',  # 连接数据库的密码
        # 'PASSWORD': 'RootAdmin?',  # 连接数据库的密码

        'HOST': '127.0.0.1',  # 连接数据库的地址
        'PORT': '3306',  # 连接数据库的端口
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGES = [
    ('zh-hans', _('Chinese')),
]

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

REST_FRAMEWORK = {"DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.AutoSchema",
                  'DEFAULT_AUTHENTICATION_CLASSES': (
                      #   'rest_framework.authentication.BasicAuthentication',
                      #   'rest_framework.authentication.SessionAuthentication',
                      #   'rest_framework.authentication.TokenAuthentication',
                      # 将token做验证
                      'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
                  ),
                  # 设置所有接口都需要被验证
                  'DEFAULT_PERMISSION_CLASSES': (
                      # ’rest_framework.permissions.IsAuthenticatedOrReadOnly’,
                      #   'rest_framework.permissions.IsAdminUser'
                  ),
                  'EXCEPTION_HANDLER': (
                      'utils.exception.custom_exception_handler'
                  )
                  }
SECRET_KEY = 'health'
# 设置过期时间
JWT_AUTH = {
    # token 有效期
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=8),
    # 'JWT_AUTH_HEADER_PREFIX': 'TOKEN',  # 在 http头 中的 开头， 默认为 JWT ，可以修改
    'JWT_ALLOW_REFRESH': True,
    # 续期有效期（该设置可在24小时内带未失效的token 进行续期）
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(hours=24),
    # 自定义返回格式，需要手工创建
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'utils.responseUserLogin.jwt_response_payload_handler',
    'JWT_SECRET_KEY': SECRET_KEY,  # jwt 生成 token 所使用的 key 。
}

# 下面是新增的配置
STATICFILES_DIRS = [
    # 指定文件目录，BASE_DIR指的是项目目录，static是指存放静态文件的目录。
    os.path.join(BASE_DIR, 'static'),
]
# 迁移静态文件的目录,这个是线上是需要使用的 python manage.py collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'static/static')


SWAGGER_SETTINGS = {
    # 'LOGIN_URL': 'rest_framework:login',
    # 'LOGOUT_URL': 'rest_framework:logout',
    # 'DEFAULT_INFO': 'beatop.urls.swagger_info',
    'USE_SESSION_AUTH': False,
    # 'SHOW_EXTENSIONS': False,
    'DOC_EXPANSION': 'none',  # none/list/full
    'SECURITY_DEFINITIONS': {
        # 'basic': {
        #     'type': 'basic'
        # },
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    }
}

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    ['http://127.0.0.1:*']
)
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
CORS_ALLOW_HEADERS = (
    '*'
)

# 部署时注释
ALLOWED_HOSTS = "*"
