# Projex Application Programming Interface (API)

[![Build Status](https://travis-ci.com/solazverULAB2018/api-projex.svg?branch=master)](https://travis-ci.com/solazverULAB2018/api-projex)
[![Coverage Status](https://coveralls.io/repos/github/solazverULAB2018/api-projex/badge.svg)](https://coveralls.io/github/solazverULAB2018/api-projex)


Application Programming Interface built under Django Rest Framework. It's used in ProjeX app. Tested and deployed using 
[Travis CI framework](https://travis-ci.com/)

## Initial Requirements

- [Python](https://www.python.org/downloads/)
- [Django](https://docs.djangoproject.com/es/2.2/intro/install/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Pip](https://pip.pypa.io/en/stable/installing/)

## Quickstart 

### Run in development environment

1. Open `set-env.sh` file and modify it as follows:

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
2. Set permissions to `set-env.sh` with `sudo chmod +777 set-env.sh`. In case you don't
   have sudo, then just execute each script line manually in your terminal.
3. Activate virtual environment and export environment variables using `source set-env.sh`.
4. Install all required packages using `make freeze`.
5. Run migrations using `python manage.py migrate`.
6. Start app using `python manage.py runserver`.

### Run alongside ProjeX app in development mode

1. Open this url in your browser when your server is running `127.0.0.1/api/v1/rest-auth/registration`.
2. Create a user with the following credentials: `username: admin`, `email: admin@admin.com` and `password: admin12345`.
3. Comment  ` 'rest_framework.authentication.SessionAuthentication', ` line from `settings.py`.
4. Login from your running app.
