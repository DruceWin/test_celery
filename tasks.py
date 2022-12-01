import time
import redis

from celery import Celery

app = Celery('tasks', broker='redis://localhost')

r = redis.Redis()


@app.task(trail=True)
def add(x, y):
    time.sleep(1)
    r.set('value', x+y)
    return x + y
