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
        export SECRET_KEY='&o0ff+%&_th__u0!7uu82h6wsq)ac%bkh&81$+l#@77)01v)fk'


        # ..to this

        source virt-env/bin/activate
        export DJANGO_DB_NAME="YOUR DATABASE NAME"
        export DJANGO_USERNAME="YOUR DATABASE USERNAME"
        export DJANGO_PASSWORD="YOUR DATABASE PASSWORD"
        export SECRET_KEY='&o0ff+%&_th__u0!7uu82h6wsq)ac%bkh&81$+l#@77)01v)fk'


    ```
2. Activate virtual environment and export environment variables using `source set-env.sh`.
3. Install all required packages using `make freeze`.
4. Run migrations using `python manage.py migrate`.
5. Start app using `python manage.py runserver`.