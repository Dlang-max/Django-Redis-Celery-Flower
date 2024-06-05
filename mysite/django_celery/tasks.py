from celery import shared_task
import time

@shared_task
def celery_worker_test():
    time.sleep(10)
    return True