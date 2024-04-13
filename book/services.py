import json
from datetime import datetime, timedelta

from django_celery_beat.models import PeriodicTask, \
     CrontabSchedule

# Создаем интервал для повтора
schedule, created = CrontabSchedule.objects.get_or_create(
    minute='*',
    hour='*',
    day_of_week='0',
    day_of_month='*',
    month_of_year='*',
)

# Создаем задачу для повторения
PeriodicTask.objects.create(
     interval=schedule,
     name='Уведомление о новых книгах в продаже',
     task='book.tasks.send_message_telegram',
     args=json.dumps(['arg1', 'arg2']),
     kwargs=json.dumps(
          {
               'be_careful': True,
          }
     ),
     expires=datetime.utcnow() + timedelta(minutes=3)
)
