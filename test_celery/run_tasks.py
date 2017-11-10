from __future__ import absolute_import
from .tasks import longtime_add, test_task


if __name__ == '__main__':
    urls = [
        'http://ya.ru/',
    ]

    for url in urls:
        result = longtime_add.delay(url)
        print('task result: ', result.result)
