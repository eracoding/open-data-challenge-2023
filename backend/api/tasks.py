from celery import shared_task


@shared_task
def checkTask():
    print("Adsad")
