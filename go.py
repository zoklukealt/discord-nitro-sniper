import os
import discord
import requests
import re
import json

with open('config.json') as f:

    config = json.load(f)

# Opens the config file for easy setting access 
    
TOKEN = config.get("TOKEN")

# User token

class bcolors:
    Blue = '\033[94m'
    Cyan = '\033[96m'
    Green = '\033[92m'
    Warning = '\033[93m'
    Fail = '\033[91m'
    Bold = '\033[1m'
    Underline = '\033[4m'
    
def wtc(text):
  print(f"{bcolors.Warning}{text}")
def ptc(text):
  print(f"{bcolors.Green}{text}")

if os.name == 'nt':
  def clear():
    os.system("cls")
else:
  def clear():
    os.system("clear")
    
client = commands.Bot(command_prefix='>', self_bot=True)

@client.event()
async def on_message(message):
    if 'discord.gift/' in message.content or 'discord.com/gifts/' in message.content or 'discordapp.com/gifts/' in message.content:
            if "discord.gift/" in message.content:
                code = re.findall("discord[.]gift/(\w+)", message.content)
            if "discordapp.com/gifts/" in message.content:
                code = re.findall("discordapp[.]com/gifts/(\w+)", message.content)
            if 'discord.com/gifts/' in message.content:
                code = re.findall("discord[.]com/gifts/(\w+)", message.content)
        wtc(f"[NOTIFICATION] Nitro code was posted. From: {message.authour}. Full message: {message.content}. Currently checking...")
            headers = {'Authorization': token}
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text
            if 'This gift has been redeemed already.' in r:
                wtc("[NOTIFICATION] This gift was already redeemed.")
            if 'subscription_plan' in r:
                ptc("[SUCCESS] Nitro successfully claimed!")
