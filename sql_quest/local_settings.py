import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'dk7)j=up6be3mtlcs#bkq$b)kuq$=)q4#a$9=x3sc-1tpy)t8f'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    
}}

DEBUG = True