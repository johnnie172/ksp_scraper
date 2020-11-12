import schedule
import time
import logging

logger = logging.getLogger(__name__)


def schedule_timer(minutes, function):
    """Function for setting timer every X minutes for another function."""
    schedule.every(minutes).minutes.do(function)
    logger.debug(f'Job {function} has been started, will run every {minutes} minutes.')
    while True:
        schedule.run_pending()
        time.sleep(1)