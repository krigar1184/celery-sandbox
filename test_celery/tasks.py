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


class BaseSubtask(celery.Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('Exception info: ', einfo)
        print('{0!r} failed: {1!r}'.format(task_id, exc))


@app.task(bind=True)
def parent_task(self):
    print('Starting parent task...')
    chord = celery.chord([subtask1.si()], body=callback_task.si())
    chord.on_error(errback_task.s()).delay()
    print('Finished parent task')


@app.task(bind=True)
def subtask1(self):
    print('Starting subtask1...')

    try:
        raise CallbackException()
    except Exception as e:
        print('Subtask1 caught exception')
        try:
            raise self.retry(exc=e, countdown=5)
        except type(e):
            return False

    return True

@app.task(bind=True)
def callback_task(self, *args, **kwargs):
    print('Starting callback...')


@app.task(bind=True)
def errback_task(request, exc, traceback):
    print('This is an errback')
