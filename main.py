from random import choice
from verses import Verses
from time import sleep
from config import create_api


api = create_api()


def tweet():
    while True:
        verses = choice(Verses)
        api.update_status(verses)
        sleep(60*60*12)


if __name__ == "__main__":
    tweet()
    
