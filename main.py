import discord
import response

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("BOT IS ONLINE")

@client.event
async def on_message(message):
    author = message.author
    guild = message.guild

    if message.content == "?zvz":
        zvz = 964540483357515856
        role = guild.get_role(zvz)
        membrosRole = role.members

        await response.reponseTime(message)

        await message.channel.send(f'{author.mention} os players de ZvZ são:')
        for member in membrosRole:
            text = f'{member}'
            await message.channel.send(text)


    if message.content == "?capitacao":
        capitacao = 964540528895078420
        role = guild.get_role(capitacao)
        membrosRole = role.members

        await response.reponseTime(message)

        await message.channel.send(f'{author.mention} os players de capitação são:')
        for member in membrosRole:
            text = f'{member}'
            await message.channel.send(text)



client.run("Your Token")