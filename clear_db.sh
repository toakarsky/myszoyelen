#!/usr/bin/bash

rm migrations -rf
rm test.db

python manage.py db init
python manage.py db migrate
python manage.py db upgrade
