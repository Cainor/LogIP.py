import sys
import logging
import requests
from time import sleep

site = "https://ifconfig.me/ip"
IP = ""

sleepSeconds = 300


def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('log.txt', mode='a+')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger


logger = setup_custom_logger('NIC')

while (True):
    try:
        response = requests.get(site)
        logger.info(response.text)
        sleep(sleepSeconds)
    except:
        sleep(sleepSeconds)
