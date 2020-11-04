import logging
from re import sub
from decimal import Decimal

logger = logging.getLogger(__name__)


def get_title_and_price(source_text_beautiful):
    """Function that scraping for the price and title from a link, returning tuple of both."""
    price_div = source_text_beautiful.find(class_="div-options-prices")
    price = price_div.span.text
    logger.debug(f'The price is: {price}.')
    title_div = source_text_beautiful.find(class_="title-text")
    title = title_div.span.text
    logger.debug(f'The title is: {title}.')

    return (title, price)


def change_price_from_str_to_decimal(item_price):
    """Function that converting string of price to decimal."""
    decimal_price = Decimal(sub(r'[^\d.]', '', item_price))
    logger.debug(f'The price is {item_price}.')
    return decimal_price
