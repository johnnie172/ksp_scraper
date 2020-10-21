import user_input_utilities, request_utilities, data_parser

import logging

logging.basicConfig(filename='ksp_scraper.log', level=30, format='%(asctime)s: %(module)s: %(levelname)s: %(message)s')

logger = logging.getLogger(__name__)

user_link = user_input_utilities.input_link()

text = request_utilities.get_text_from_url(user_link)

price_title_tuple = data_parser.get_title_and_price(text)
print(price_title_tuple[0])
print(price_title_tuple[1])
