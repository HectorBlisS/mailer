web: gunicorn mailer.wsgi 
worker: celery worker  --app=mailer.app
worker: celery flower --app=mailer.app --port=5555