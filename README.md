# Projex Application Programming Interface (API)

[![Build Status](https://travis-ci.com/solazverULAB2018/api-projex.svg?branch=master)](https://travis-ci.com/solazverULAB2018/api-projex)


Application Programming Interface built under Django Rest Framework. It's used in ProjeX app. Tested and deployed using 
[Travis CI framework](https://travis-ci.com/)

## Initial Requirements

- [Python](https://www.python.org/downloads/)
- [Django](https://docs.djangoproject.com/es/2.2/intro/install/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Pip](https://pip.pypa.io/en/stable/installing/)

## Quickstart 

### Run in development environment

1. Open `settings.py` file.
2. Export `DJANGO_DB_NAME`, `DJANGO_USERNAME` and `DJANGO_PASSWORD` with your corresponding
   PostgreSQL Database configuration.
3. Go to `api-projex` folder.
4. Activate virtual environment using `source virt-env/bin/activate`.
5. Install all required packages using `pip install -r requirements.txt`.
6. Run migrations using `python manage.py migrate`.
7. Start app using `python manage.py runserver`.