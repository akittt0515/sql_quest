import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '%a46pm3zq@dj9)h(hloxhsm0eo7%-dp)tids3w(mdc*7814x5q'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    
}}

DEBUG = True