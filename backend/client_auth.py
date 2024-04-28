import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

client = tweepy_Client(
    bearer_token = os.getenv('BEARER_TOKEN'),
    consumer_key = os.getenv('CONSUMER_KEY'),
    consumer_secret= os.getenv("CONSUMER_SECRET"),
    access_token= os.getenv("ACCESS_TOKEN"),
    access_token_secret= os.getenv("ACCESS_SECRET"),
)