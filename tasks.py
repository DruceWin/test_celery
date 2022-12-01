import time
import redis

from celery import Celery

app = Celery('tasks', broker='redis://localhost')

r = redis.Redis()

@app.task
def add(x, y):
    time.sleep(6)
    r.set('value', x+y)
    return x + y
