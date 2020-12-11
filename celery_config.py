from datetime import timedelta
from tasks import app
import db_config
import os

# env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), '.env')

imports = 'tasks'
broker_url = 'amqp://guest:guest@localhost:5672/ksp'
celery_ignore_result = False

# CELERY_IMPORTS = ('tasks')
# CELERY_IGNORE_RESULT = False
# BROKER_HOST = '127.0.0.1'
# BROKER_PORT = 5672
# BROKER_URL = 'amqp://'


app.conf.beat_schedule = {
    'update-prices-every-1-minutes': {
        'task': 'tasks.update_all_prices',
        'schedule': timedelta(minutes=1),
    },
}
