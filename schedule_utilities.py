import schedule
import time
import logging

logger = logging.getLogger(__name__)


# def get_delta():
#     time_now = datetime.today()
#     next_day = time_now.replace(day=time_now.day + 1, hour=1, minute=0, second=0, microsecond=0)
#     delta_t = next_day - time_now
#     secs = delta_t.seconds + 1
#     logger.debug(f'Secs are {secs}')
#     return secs
#
#
# def start_timer(secs, function):
#     t = Timer(secs, function)
#     t.start()
#     logger.debug(f'Timer started, will execute {function} every {secs} secs.')

def schedule_timer(minutes, function):
    """Function for setting timer every X minutes for another function."""
    schedule.every(minutes).minutes.do(function)
    logger.debug(f'Job {function} has been started, will run every {minutes} minutes.')
    while True:
        schedule.run_pending()
        time.sleep(1)