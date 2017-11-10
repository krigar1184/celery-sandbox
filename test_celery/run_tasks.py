from __future__ import absolute_import
import test_celery.tasks as t


if __name__ == '__main__':
    t.parent_task.delay()
