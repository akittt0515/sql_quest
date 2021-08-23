import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '34##5*1t^zsnh_@y7$+c@i_d5ty8$gk4))=1xetejbzkr!+(o('

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    
}}

DEBUG = True