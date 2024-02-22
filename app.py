import requests as r
import json
import random
import tweepy

from dotenv import load_dotenv
import os

from datetime import datetime

timestamp = datetime.now()
formatted_timestamp = timestamp.strftime("%d-%m-%Y %H:%M:%S")
print(formatted_timestamp)

load_dotenv()

## PART 1 - GET NEWS API

news_api = os.getenv("news_api")

url = f'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={news_api}'
response = r.get(url).json()

number = random.randint(0, 7)

news = []

for i in response['articles']:
    if i['description'] != None and i['description'] != "[Removed]":
        #print(i['description'])
        news.append(i['description'])

tweet_news = news[number]
print(f'news obtained: {tweet_news}')

### PART 2 - OPEN AI

# Set up your OpenAI API key
api_key = os.getenv("openai")

# Call the OpenAI API to generate a response
response = r.post(
    "https://api.openai.com/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "system",
        "content": "You write tweets based on the news I send you, be as human as possible and be sarcastic when you find appropriate."
      },
      {
        "role": "user",
        "content": f"{tweet_news}"
      }
    ]}
)
# Print the generated response
response = response.json()
tweet_final = (response['choices'][0]['message']['content'])
print(f'Tweet: {tweet_final}')

## PART 3 - TWEET IT

consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

response = client.create_tweet(
    text=tweet_final
)
print('tweet sent, url:')
print(f"https://twitter.com/user/status/{response.data['id']}")
print('---------------------------')
