web: bash -c "python manage.py makemigrations && python manage.py migrate && gunicorn config.wsgi:application"
worker: python manage.py runbot