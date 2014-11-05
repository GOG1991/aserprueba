import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ms6kf5i*(vnzcbrc*r^5i6a=-ogr5anq&$1-j7o16gr+o#if9('

DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

DJANGO_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

)

THIRD_PARTY_APPS = (  
    'south',
    'jquery',
    'djangoformsetjs',

)

LOCAL_APPS = (
    'clientes',
    'equipos',
    'historiales',
    'perfiles',
    'servicios',
    'estados',
    'home',

)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'aser.urls'

WSGI_APPLICATION = 'aser.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aserdb080814',
        'USER':'aser_adminbd20',
        'PASSWORD':'JUvX8O08',
        'HOST': 'localhost',
    }
}

LANGUAGE_CODE = 'es-Mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True
#archivos estaticos
#defimos la url de los archivos staticos
STATIC_URL = '/static/'
#Definimos la ruta de los archivos staticos
STATIC_ROOT = '/home/aser/app/static/'

MEDIA_ROOT = '/home/aser/app/media/'
MEDIA_URL = '/media/'

# para habilitar el sidebar del admin suit
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    #'perfiles.contextprocessors.serperfil',
    'django.core.context_processors.request',
)

#Personalizar suit
SUIT_CONFIG = {
    'ADMIN_NAME': 'ASER',
    'SHOW_REQUIRED_ASTERISK': True,
    'MENU': (
        # Reorder app models
        {'app': 'auth', 'label': 'Usuarios' ,'models': ('user', 'group'),'icon':'icon-user'},
        {'label': 'Aser', 'url': '/home', 'icon':'icon-home'},
        # Separator
        '-',
        {'app': 'servicios', 'icon':'icon-print'},
        {'app': 'clientes', 'icon':'icon-book'},
        {'app': 'equipos', 'icon':'icon-hdd'},
        {'app': 'estados', 'icon':'icon-barcode'},
        {'app': 'historiales', 'label': 'Fallas y soluciones', 'icon':'icon-barcode'},

    )
}

# definimos el modulo para crear los perfiles de los usuarios
AUTH_PROFILE_MODULE = 'perfiles.perfiles'
