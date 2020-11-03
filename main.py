import user_input_utilities, request_utilities, data_parser, data_base_utilities, consts
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
#
# data_base_utilities.create_users_table()

query1 = "INSERT INTO users(email, password) VALUES('gmail', 123456)"

query2 = ("select * from items")
# record = ('bezeq', '123456')

vars_item = ('עכבר גיימרים', 165, 165)

data_base = Database(consts)
data_base.connect()
# data_base.insert_into_table(query1)
# data_base.add_user(record)
# data_base.select_rows(query2)
dict = data_base.select_rows_dict_cursor(query2)
print(dict)
print(data_base.conn.closed)
data_base.add_item(vars_item)