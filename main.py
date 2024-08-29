import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_API_TOKEN')
TARGET_CHANNEL_ID = int(os.getenv('TARGET_CHANNEL_ID'))
print(f"Token: {DISCORD_TOKEN}")
print(f"Token: {TARGET_CHANNEL_ID}")
# Configure intents for the bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


TARGET_CHANNEL_ID = int(os.getenv('TARGET_CHANNEL_ID'))
DISCORD_TOKEN = os.getenv('DISCORD_API_TOKEN')
def scarpe_data():
    print("Start scraping the data ")
    url='https://kalimatimarket.gov.np/'
    cookies = {
        'TawkConnectionTime': '0',
        'XSRF-TOKEN': 'eyJpdiI6IlVycENQQmR6S0MrUEMyanlPWEhNZHc9PSIsInZhbHVlIjoiSWFqb2dxQmplbTc1YjE1cW5qMTN3azE5akdMV0JhSmc5OWdERFNUb0s2SzV1SmgrcDRUVEVhYUxDY3hKZHhFcVUyK0RBVnpGZG1XR0ZoaXFIS3o4Z1FUWG44Qk8zMVdNRWJnbFg0S0RwNCtxK2V5SG9tUGNUbmZhMlByaUcvUFgiLCJtYWMiOiJkYTIzMWM1MmFmOTgwNzgxY2NmYTE1ZGM0YjhkNzlkYTNhZWJhOTdhZjU2ZWMzZDk0ZGRiMDI4Y2VlMTYwMGY5IiwidGFnIjoiIn0%3D',
        'kalimati_fruits_and_vegetable_market_development_board_session': 'eyJpdiI6IitQaTQ5NmpkV3RXTlpLb1c0UDhsZGc9PSIsInZhbHVlIjoiZnlGMENkQ1J4Y3N2V3B5d2pCSUZqbk9IejBSVkU0VlpCZlA0d3FVczlnMERNQjgzVnBFVkE4Q08yTnM3V1pnQmUxT1Z2WFZyajNiZWxGdGFXRUpINFFiS1NxQWtKN1o0WlZKdVhsZEpSVENPQXVPZXhBL29WNzExUWt1Zis5a0wiLCJtYWMiOiIyY2FhNzU4ODE4NTM1MDk4YTQ0NmM3ZjMwZjY2YjM5MjgyZDlhMTNmY2U5ZGE0NmFhMzBiYmI4MzZlOTQ1ODQwIiwidGFnIjoiIn0%3D',
        'twk_idm_key': '7sq0BHLaNgexpc6n8j0pi'
    }
  
    response = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')
    veg = table.find('tbody').find_all('tr')
    data = []
    for i in veg:
        columns = i.find_all('td')
        commodity = columns[0].get_text(strip=True)
        price = columns[1].get_text(strip=True)
        print(f"Scraped: {commodity} - {price}")  # Debug print

        data.append({
            "commodity": commodity,
            "price": price
        })

    message = "\n".join([f"{item['commodity']}: {item['price']}" for item in data])
    if len(message) > 1000:
        message = message[:1000] + '...'

    print("Scraped Data:\n", message)  
    return message

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    for guild in client.guilds:
        print(f'Connected to guild: {guild.name}')
    
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_data, CronTrigger(hour=21, minute=44)) 
    scheduler.start()
        

# Event to handle incoming messages
@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    if message.content.startswith('kitna'):
            try:
                print("Scrape command detected.") 
                scrape_message = scarpe_data()
                target_channel = client.get_channel(TARGET_CHANNEL_ID)
                if target_channel:
                    await target_channel.send(scrape_message)
                else:
                    print(f'Channel with ID {TARGET_CHANNEL_ID} not found.')
            except Exception as e:
                print(f'Error sending message: {e}')

@client.event 
async def send_data():
    print("Sending the Message in the estimated time ")
    scarped_message=scarpe_data()
    target_channel = client.get_channel(TARGET_CHANNEL_ID)
    if target_channel:
        await target_channel.send(scarped_message)
    else:
        print(f'Channel with ID {TARGET_CHANNEL_ID} not found.')

client.run(DISCORD_TOKEN)

  