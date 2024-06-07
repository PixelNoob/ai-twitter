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

# Part 1 - OpenAI

# Set up your OpenAI API key
api_key = os.getenv("openai")

# Define a list of prompts to provide variety in the generated tweets
prompts = [
    "Can you give me a motivational tweet that inspires people to overcome challenges?",
    "Generate a motivational tweet about the importance of perseverance.",
    "Create a motivational tweet encouraging people to follow their dreams.",
    "Write a motivational tweet about the power of positive thinking.",
    "Give me a motivational tweet about finding strength in adversity.",
    "Provide a motivational tweet that emphasizes the value of hard work.",
    "Compose a motivational tweet about the benefits of staying focused and determined."
]

# Select a random prompt from the list
selected_prompt = random.choice(prompts)

# Call the OpenAI API to generate a response using GPT-4
response = r.post(
    "https://api.openai.com/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "gpt-4",
        "messages": [
            {
                "role": "system",
                "content": "You write spiritual motivational tweets"
            },
            {
                "role": "user",
                "content": selected_prompt
            }
        ]
    }
)

# Print the generated response
response = response.json()
tweet_final = response['choices'][0]['message']['content']
print(f'Tweet: {tweet_final}')

# Part 3 - Tweet It

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
print('Tweet sent, url:')
print(f"https://twitter.com/user/status/{response.data['id']}")
print('---------------------------')
