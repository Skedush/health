from .common import *


INSTALLED_APPS = [
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
    'user',
    'title',
    'category',
    'dicEntry',
    'userEntry',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'health',  # 连接数据库的名称
        'USER': 'root',  # 连接数据库的用户名
        'PASSWORD': 'RootAdmin?',  # 连接数据库的密码
        'HOST': '127.0.0.1',  # 连接数据库的地址
        'PORT': '3306',  # 连接数据库的端口
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
