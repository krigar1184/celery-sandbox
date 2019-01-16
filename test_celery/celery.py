from __future__ import absolute_import
import os
from celery import Celery


username = os.environ.get('RABBITMQ_USERNAME', 'rabbit')
passwd = os.environ.get('RABBITMQ_PASSWD', 'rabbit')
host = os.environ.get('RABBITMQ_HOST', 'rabbit')
port = os.environ.get('RABBITMQ_PORT', '5672')

broker = os.environ.get('CELERY_BROKER', 'amqp://{username}:{passwd}@{host}:{port}')
backend = os.environ.get('CELERY_BACKEND', 'rpc://')
include = ['test_celery.tasks']

app = Celery(
    __name__,
    broker=broker.format(username=username, passwd=passwd, host=host, port=port),
    backend=backend,
    include=include,
)
