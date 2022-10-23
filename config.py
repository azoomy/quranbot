import tweepy
import logging
import os
import credentials
logger = logging.getLogger()


def create_api():
    consumer_key = os.getenv(credentials.CONSUMER_KEY)
    consumer_secret = os.getenv(credentials.CONSUMER_SECRET)
    access_token = os.getenv(credentials.ACCESS_TOKEN)
    access_token_secret = os.getenv(credentials.ACCESS_TOKEN_SECRET)

    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
