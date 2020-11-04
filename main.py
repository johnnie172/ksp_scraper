import user_input_utilities, request_utilities, data_parser, consts
from data_base_utilities import Database

import logging

logging.basicConfig(filename='ksp_scraper.log', level=10
                    , format='%(asctime)s: %(module)s: %(funcName)s: %(levelname)s: %(message)s')

logger = logging.getLogger(__name__)

# user_link = user_input_utilities.input_link()
#
# text = request_utilities.get_text_from_url(user_link)
#
# price_title_tuple = data_parser.get_title_and_price(text)
# print(price_title_tuple[0])
# print(price_title_tuple[1])


query1 = "INSERT INTO users(email, password) VALUES('gmail', 123456)"

query2 = ("select * from items")
# record = ('bezeq', '123456')

user_email = 'gmail'
user_password = '123456'

item_title = 'מקלדת גיימרים'
item_price = 300
lowest_price = 300



# data_base = Database(consts)
# data_base.connect()
# # data_base._db_setup()
#
#
# # data_base.insert_into_table(query1)
# # data_base.add_user(record)
# # data_base.select_rows(query2)
# dict = data_base.select_rows_dict_cursor(query2)
# print(dict)
# print(data_base.conn.closed)
# data_base.add_item(item_title, item_price, lowest_price)
# data_base.add_user(user_email, user_password)

if __name__ == '__main__':



    text = request_utilities.get_text_from_url(user_input_utilities.input_link())
    title_and_price = data_parser.get_title_and_price(text)
    price = data_parser.change_price_from_str_to_decimal(title_and_price[1])
    title = title_and_price[0]
    database = Database(consts)
    database.connect()
    database._db_setup()
    database.add_item(title, price)
