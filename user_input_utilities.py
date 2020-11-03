import logging
import consts

logger = logging.getLogger(__name__)


def input_link():
    """Function that asked user input for link to scrap."""
    answer_item_link = input(str("Please enter KSP product link(starting with https://) : "))

    if answer_item_link[0:8] == 'https://' and answer_item_link[-1].isnumeric():
        logger.info('The answer_item_link is: {}'.format(answer_item_link))
        return answer_item_link
    else:
        logger.error(f'user answer_item_link is invalid the input was: {answer_item_link}.')
        raise Exception(consts.LINK_ERROR_MESSAGE)


def input_target_price():
    """Function that asked user input for target price."""
    answer_target_price = input(int('Please enter the target price that you would like to be notify of:'))
    if answer_target_price.isnumeric():
        logger.debug(f'The answer_target_price is: {answer_target_price}')
        return answer_target_price
    else:
        logger.error(f'user answer_targer_price is invalid the input was: {answer_target_price}.')
        raise Exception(consts.TARGET_PRICE_ERROR_MESSAGE)
