FROM python:2.7
WORKDIR /usr/src/app/
ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY ./test_celery/* /usr/src/app/test_celery/
ENTRYPOINT celery -A /usr/src/app/test_celery worker --concurrency=20 --loglevel=info
