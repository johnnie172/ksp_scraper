import user_input_utilities, consts
from main import dbq
import logging

logger = logging.getLogger(__name__)


def user_login():
    """Login user, getting dbq instance"""
    email = user_input_utilities.input_user_email()
    password = user_input_utilities.input_user_password()
    user = dbq.select_user(email, password)
    logger.debug(f'User with email - {email} is logged in to the system.')
    return user


def user_signup():
    """Signup user, adding to dbq instance and returning user_id"""
    email = user_input_utilities.input_user_email()
    password = user_input_utilities.input_user_password_sign_up()
    user_id = dbq.add_user(email, password)
    if user_id == None:
        print(consts.EMAIL_ALREADY_EXISTS_MESSAGE)
        logger.debug(f'{consts.EMAIL_ALREADY_EXISTS_MESSAGE}, email is: {email}.')
        return None
    logger.debug(f'New user is added, user id is:{user_id}')
    return user_id


def user_log_out():
    pass


def notify_out_of_stock():
    # todo send notificetions
    pass
