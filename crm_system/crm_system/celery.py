from os import environ
from celery import Celery


environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_system.settings')
app = Celery('crm_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
