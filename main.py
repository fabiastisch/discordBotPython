import discord
from discord import Game, Guild, Member, Embed
from commands import cmd_ping, STATICS


@client.event
async def on_ready():
    print("Logged in successfully.")
    # await client.send_message()
    for s in client.guilds:
        print(" - %s (%s)" % (s.name, s.id))

    game = discord.Game("with the API")
    await client.change_presence(activity=game, status=discord.Status.online)


@client.event
async def on_message(message):
    # Nicht auf eigene Nachrichten reagieren
    if message.author =

    if message.content.startswith(STATICS.PREFIX):
        invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[len(STATICS.PREFIX):]
        print("INVOKE: %s\nARGS: %s" % (invoke, args.__str__()))

        if commands.__contains__(invoke):
            await commands.get(invoke).ex(args, message, client, invoke)
        else:
            await client.send_message(message.channel, embed=Embed(color=discord.Color.red(), description=(
                    "Die Funktion `%s` ist nicht definiert!" % invoke)))

    print(message.content + " - " + message.author.name)


client.run(SECRETS.TOKEN)
