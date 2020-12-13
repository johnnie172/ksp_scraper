import user_input_utilities
import consts
import email_utilities
import logging
import hashlib
import binascii
import os


class UserUtilities:

    def __init__(self, db_queries):
        self.logger = logging.getLogger(__name__)
        self.db_queries = db_queries

    def user_login(self):
        """Login user, returning the id and email after verifying password"""
        email = user_input_utilities.input_user_email()
        user = self.db_queries.select_user(email)
        id = user[0]
        email = user[1]
        password = user[2]

        if self.verify_password(password):
            self.logger.debug(f'User with email:{email} is logged in!')
            return (id, email)
        else:
            self.logger.debug('Password not matches!')
            print('Wrong password!')
            return False

    def user_signup(self):
        """Signup user, adding to db_queries instance and returning user_id"""
        email = user_input_utilities.input_user_email()
        password = user_input_utilities.input_user_password_sign_up()
        user_id = self.db_queries.add_user(email, password)

        if user_id == None:
            print(consts.EMAIL_ALREADY_EXISTS_MESSAGE)
            self.logger.debug(f'{consts.EMAIL_ALREADY_EXISTS_MESSAGE}, email is: {email}.')
            return None

        self.logger.debug(f'New user is added, user id is:{user_id}')
        return user_id

    def user_log_out(self):
        pass

    def notify_out_of_stock(self, users_id_records, item_id):
        """Notify users that item is out of stock."""
        self.logger.debug(f'users id records are:{users_id_records}.')
        self.logger.debug(f'item_id is: {item_id}.')
        item_title = self.db_queries.select_row(f'SELECT title FROM items WHERE id = {item_id}')[0]
        email_records = self.db_queries.select_emails_to_notify(tuple(users_id_records))

        emails_to_send = ""
        for email in email_records:
            emails_to_send += (f', {email[0]}')
        email_utilities.send_out_of_stock_mail(emails_to_send, item_title)

        # todo in dbqueries.check_users_for_out_of_stock_item the same as the target price

    def notify_target_price(self, users_id_records):
        """Notify users that item is at the target price."""
        self.logger.debug(f'users_id_records are:{users_id_records}')

        users_list = []
        current_item_id = users_id_records[0][1]
        items_users_dict = {}

        for user in users_id_records:
            self.logger.debug(f'user is:{user}')
            user_id = user[0]
            item_id = user[1]

            if current_item_id == item_id:
                items_users_dict = {}
                items_users_dict[item_id] = users_list
                users_list.append(user_id)
                self.logger.debug(f'items_users_dict is: {items_users_dict}')
            else:
                users_list = []
                self.logger.debug(f'users_list is: {users_list}')
                items_users_dict[item_id] = users_list
                users_list.append(user_id)
                self.logger.debug(f'items_users_dict is: {items_users_dict}')

        for item in items_users_dict:
            self.logger.debug(f'item is: {item}')
            item_uin = self.db_queries.select_row(f'SELECT uin FROM items WHERE id = {item}')
            current_users_ids = items_users_dict[item]
            self.logger.debug(f'current_users_ids is: {current_users_ids}')
            email_records = self.db_queries.select_emails_to_notify(tuple(current_users_ids))
            self.logger.debug(f'email_records are: {email_records}')

            emails_to_send = ""
            for email in email_records:
                self.logger.debug(f'email is: {email}')
                self.logger.debug(f'uin is: {item_uin}')
                emails_to_send += (f', {email[0]}')
            email_utilities.send_target_price_mail(emails_to_send, item_uin[0])

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        self.logger.debug('Hashing password.')
        return (salt + pwdhash).decode('ascii')

    def verify_password(self, stored_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      user_input_utilities.input_user_password().encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        self.logger.debug('Verifying password.')
        return pwdhash == stored_password

    # def hash_password(password):
    #     """Hashing password"""
    #     salt = bcrypt.gensalt()
    #     hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    #     self.logger.debug('Hashing password.')
    #     return hashed_password.decode('utf-8')

    # def check_password(hashed_password):
    #     """Checking hashed password"""
    #     if bcrypt.checkpw(user_input_utilities.input_user_password().encode('utf8'), hashed_password.encode('utf8')):
    #         self.logger.debug('Password matches!')
    #         return True
    #     self.logger.debug('Password not matches!')
    #     print('Wrong password!')
    #     return False
