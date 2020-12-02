import user_input_utilities, consts, email_utilities
from main import dbq
import logging
import hashlib
import binascii
import os

logger = logging.getLogger(__name__)


def user_login():
    """Login user, returning the id and email after verifying password"""
    email = user_input_utilities.input_user_email()
    user = dbq.select_user(email)
    id = user[0]
    email = user[1]
    password = user[2]
    if verify_password(password):
        logger.debug(f'User with email:{email} is logged in!')
        return (id, email)
    else:
        logger.debug('Password not matches!')
        print('Wrong password!')
        return False


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


def notify_out_of_stock(users_id_records, item_id):
    """Notify for users that item is out of stock."""
    item_title = dbq.select_row(f'SELECT title FROM items WHERE id = {item_id}')[0]
    email_records = dbq.select_emails_to_notify(tuple(users_id_records))
    for user in email_records:
        user_email = user[0]
        email_utilities.send_out_of_stock_mail(user_email, item_title)

def notify_target_price(users_id_records):
    """Notify for users that item is at the target price."""
    logger.debug(f'users_id_records are:{users_id_records}')
    current_item_id = None
    count = 0
    for user in users_id_records:
        count += 1
        logger.debug(f'usersis:{user}')
        current_users_ids = []
        user_id = user[0]
        item_id = user[1]
        if current_item_id is None:
            current_item_id = item_id

        if current_item_id == item_id:
            current_users_ids.append(user_id)
            logger.debug(f'current_item_id is: {current_item_id}')
            logger.debug(f'current_users_ids is: {current_users_ids}')
        else:
            item_uin = dbq.select_row(f'SELECT uin FROM items WHERE id = {item_id}')[0]
            email_records = dbq.select_emails_to_notify(tuple(current_users_ids))
            for user_to_notify in email_records:
                logger.debug(f'user is:{user_to_notify}')
                user_email = user_to_notify[0]
                logger.debug(f'email is: {user_email}')
                logger.debug(f'uin is: {item_uin}')
                email_utilities.send_target_price_mail(user_email, item_uin)
            current_users_ids = []
        if len(users_id_records) == count:
            item_uin = dbq.select_row(f'SELECT uin FROM items WHERE id = {item_id}')[0]
            email_records = dbq.select_emails_to_notify(tuple(current_users_ids))
            for user_to_notify in email_records:
                logger.debug(f'user is:{user_to_notify}')
                user_email = user_to_notify[0]
                logger.debug(f'email is: {user_email}')
                logger.debug(f'uin is: {item_uin}')
                email_utilities.send_target_price_mail(user_email, item_uin)
            current_users_ids = []

    #todo: it sent only to user id 23 and not to user id 22


    pass


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    logger.debug('Hashing password.')
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  user_input_utilities.input_user_password().encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    logger.debug('Verifying password.')
    return pwdhash == stored_password

# def hash_password(password):
#     """Hashing password"""
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
#     logger.debug('Hashing password.')
#     return hashed_password.decode('utf-8')


# def check_password(hashed_password):
#     """Checking hashed password"""
#     if bcrypt.checkpw(user_input_utilities.input_user_password().encode('utf8'), hashed_password.encode('utf8')):
#         logger.debug('Password matches!')
#         return True
#     logger.debug('Password not matches!')
#     print('Wrong password!')
#     return False
