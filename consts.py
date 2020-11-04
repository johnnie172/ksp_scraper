import os

DATABASE_NAME = os.environ.get('DATABASE_NAME')
DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_PORT = os.environ.get('DATABASE_PORT')
DATABASE_TABLES_SETUP_FILE = 'create_tabels.sql'

LINK_ERROR_MESSAGE = 'Sorry we cannot use this link, Please try again.'
TARGET_PRICE_ERROR_MESSAGE = 'Sorry the target price is not valid, please make sure you entered numbers only(not decimal).'
