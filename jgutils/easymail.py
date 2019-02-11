#!/usr/bin/env python3.7
"""Easy Mail: Jerod Gawne, 2019.01.11 <https://github.com/jerodg>"""
import logging
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename, realpath
from sys import exc_info
from traceback import print_exception
from typing import NoReturn

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


# todo: add support for credentials


def easymail(**kwargs: dict) -> NoReturn:
    """:param kwargs: subject; str
                   sender; Optional[str]
                   recipients; List[str]
                   body; Optional[str] (supports html)
                   attachments; Optional[List[str]]
                   host; Optional[str]"""
    msg = MIMEMultipart('alternative')
    subject = kwargs.pop('subject')
    msg['Subject'] = subject
    sender = kwargs.pop('sender', 'donotreply@localhost')
    msg['From'] = sender
    recipients = kwargs.pop('recipients')
    msg['To'] = ', '.join(recipients)
    msg.attach(MIMEText(kwargs.pop('body', subject), 'html'))

    try:
        for attachment in kwargs.pop('attachment'):
            attachment = realpath(attachment)
            with open(attachment, 'rb') as afile:
                attachment = MIMEApplication(afile.read())
                attachment.add_header('Content-Disposition', 'attachment', filename=basename(attachment))
                msg.attach(attachment)
    except FileNotFoundError as fnfe:
        logger.warning(fnfe)
    except KeyError:
        pass

    server = smtplib.SMTP(kwargs.pop('host', 'localhost'))
    server.sendmail(sender, recipients, msg.as_string())
    server.quit()


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(print_exception(*exc_info()))
