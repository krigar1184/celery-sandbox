FROM python:3.6
ADD requirements.txt /usr/src/app/requirements.txt
ADD ./test_celery/ /usr/src/app/
WORKDIR /usr/src/app/
RUN pip install -r requirements.txt
ENTRYPOINT /bin/bash
# ENTRYPOINT celery -A test_celery worker --concurrency=20 --loglevel=info
