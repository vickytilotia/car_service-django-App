django-admin startproject carservice   #created a new django project
python manage.py startapp service      # created a new app   

now go to settings.py and add the app to insatalled app.
don't forget to add comma at the end


what each files do?

apps.py - configuration and initialization
models.py - data layer
views.py  - control layer
admin.py  - administration interface
urls.py   - url routing
migrations - hold migrations
tests.py  - tests the app


url patterns ----> views(models ---->views)  ------>templates

migrations vs models:-
define the structure of database
migrations generate the script to change the database

when is migrations needed?
adding a new table
adding/remooving/changing field

commands for migrations:
python manage.py makemigrations       # generate migrations
python manage.py migrate              # apply the generated migrations
python manage.py showmigrations       # list project migrations and their status


To create a super user

python manage.py createsuperuser
username vickytilotia
password 123456


This is project is not functional by now!!!