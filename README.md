# Projex Application Programming Interface (API)

[![Build Status](https://travis-ci.org/solazverULAB2018/api-projex.png?branch=master)](https://travis-ci.org/solazverULAB2018/api-projex)


Application Programming Interface built under Django Rest Framework. It's used in ProjeX app.

## Initial Requirements

- [Python](https://www.python.org/downloads/)
- [Django](https://docs.djangoproject.com/es/2.2/intro/install/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Pip](https://pip.pypa.io/en/stable/installing/)

## Quickstart 

### Run in development environment

1. Open `settings.py` file.
2. Change the following lines:

``` python
# settings.py
# Change this

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'api-projex',
	'USER': 'julio',
	'PASSWORD': '12345678',
	'HOST': 'localhost',
	'PORT': '',
    }
}

# to this

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'YOUR_POSTGRESQL_DATABASE',
	'USER': 'YOUR_POSTGRESQL_USERNAME',
	'PASSWORD': 'YOUR_POSTGRESQL_PASSWORD',
	'HOST': 'localhost',
	'PORT': '',
    }
}


```
3. Go to `api-projex` folder.
4. Activate virtual environment using `source virt-env/bin/activate`.
5. Install all required packages using `pip install -r requirements.txt`.
6. Run migrations using `python manage.py migrate`.
7. Start app using `python manage.py runserver`.