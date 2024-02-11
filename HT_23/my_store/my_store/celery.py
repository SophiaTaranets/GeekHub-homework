import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_sears_product.settings')
celery_app = Celery('my_store')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()


@celery_app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
