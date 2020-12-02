import consts
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logger = logging.getLogger(__name__)

s = smtplib.SMTP(host=consts.SMTP_HOST, port=587)
s.starttls()
s.login(consts.SMTP_ADDRESS, consts.SMTP_PASSWORD)


def send_target_price_mail(email, item_uin):
    msg = MIMEMultipart()  # create a message

    message = f'The item that you wanted is now at the target price, item link: {consts.URL_TO_ADD_UIN + item_uin}.'

    # setup the parameters of the message
    msg['From'] = consts.SMTP_ADDRESS
    msg['To'] = email
    msg['Subject'] = consts.EMAIL_MESSAGE_TITLE
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    # send the message via the server set up earlier.
    s.send_message(msg)
    logger.debug(f'Sending email to: {email}, about target price to uin:{item_uin}.')

    del msg


def send_out_of_stock_mail(email, item_title):
    msg = MIMEMultipart()  # create a message
    message = f'The item that you wanted is now out of stock, item title: {item_title}.'

    # setup the parameters of the message
    msg['From'] = consts.SMTP_ADDRESS
    msg['To'] = email
    msg['Subject'] = consts.EMAIL_MESSAGE_TITLE

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    logger.debug(f'Sending email to: {email}, about out of stock itme to item:{item_title}.')

    del msg
