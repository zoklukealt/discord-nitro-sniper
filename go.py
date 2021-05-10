import os
import discord

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
  print(f"{bcolors.Blue}{text}")

if os.name == 'nt':
  def clear():
    os.system("cls")
else:
  def clear():
    os.system("clear")
    
client = commands.Bot(command_prefix='>', self_bot=True)

print("
