import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')2wv-%h3_0a=#k5u+-gy@e$)a*w##bn1nw(hut1lcqbe@gt#6w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_comments_xtd',
    'django_comments',

    'madde.apps.MaddeConfig',
    'hesaplar.apps.HesaplarConfig',
    'corsheaders',

    'crispy_forms',
    'ckeditor',
    'social_django',
    'django_social_share',


]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'kelepirbul.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'hesaplar.authentication.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

WSGI_APPLICATION = 'kelepirbul.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'tr-TR'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Comments app
COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_CONFIRM_EMAIL = False
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#  To help obfuscating comments before they are sent for confirmation.
COMMENTS_XTD_SALT = (b"Timendi causa est nescire. "
                     b"Aequam memento rebus in arduis servare mentem.")
# Source mail address used for notifications.
COMMENTS_XTD_FROM_EMAIL = "noreply@example.com"
# Contact mail address to show in messages.
COMMENTS_XTD_CONTACT_EMAIL = "helpdesk@example.com"
COMMENTS_XTD_MAX_THREAD_LEVEL = 1
COMMENTS_XTD_APP_MODEL_OPTIONS = {
    'default': {
        'allow_flagging': True,
        'allow_feedback': True,
        'show_feedback': True,
        'who_can_post': 'users'  # Valid values: 'all', users'
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
CRISPY_TEMPLATE_PACK = 'bootstrap4'
STATIC_URL = '/static/'
MEDIA_URL = '/images/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')
# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '691575177250-vik22urqe0vsm0c6t17q9sbvtj1ofi8e.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'hrGqsR4oKC0ejaq_6ESC-aMB'
# CKEDITOR WYSIWYG editor
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
X_FRAME_OPTIONS = 'SAMEORIGIN'

SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/settings/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

'''CORS_ALLOWED_ORIGIN_REGEXES = [
    path('', views.index, name='index'),
    path('madde/<int:pk>', views.madde_detay, name='madde_detay'),
    path('vote/', views.product_vote, name='vote' ),
]'''
'''CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:9000"
]'''
CORS_ALLOW_ALL_ORIGINS = True
