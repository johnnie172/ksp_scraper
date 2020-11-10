import os

DATABASE_NAME = os.environ.get('DATABASE_NAME')
DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_PORT = os.environ.get('DATABASE_PORT')
DATABASE_TABLES_SETUP_FILE = 'create_tabels.sql'

URL_TO_ADD_UIN = 'https://ksp.co.il/?uin='

USER_EMAIL_ERROR_MESSAGE = 'You have entered invalid Email address'
LINK_ERROR_MESSAGE = 'Sorry we cannot use this link, Please try again.'
TARGET_PRICE_ERROR_MESSAGE = 'Sorry the target price is not valid, please make sure you entered numbers only(not ' \
                             'decimal). '
UIN_ERROR_MESSAGE = 'Sorry, cannot find uin.'
