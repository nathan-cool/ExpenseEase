release: python mysite/manage.py migrate
web: gunicorn mysite.mysite.wsgi:application --log-file=-