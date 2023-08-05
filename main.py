import discord
import account_interactions as acc
from keep_alive import keep_alive
from cap import cap
from cap import balance
from discord.ext import commands
import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix=["ex!", "Ex!", "el!", "El!"],
                      case_insensitive=True,
                      intents_members=True,
                      intents = intents)
c_name = "EL Marks"

admins = ["838104737642971178", "806666676023066678", "740951072780058684", "554081235245334534"]

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('el!help - Created by the Government of Gapla for Excelsioran-Libertasian Cooperative Bank'))
    print("Excelsior-Libertas Bank Bot is ready. \n")

@client.command(help="Checks yours or other people's balances")
async def bal(ctx, user:discord.Member=None):
  if user == None:
    await ctx.send(f"`{str(ctx.author)} has : [{acc.bal(str(ctx.author.id))}] EL Marks!`")
  else:
    user = str(user.mention)
    a = user.replace("<","")
    a = a.replace(">","")
    a = a.replace("@","")
    a = a.replace("!","")
    user = await client.fetch_user(a)
    await ctx.send(f"`{user} has [{acc.bal(str(user.id))}] El Marks!`")

@client.command(help="The command to allow admins to add or subtract money from your balance")
async def add(ctx, amount, user:discord.Member=None):
  if str(ctx.author.id) in admins:
    if cap(amount):
      user = str(user.mention)
      a = user.replace("<","")
      a = a.replace(">","")
      a = a.replace("@","")
      a = a.replace("!","")
      user = await client.fetch_user(a)
      await ctx.send(f"`{user} now has [{acc.add(str(user.id), amount)}] EL Marks!`")
    else:
      await ctx.send("`ERROR: This transaction will result in the cap being exceeded. To change the cap, please contact Wyatt.`")
  else:
    await ctx.send("`you no admin, so stop try to rob bank`")

@client.command(help="Lets the admins set your bank account balance")
async def set(ctx, amount, user:discord.Member=None):
  if str(ctx.author.id) in admins:
    if cap(amount):
      user = str(user.mention)
      a = user.replace("<","")
      a = a.replace(">","")
      a = a.replace("@","")
      a = a.replace("!","")
      user = await client.fetch_user(a)
      await ctx.send(f"`{user} now has [{acc.set(str(user.id), amount)}] EL Marks!`")
    else:
      await ctx.send("`ERROR: This transaction will result in the cap being exceeded. To change the cap, please contact Wyatt.`")
  else:
    await ctx.send("`you no admin, so stop try to rob bank`")

@client.command(help="Gift other people EL Marks!")
async def gift(ctx, amount, user:discord.Member=None):
  if user == None:
    await ctx.send("`Please enter a VALID username!`")
  else:
    user = str(user.mention)
    a = user.replace("<","")
    a = a.replace(">","")
    a = a.replace("@","")
    a = a.replace("!","")
    user = await client.fetch_user(a)
    ou = acc.gift(str(ctx.author.id), amount, str(user.id))
    print(ou)
    if ou == "AC":
      await ctx.send(f"`{str(ctx.author)} now has [{acc.bal(str(ctx.author.id))}] EL Marks and {str(user)} now has [{acc.bal(str(user.id))}] EL Marks`")
    else:
      await ctx.send("`invalid balance/negative amount`")

@client.command(help="Information about the EL Mark")
async def info(ctx):
  await ctx.send("`Information about the EL Mark`")
  await ctx.send("Monetary union members: Excelsior, Libertas")
  await ctx.send("Official users: Excelsior, Libertas, Bryantia, Cotter Menaceland")

@client.command(help="View information about the EL Mark's circulation")
async def supply(ctx):
  await ctx.send("Current circulation: " + str(balance()))
  await ctx.send("Maximum circulation: " + str(6000000))

keep_alive()

client.run(os.environ['newkey'])