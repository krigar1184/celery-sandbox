from __future__ import absolute_import
import os
from celery import Celery


username = os.environ.get('RABBIT_USERNAME', 'rabbit')
passwd = os.environ.get('RABBIT_PASSWD', 'rabbit')
host = os.environ.get('RABBIT_HOST', 'localhost')

broker = os.environ.get('CELERY_BROKER', 'amqp://{username}:{passwd}@{host}')
backend = os.environ.get('CELERY_BACKEND', 'rpc://')
include = ['test_celery.tasks']

app = Celery(
    __name__,
    broker=broker.format(username=username, passwd=passwd, host=host),
    backend=backend,
    include=include
)
