from __future__ import absolute_import
import os
from .celery import app
import time
import requests
from pymongo import MongoClient


mongo_host = os.environ.get('MONGO_HOST', 'database')
mongo_port = os.environ.get('MONGO_PORT', 27017)
client = MongoClient(mongo_host, mongo_port)
db = client.mongodb_test
collection = db.celery_test
post = db.test


@app.task(bind=True, default_retry_delay=10)
def longtime_add(self, i):
    print('long time task begins')

    try:
        r = requests.get(i)
        post.insert({'status': r.status_code, 'create_time': time.time()})
        print('long time task finished')
    except Exception as e:
        raise self.retry(exc=e)

    return r.status_code


@app.task()
def test_task(x, y):
    print('pewpew')
    post.insert({'result': x * y})
