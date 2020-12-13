from datetime import timedelta
from tasks import app


imports = 'tasks'
broker_url = 'amqp://guest:guest@localhost:5672/ksp'
celery_ignore_result = False

app.conf.beat_schedule = {
    'main-task-every-60-minutes': {
        'task': 'tasks.celery_main_task',
        'schedule': timedelta(minutes=60),
    },
}
