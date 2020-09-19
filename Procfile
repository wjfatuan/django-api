release: python app/manage.py migrate
web: gunicorn simpleapi.wsgi --log-file - --chdir app/ 