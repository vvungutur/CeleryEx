# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime
import time

@shared_task
def async_write(pings):
	with open ('log.txt', 'w') as logFile:
		for ping in range(pings):
			time.sleep(1)
			now = datetime.now()
			logFile.write(str(now) + '\n')


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
