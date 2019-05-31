from projexbackend.config.common import *
import os

############################ PRODUCTION SETTINGS ##################################

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
DEBUG = False
ALLOWED_HOSTS = ['projexbackend.herokuapp.com']
#### Database configuration #####

import dj_database_url 
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
DEBUG = True
