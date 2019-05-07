"""
Django settings for DjoSiteDba project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm6*_l!wu_wm-gzt7!8r42r%^2687yu4oh7klqy31do+lw9-fsq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

'''
# SET WOKRING ENV AND DB PASSWORD
# COULD SET MULTIPUL TARGET SERVER
# index: USING INDEX EXPRESS DIFFERENT WORK-TARGET SYSTEM, such as PC or Server
# Different working environment might adapt variance db names.
'''
_SERVER_HOSTNAME_SET = [{'att': 'svr', 'name': 'iZbp1iil3e0qqrfbczpmkhZPGS-20180113SZM ', 'index': 1},
                        {'att': 'pc', 'name': 'ZJLPC', 'index': 2},
                        {'att': 'pc', 'name': 'PGS-20180113DJZ', 'index': 3},
                        {'att': 'pc', 'name': 'PGS-20180113SZM', 'index': 4},
                        {'att': 'pc', 'name': 'kickseed', 'index': 5},
                        {'att': 'fssvr', 'name': 'fsg0518', 'index': 6},  # fs鏈嶅姟鍣�
                        ]
PasswordSetFlag = False
LOCAL_HOSTNAME = socket.gethostname()
# ip = socket.gethostbyname(LOCAL_HOSTNAME)
# print(LOCAL_HOSTNAME)
# print(ip)
LOCAL_WK_TARGET = 1
LOCAL_DB_PASSWORD = '123456'
DB_HOST = "db"
DB_PORT = 3306
print(LOCAL_HOSTNAME)
for element in _SERVER_HOSTNAME_SET:
    if (element['name'].find(LOCAL_HOSTNAME) >= 0) and (element['name'] == 'iZbp1iil3e0qqrfbczpmkhZ'):
        # IS_FORMAL_DEPLOYMENT = True
        LOCAL_DB_PASSWORD = 'xiaohui@bxxh'
        LOCAL_WK_TARGET = element['index']
        # PasswordSetFlag = True
    elif (element['name'].find(LOCAL_HOSTNAME) >= 0) and (element['name'] == 'ZJLPC'):
        # IS_FORMAL_DEPLOYMENT = False
        LOCAL_DB_PASSWORD = '123456'
        LOCAL_WK_TARGET = element['index']
        # PasswordSetFlag = True
    elif (element['name'].find(LOCAL_HOSTNAME) >= 0) and (element['name'] == 'PGS-20180113DJZ'):
        # IS_FORMAL_DEPLOYMENT = False
        LOCAL_DB_PASSWORD = '123456'
        LOCAL_WK_TARGET = element['index']
        # PasswordSetFlag = True
    elif (element['name'].find(LOCAL_HOSTNAME) >= 0) and (element['name'] == 'PGS-20180113SZM'):
        # IS_FORMAL_DEPLOYMENT = False
        LOCAL_DB_PASSWORD = '123456'
        LOCAL_WK_TARGET = element['index']
        # PasswordSetFlag = True
    elif (element['name'].find(LOCAL_HOSTNAME) >= 0) and (element['name'] == 'fsg0518'):
        # IS_FORMAL_DEPLOYMENT = False
        LOCAL_DB_PASSWORD = 'xiaohui@bxxh'
        LOCAL_WK_TARGET = element['index']
        # PasswordSetFlag = True
    elif (element['name'].find(LOCAL_HOSTNAME) >= 0) and (element['name'] == 'kickseed'):
        #         IS_FORMAL_DEPLOYMENT = False
        LOCAL_DB_PASSWORD = '123456'
        LOCAL_WK_TARGET = element['index']
    else:
        LOCAL_DB_PASSWORD = 'bxxhbxxh'
        LOCAL_WK_TARGET = -1
#         PasswordSetFlag = True
#     else:
#         # IS_FORMAL_DEPLOYMENT = False
#         LOCAL_DB_PASSWORD = '123456'
#         LOCAL_WK_TARGET = element['index']
# <<<<<<< HEAD
#         # PasswordSetFlag = True
# # if (PasswordSetFlag == False):
# #     IS_FORMAL_DEPLOYMENT = True
# #     LOCAL_DB_PASSWORD = 'bxxhbxxh'
# #     LOCAL_WK_TARGET = 1
# =======
#         PasswordSetFlag = True
#
# # if (PasswordSetFlag == False):
# #     IS_FORMAL_DEPLOYMENT = True
# #     LOCAL_DB_PASSWORD = 'bxxhbxxh';
# #     LOCAL_WK_TARGET = 1
# >>>>>>> 2f1bc20919f4c60c266fe59923f97f9279ddbf0d

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DappDbCebs',
    'DappDbF1sym',
    'DappDbF2cm',
    'DappDbF3dm',
    'DappDbF4icm',
    'DappDbF5fm',
    'DappDbF6pm',
    'DappDbF7ads',
    'DappDbF8psm',
    'DappDbF9gism',
    'DappDbF10oam',
    'DappDbF11faam',
    'DappDbFxprcm',
    'DappDbSnr',
    'DappDbF12iwdp',
    'DappDbF13phos',
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

ROOT_URLCONF = 'DjoSiteDba.urls'

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

WSGI_APPLICATION = 'DjoSiteDba.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
# Comments Options setting will remove running WARNING.

# SERVER
print("LOCAL_WK_TARGET:" + str(LOCAL_WK_TARGET))
if (LOCAL_WK_TARGET == 1):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'NAME': 'Django',
            'USER': 'mfunhcu',
            'PASSWORD': LOCAL_DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': {
                "init_command": "SET default_storage_engine='INNODB'"
            },
            'CONN_MAX_AGE': None,
        },
        "IWDP": {
            'ENGINE': 'django.db.backends.mysql',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'NAME': 'iwdp',
            'USER': 'mfunhcu',
            'PASSWORD': LOCAL_DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': {
                "init_command": "SET default_storage_engine='INNODB'"
            },
            'CONN_MAX_AGE': None,
        },
        'CEBS': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'cebs',
            'USER': 'mfunhcu',
            'PASSWORD': LOCAL_DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': {
                'autocommit': True,
                #                 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
            'CONN_MAX_AGE': None,
        }
    }
    DATABASE_ROUTERS = ['DjoSiteDba.db_route.DatabaseAppsRouter']
    DATABASE_APPS_MAPPING = {
        'admin': 'default',
        'auth': 'default',
        'contenttypes': 'default',
        'sessions': 'default',
        'messages': 'default',
        'staticfiles': 'default',
        'DappDbF1sym': 'default',
        'DappDbF2cm': 'default',
        'DappDbF3dm': 'default',
        'DappDbF4icm': 'default',
        'DappDbF5fm': 'default',
        'DappDbF6pm': 'default',
        'DappDbF7ads': 'default',
        'DappDbF8psm': 'default',
        'DappDbF9gism': 'default',
        'DappDbF10oam': 'default',
        'DappDbF11faam': 'default',
        'DappDbFxprcm': 'default',
        'DappDbSnr': 'default',
        'DappDbCebs': 'CEBS',
        'DappDbF12iwdp': 'IWDP',
        'DappDbF13phos': 'IWDP'
    }

# ZJL PC
elif (LOCAL_WK_TARGET == 2):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'hstdb',
            'USER': 'root',
            'PASSWORD': LOCAL_DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            #             'OPTIONS': {
            #                 'autocommit': True,
            #                 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            #             },
            'CONN_MAX_AGE': None,
        }
    }

# XDPC
elif (LOCAL_WK_TARGET == 3):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'NAME': 'djztest6',
            'USER': 'root',
            'PASSWORD': LOCAL_DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            #             'OPTIONS': {
            #                 'autocommit': True,
            #                 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            #             },
            'OPTIONS': {
                "init_command": "SET default_storage_engine='INNODB'"
            },
            'CONN_MAX_AGE': None,
        },
        "IWDP": {
            'ENGINE': 'django.db.backends.mysql',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'NAME': 'iwdp',
            'USER': 'root',
            'PASSWORD': LOCAL_DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': {
                "init_command": "SET default_storage_engine='INNODB'"
            },
            'CONN_MAX_AGE': None,
        },
        'CEBS': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'cebs',
            'USER': 'root',
            'PASSWORD': LOCAL_DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': {
                'autocommit': True,
                #                 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
            'CONN_MAX_AGE': None,
        }
    }
    DATABASE_ROUTERS = ['DjoSiteDba.db_route.DatabaseAppsRouter']
    DATABASE_APPS_MAPPING = {
        'admin': 'default',
        'auth': 'default',
        'contenttypes': 'default',
        'sessions': 'default',
        'messages': 'default',
        'staticfiles': 'default',
        'DappDbF1sym': 'default',
        'DappDbF2cm': 'default',
        'DappDbF3dm': 'default',
        'DappDbF4icm': 'default',
        'DappDbF5fm': 'default',
        'DappDbF6pm': 'default',
        'DappDbF7ads': 'default',
        'DappDbF8psm': 'default',
        'DappDbF9gism': 'default',
        'DappDbF10oam': 'default',
        'DappDbF11faam': 'default',
        'DappDbFxprcm': 'default',
        'DappDbSnr': 'default',
        'DappDbCebs': 'CEBS',
        'DappDbF12iwdp': 'IWDP',
        'DappDbF13phos': 'IWDP'
    }
# LCPC
elif (LOCAL_WK_TARGET == 4):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'cebs',
            'USER': 'root',
            'PASSWORD': LOCAL_DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': {
                'autocommit': True,
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
            'CONN_MAX_AGE': None,
        },
        'cebs': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'cebs',
            'USER': 'root',
            'PASSWORD': LOCAL_DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': {
                'autocommit': True,
                #                 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
            'CONN_MAX_AGE': None,
        }
    }
    DATABASE_ROUTERS = ['DjoSiteDba.db_route.DatabaseAppsRouter']
    DATABASE_APPS_MAPPING = {
        'admin': 'default',
        'auth': 'default',
        'contenttypes': 'default',
        'sessions': 'default',
        'messages': 'default',
        'staticfiles': 'default',
        'DappDbF1sym': 'default',
        'DappDbF2cm': 'default',
        'DappDbF3dm': 'default',
        'DappDbF4icm': 'default',
        'DappDbF5fm': 'default',
        'DappDbF6pm': 'default',
        'DappDbF7ads': 'default',
        'DappDbF8psm': 'default',
        'DappDbF9gism': 'default',
        'DappDbF10oam': 'default',
        'DappDbF11faam': 'default',
        'DappDbFxprcm': 'default',
        'DappDbSnr': 'default',
        'DappDbCebs': 'cebs',

    }

# Ubuntu 16 From xiaohui

elif (LOCAL_WK_TARGET == 5):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'cebs',
            'USER': 'root',
            'PASSWORD': LOCAL_DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': {
                'autocommit': True,
                # 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
            'CONN_MAX_AGE': None,
        },
        'cebs': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'cebs',
            'USER': 'root',
            'PASSWORD': LOCAL_DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': {
                'autocommit': True,
                #                 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
            'CONN_MAX_AGE': None,
        }
    }
    DATABASE_ROUTERS = ['DjoSiteDba.db_route.DatabaseAppsRouter']
    DATABASE_APPS_MAPPING = {
        'admin': 'default',
        'auth': 'default',
        'contenttypes': 'default',
        'sessions': 'default',
        'messages': 'default',
        'staticfiles': 'default',
        'DappDbF1sym': 'default',
        'DappDbF2cm': 'default',
        'DappDbF3dm': 'default',
        'DappDbF4icm': 'default',
        'DappDbF5fm': 'default',
        'DappDbF6pm': 'default',
        'DappDbF7ads': 'default',
        'DappDbF8psm': 'default',
        'DappDbF9gism': 'default',
        'DappDbF10oam': 'default',
        'DappDbF11faam': 'default',
        'DappDbFxprcm': 'default',
        'DappDbSnr': 'default',
        'DappDbCebs': 'cebs',
    }
# 澶嶇強鏁版嵁搴�
elif (LOCAL_WK_TARGET == 6):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'Django',
            'USER': 'mfunhcu',
            'PASSWORD': LOCAL_DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': {
                'autocommit': True,
                #                 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
            'CONN_MAX_AGE': None,
        },
        "IWDP": {
            'ENGINE': 'django.db.backends.mysql',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'NAME': 'iwdp',
            'USER': 'mfunhcu',
            'PASSWORD': LOCAL_DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': {
                "init_command": "SET default_storage_engine='INNODB'"
            },
            'CONN_MAX_AGE': None,
        },
        'CEBS': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'cebs',
            'USER': 'mfunhcu',
            'PASSWORD': LOCAL_DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': {
                'autocommit': True,
                #                 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
            'CONN_MAX_AGE': None,
        }
    }
    DATABASE_ROUTERS = ['DjoSiteDba.db_route.DatabaseAppsRouter']
    DATABASE_APPS_MAPPING = {
        'admin': 'default',
        'auth': 'default',
        'contenttypes': 'default',
        'sessions': 'default',
        'messages': 'default',
        'staticfiles': 'default',
        'DappDbF1sym': 'default',
        'DappDbF2cm': 'default',
        'DappDbF3dm': 'default',
        'DappDbF4icm': 'default',
        'DappDbF5fm': 'default',
        'DappDbF6pm': 'default',
        'DappDbF7ads': 'default',
        'DappDbF8psm': 'default',
        'DappDbF9gism': 'default',
        'DappDbF10oam': 'default',
        'DappDbF11faam': 'default',
        'DappDbFxprcm': 'default',
        'DappDbSnr': 'default',
        'DappDbF12iwdp': 'IWDP',
        'DappDbF13phos': 'IWDP',
        'DappDbCebs': 'cebs'
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'cebs',
            'USER': 'root',
            'PASSWORD': LOCAL_DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'CONN_MAX_AGE': None,
        }
    }

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators


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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = False

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
