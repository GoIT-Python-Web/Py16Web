from celery import Celery

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'

celery = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)


@celery.task(name='Add two numbers')
def add(x, y):
    return x + y


@celery.task(name='Sub two numbers')
def sub(x, y):
    return x - y
