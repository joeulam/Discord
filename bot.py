import discord
from discord.ext import commands
client = commands.Bot(command_prefix = '!')

#id = 704819240800092201

@client.event
async def on_message(message):
    id = client.get_guild(704819240800092201)
    if message.content.find("!hello") != -1:
        await message.channel.send("Hi")
    elif message.content == "!users":
        await message.channel.send(f"Number of Members: {id.member_count}")
    elif message.content == "!Goodnight":
        await message.channel.send("Goodnight guys sleep early!")
    elif message.content == "!help":
        embed = discord.Embed(title="Help on BOT", description="Some useful commands")
        embed.add_field(name="!hello", value="Greets the user")
        embed.add_field(name="!users", value="Prints number of users")
        embed.add_field(name="!Goodnight", value="Says goodnight to users")
        await message.channel.send(content=None, embed=embed)
    elif message.content == "!clear":
        await message.channel.delete(message)




client.run("NzA0ODM0ODYxMDI1ODUzNTcy.Xqjbcw.2zr1g_etEzWwG_oJSYj5CDtqoQ4")
