import user_input_utilities
from main import dbq
import logging


logger = logging.getLogger(__name__)


def user_login():
    """Login user, getting dbq instance"""
    email = user_input_utilities.input_user_email()
    password = user_input_utilities.input_user_password()
    user = dbq.select_user(email, password)
    return user

def user_signup():
    pass


def user_log_out():
    pass