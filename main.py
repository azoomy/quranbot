import logging
from config import create_api
from random import randint
from time import sleep
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
api = create_api()


def bring_verse(verse):
    url = 'http://api.alquran.cloud/ayah/' + str(verse) + '/editions/quran-uthmani,en.pickthall'
    json_data = requests.get(url).json()
    verse_en = json_data['data'][1]['text']
    surah = json_data['data'][0]['surah']['englishName'] + \
            '(' + str(json_data['data'][0]['surah']['number']) + '):' + \
            str(json_data['data'][0]['numberInSurah'])
    return [verse_en, surah]


def main():
    ayah_no = randint(1, 6237)
    ayah = bring_verse(ayah_no)
    if len(ayah[0]) > 250:
        main()
    else:
        ayah_tweet = ayah[0] + " - " + ayah[1]
        logger.info(ayah_tweet)
        api.update_status(ayah_tweet)


def tweet():
    while True:
        logger.info("updating...")
        main()
        logger.info("sleeping...")
        sleep(60 * 60 * 4)


if __name__ == "__main__":
    tweet()
