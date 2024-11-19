from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')  # Replace 'your_project' with your project's name.
# app.conf.broker_url = 'redis://localhost:6379/0'
# Configure Celery using settings from Django settings.py.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load tasks from all registered Django app configs.
app.autodiscover_tasks()
broker_connection_retry_on_startup = True

# Add these settings
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# celery -A core worker --pool=solo --loglevel=info