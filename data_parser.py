import logging

logger = logging.getLogger(__name__)


def get_title_and_price(source_text_beautiful):
    price_div = source_text_beautiful.find(class_="div-options-prices")
    price = price_div.span.text
    logger.info(f'The price is: {price}')
    title_div = source_text_beautiful.find(class_="title-text")
    title = title_div.span.text
    logger.info(f'The title is: {title}')

    return (price, title)
