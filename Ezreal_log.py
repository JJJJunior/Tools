# *-*coding: utf-8 *-*

"""
author : Ezreal
"""

import logging


class EzrealLog():
    def __init__(self, filename):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        console_log = logging.StreamHandler()
        console_log.setFormatter(formatter)

        file_log = logging.FileHandler(filename)
        file_log.setFormatter(formatter)

        self.logger.addHandler(console_log)
        self.logger.addHandler(file_log)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

