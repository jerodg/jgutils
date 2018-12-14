#!/usr/bin/env python3.7
"""Get IPs: Jerod Gawne, 2017.03.22 <https://github.com/jerodg/jgutils>"""
import logging
import pprint
import socket
import sys
import traceback
from typing import NoReturn

import random
import requests

logger = logging.getLogger(__name__)
DBG = logger.isEnabledFor(logging.DEBUG)
NFO = logger.isEnabledFor(logging.INFO)


class GetIps(object):
    """GetIps"""
    URI = ('http://whatismyip.akamai.com',
           'http://myip.dnsomatic.com',
           'https://api.infoip.io/ip'
           'https://api.ipify.org/',
           'https://ipv4.icanhazip.com')
    URI6 = ('https://ipv6.icanhazip.com',
            'http://v6.ipv6-test.com/api/myip.php')

    def __init__(self):
        super().__init__()
        self.ips = {'lan4': None,
                    'lan6': None,
                    'wan4': None,
                    'wan6': None}

        self.getlan4()
        self.getlan6()
        self.getwan4()
        self.getwan6()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __repr__(self):
        pprint.pprint(self.__dict__)

    def getlan4(self) -> NoReturn:
        """
        :return: NoReturn"""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 53))
        self.ips['lan4'] = s.getsockname()[0]
        s.close()

    def getlan6(self) -> NoReturn:
        """
        :return: NoReturn"""
        s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        s.connect(('2001::aaaa', 53))
        self.ips['lan6'] = s.getsockname()[0]
        s.close()

    def getwan4(self) -> NoReturn:
        """
        :return: NoReturn"""
        uri = random.shuffle(self.URI)
        for u in uri:
            rs = requests.get(u)
            if rs.status_code == 200:
                self.ips['wan4'] = rs.text.strip()
                return
            else:
                logger.error('All hosts exhausted; WAN4 IP unknown')
                break

    def getwan6(self) -> NoReturn:
        """
        :return: NoReturn"""
        uri = random.shuffle(self.URI6)
        for u in uri:
            rs = requests.get(u)
            if rs.status_code == 200:
                self.ips['wan6'] = rs.text.strip()
                return
            else:
                logger.error('All hosts exhausted; WAN6 IP unknown')
                break


if __name__ == '__main__':
    try:
        print(__doc__)
    except Exception as excp:
        logger.exception(traceback.print_exception(*sys.exc_info()))
