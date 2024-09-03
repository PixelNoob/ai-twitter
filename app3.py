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

# Set up your OpenAI API key
api_key = os.getenv("openai")


# Load the list of supplements
supplements = [
    "Vitamin C", "Vitamin D", "Vitamin E", "Vitamin A", "Vitamin K", "Vitamin B1 (Thiamine)", 
    "Vitamin B2 (Riboflavin)", "Vitamin B3 (Niacin)", "Vitamin B5 (Pantothenic Acid)", 
    "Vitamin B6 (Pyridoxine)", "Vitamin B7 (Biotin)", "Vitamin B9 (Folate)", 
    "Vitamin B12 (Cobalamin)", "Calcium", "Magnesium", "Zinc", "Iron", "Copper", 
    "Manganese", "Selenium", "Chromium", "Iodine", "Potassium", "Sodium", "Phosphorus", 
    "Omega-3 Fatty Acids (Fish Oil)", "Omega-6 Fatty Acids", "Omega-9 Fatty Acids", 
    "Coenzyme Q10 (CoQ10)", "Alpha-Lipoic Acid", "N-Acetylcysteine (NAC)", "L-Glutamine", 
    "L-Arginine", "L-Carnitine", "L-Tyrosine", "L-Theanine", "L-Lysine", "L-Proline", 
    "L-Serine", "L-Citrulline", "L-Leucine", "L-Isoleucine", "L-Valine", "Creatine", 
    "Beta-Alanine", "Taurine", "GABA (Gamma-Aminobutyric Acid)", "5-HTP (5-Hydroxytryptophan)", 
    "Melatonin", "Probiotics", "Prebiotics", "Fiber (Psyllium Husk)", "Collagen", 
    "Glucosamine", "Chondroitin", "MSM (Methylsulfonylmethane)", "Hyaluronic Acid", 
    "Resveratrol", "Curcumin (Turmeric Extract)", "Quercetin", "Echinacea", "Elderberry", 
    "Garlic Extract", "Ginkgo Biloba", "Ginseng", "Ashwagandha", "Rhodiola Rosea", 
    "Maca Root", "Saw Palmetto", "Milk Thistle", "Aloe Vera", "Green Tea Extract", 
    "Red Yeast Rice", "Spirulina", "Chlorella", "Whey Protein", "Casein Protein", 
    "Pea Protein", "Soy Protein", "Rice Protein", "Hemp Protein", "Caffeine", 
    "Green Coffee Bean Extract", "Raspberry Ketones", "CLA (Conjugated Linoleic Acid)", 
    "MCT Oil (Medium-Chain Triglycerides)", "Coconut Oil", "Olive Leaf Extract", 
    "Bilberry", "Astaxanthin", "Beta-Glucan", "Bromelain", "Papain", "Grape Seed Extract", 
    "Alpha-GPC", "Phosphatidylserine", "SAMe (S-Adenosyl Methionine)", 
    "DHEA (Dehydroepiandrosterone)", "Tribulus Terrestris", "Fenugreek"
]

# Select a random supplement from the list
selected_prompt = "Write a factual tweet about this supplement {}".format(random.choice(supplements))

# Call the OpenAI API to generate a response using GPT-4
response = r.post(
    "https://api.openai.com/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "gpt-4-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You write tweets about diet supplements and its benefits"
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

# Tweet It

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
