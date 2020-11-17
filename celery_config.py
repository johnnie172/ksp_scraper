from datetime import timedelta
from tasks import app

CELERY_IMPORTS = ('tasks')
CELERY_IGNORE_RESULT = False
BROKER_HOST = '127.0.0.1'
BROKER_PORT = 5672
BROKER_URL = 'amqp://'

app.conf.beat_schedule = {
    'update-prices-every-15-minutes': {
        'task': 'tasks.update_all_prices',
        'schedule': timedelta(minutes=15),
    },
}
