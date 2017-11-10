from __future__ import absolute_import
import celery
import os
from .celery import app
from pymongo import MongoClient


mongo_host = os.environ.get('MONGO_HOST', 'database')
mongo_port = os.environ.get('MONGO_PORT', 27017)
client = MongoClient(mongo_host, mongo_port)
db = client.mongodb_test
collection = db.celery_test
post = db.test


class CallbackException(Exception):
    pass


@app.task(bind=True)
def parent_task(self):
    print('Starting parent task...')
    subtask_signature = subtask.si()
    callback_signature = callback_task.si()
    chord = celery.chord([subtask_signature], body=callback_signature)
    chord.delay()
    print('Finished parent task')


@app.task(bind=True)
def subtask(self):
    print('Starting subtask...')


@app.task(bind=True)
def callback_task(self):
    print('Starting callback...')
    try:
        raise CallbackException()
    except CallbackException as e:
        self.request.update({'exception_type': type(e)})
        raise CallbackException()
