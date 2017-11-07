from __future__ import absolute_import
from test_celery.tasks import longtime_add


if __name__ == '__main__':
    urls = [
        'http://ya.ru/',
    ]

    for url in urls:
        result = longtime_add.delay(url)
        print('task result: ', result.result)
