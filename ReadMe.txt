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