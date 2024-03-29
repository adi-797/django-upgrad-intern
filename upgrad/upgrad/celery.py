from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

from django.conf import settings

upgrad_celery = Celery('proj')


upgrad_celery.config_from_object('django.conf:settings')
upgrad_celery.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@upgrad_celery.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))