#!/usr/bin/env bash

set -e

echo "Deploying master to production"

heroku git:remote --app projexbackend --remote production
git push production
heroku run --remote production python manage.py migrate

