# Projex Application Programming Interface (API)

[![Build Status](https://travis-ci.com/solazverULAB2018/api-projex.svg?branch=master)](https://travis-ci.com/solazverULAB2018/api-projex)
[![Coverage Status](https://coveralls.io/repos/github/solazverULAB2018/api-projex/badge.svg?branch=master)](https://coveralls.io/github/solazverULAB2018/api-projex?branch=master)


Application Programming Interface built under Django Rest Framework. It's used in ProjeX app. Tested and deployed using 
[Travis CI framework](https://travis-ci.com/)

## Initial Requirements

- [Python](https://www.python.org/downloads/)
- [Django](https://docs.djangoproject.com/es/2.2/intro/install/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Pip](https://pip.pypa.io/en/stable/installing/)

## Quickstart 

### Run in development environment

1. Open `set-env` file and modify it as follows:

    ``` shell
        # Change this

        source virt-env/bin/activate
        export DJANGO_DB_NAME="api-projex"
        export DJANGO_USERNAME="julio"
        export DJANGO_PASSWORD="12345678"

        # ..to this

        source virt-env/bin/activate
        export DJANGO_DB_NAME="YOUR DATABASE NAME"
        export DJANGO_USERNAME="YOUR DATABASE USERNAME"
        export DJANGO_PASSWORD="YOUR DATABASE PASSWORD"

    ```
2. Activate virtual environment and export environment variables using `source set-env`.
3. Install all required packages using `pip install -r requirements.txt`.
4. Run migrations using `python manage.py migrate`.
5. Start app using `python manage.py runserver`.