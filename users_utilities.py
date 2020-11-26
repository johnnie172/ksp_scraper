import user_input_utilities, consts
from main import dbq
import logging
import bcrypt

logger = logging.getLogger(__name__)


def user_login():
    """Login user, returning the id and email after verifying password"""
    email = user_input_utilities.input_user_email()
    user = dbq.select_user(email)
    id = user[0]
    email = user[1]
    password = user[2]
    if check_password(password):
        logger.debug(f'User with email:{email} is logged in!')
        return (id, email)


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


def hash_password(password):
    """Bycrypt password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    logger.debug('Hashing password.')
    return hashed_password.decode('utf-8')


def check_password(hashed_password):
    """Checking bycrypt password"""
    if bcrypt.checkpw(user_input_utilities.input_user_password().encode('utf8'), hashed_password.encode('utf8')):
        logger.debug('Password matches!')
        return True
    logger.debug('Password not matches!')
    print('Wrong password!')
    return False


def user_log_out():
    pass


def notify_out_of_stock():
    # todo send notificetions
    pass
