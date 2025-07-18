web: bash -c "python manage.py migrate && python manage.py create_admin && gunicorn config.wsgi:application"
worker: python manage.py runbot