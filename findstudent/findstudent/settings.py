import os

from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "4d!2@*cmd5)xz$s#jt9xt8dcox2om!78a^=+wy!dyyf)9b!lkj"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'testserver',
    'localhost',
    '127.0.0.1',
    '78.155.218.220',
    'findstudent.ru',
]


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'account',
    'bootstrap4',
    'storages',
    'imagekit',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'profiles.apps.ProfilesConfig',
    'data.apps.DataConfig',
    'pages.apps.PagesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'findstudent.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'account.context_processors.account',
            ],
        },
    },
]

WSGI_APPLICATION = 'findstudent.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database1',
        'USER': 'database1_role',
        'PASSWORD': 'database1_password',
        'HOST': 'database1',
        'PORT': '5432',
    },
    'database2': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database2',
        'USER': 'database2_role',
        'PASSWORD': 'database2_password',
        'HOST': 'database2',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Russian')),
    ('de', _('German')),
    ('fr', _('French')),
    ('uk', _('Ukrainian')),
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'static')
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "mystatic"),
]

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_REGION_NAME = 'eu-west-1'
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_URL = 's3.eu-west-1.amazonaws.com'
AWS_ACCESS_KEY_ID = 'AKIAIX2XWGFFSJ46EDDA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'findstudentstaging'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

VK_URL = 'https://api.vk.com/method'
VK_LANG = 'ru'
VK_VERSION = '5.92'
VK_TOKEN = '183c229a183c229a183c229a43185515081183c183c229a44ba90cab7dfd302261cc6de'

AUTH_USER_MODEL = 'profiles.Profile'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)

SITE_ID = 3

DEFAULT_FROM_EMAIL = 'Igorzz2011@yandex.ru'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'Igorzz2011@yandex.ru'
EMAIL_HOST_PASSWORD = '117405'
EMAIL_USE_SSL = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
