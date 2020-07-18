import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9u1))8ol#(lg^cyoxbw4-+50uue^a+p%vdsfv%$^#$^&gbg6346sddfbg^$%dsn+_t#9y)yjl4!%r)bv'
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obtm;vdanfn3kt43256Q#$#Re*#@$*@(%(_@#+t+_+_+#)r%+$#@)^_%@#$%)$#2_+&k3q+pmu)5%asj6yjpkag')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [

    # Default apps

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My apps
    'community',
    'learn',
    'registration',
    
    # Third Party Libraries
    'crispy_forms',
    
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'


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

ROOT_URLCONF = 'WitQuake.urls'

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

WSGI_APPLICATION = 'WitQuake.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.witquakedb'),
    }
}


# Password validation

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


# INTERNATIONALIZATION

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ACCOUNT SETTING

QUOTES_PER_PAGE = 2

ACCOUNT_ACTIVATION_DAYS = 3

# EMAIL_HOST = 'mail.domain.com'
# EMAIL_HOST_USER = 'abc@domain.com'
# EMAIL_HOST_PASSWORD = 'abcdef'
# DEFAULT_FROM_EMAIL = 'abc@domain.com'
# SERVER_EMAIL = 'abc@domain.com'
# EMAIL_PORT = 25
# EMAIL_USE_TLS = False

EMAIL_HOST = 'mail.witquake.co.in'
EMAIL_HOST_USER = 'services@witquake.co.in'
EMAIL_HOST_PASSWORD = 'witquake@123'
DEFAULT_FROM_EMAIL = 'services@witquake.co.in'
SERVER_EMAIL = 'services@witquake.co.in'
EMAIL_PORT = 25
EMAIL_USE_TLS = False

# STATIC FILES (CSS, JavaScript, Images)

LOGIN_REDIRECT_URL = "/forum/question"

STATIC_ROOT = os.path.join(BASE_DIR + '/staticfiles')

STATIC_URL = '/static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_ROOT = os.path.join(BASE_DIR + '/static/images')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

