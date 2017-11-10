FROM python:3.6
ADD requirements.txt /usr/src/app/requirements.txt
ADD ./test_celery/ /usr/src/app/test_celery
WORKDIR /usr/src/app/
RUN pip install -r requirements.txt
ENV C_FORCE_ROOT 1
ENTRYPOINT celery -A test_celery worker --concurrency=20 --loglevel=info
