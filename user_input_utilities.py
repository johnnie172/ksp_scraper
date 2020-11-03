import logging
import consts

logger = logging.getLogger(__name__)


def input_link():
    answer_item_link = input(str("Please enter KSP product link(starting with https://) : "))

    if answer_item_link[0:8] == 'https://' and answer_item_link[-1].isnumeric():
        logger.info('The answer_item_link is: {}'.format(answer_item_link))
        return answer_item_link
    else:
        logger.error(f'user answer_item_link is invalid the input was: {answer_item_link}')
        raise Exception(consts.LINK_ERROR_MESSAGE)

