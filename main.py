from random import choice
from verses import Verses
import logging
from time import sleep
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
api = create_api()


def tweet():
    while True:
        verses = choice(Verses)
        logger.info("updating status.....")
        api.update_status(verses)
        logger.info("sleeping")
        sleep(60*60*4)


if __name__ == "__main__":
    tweet()
