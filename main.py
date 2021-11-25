from random import choice
from verses import Verses
import logging
from hadiths import Hadiths
from time import sleep
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
api = create_api()


def tweet():
    while True:
        hadith = choice(Hadiths)
        verses = choice(Verses)
        logger.info("updating status.....")
        api.update_status(verses)
        api.update_status(hadith)
        logger.info("sleeping")
        sleep(60 * 60 * 12)


if __name__ == "__main__":
    tweet()
