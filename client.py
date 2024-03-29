import asyncio
import random
import discord
import SECRETS
from discord import *
from SETTINGS.STATICS import *
from commands import cmd
import myLogger

logger = myLogger.getLogger("Client")
logger.debug("client")


class MyClient(discord.Client):

    # Wenn der Bot sich einloggen konnte
    async def on_ready(self):

        logger.info("Logged in")

    #  print('Eingeloggt als \n' + self.user.name + ' ' + self.user.id.__str__() + '\n -----------')

    # Wenn eine Reaktion hinzugefügt wird
    async def on_reaction_add(self, reaction, user):
        logger.info("Reaction wurde hinzugefügt")

    #  print(reaction.emoji + '\n' + user.__str__())

    # Wenn eine Reaktion entfernt wird
    async def on_reaction_remove(self, reaction, user):
        logger.info("Reaction wurde entfernt")

    #  print(reaction.emoji + ' Removed\n' + user.__str__())

    #Eine Reaktion aus dem Cache
    async def on_raw_reaction_add(self, payload):
        logger.info("Raw Reaction add")

        channel = self.get_channel(payload.channel_id)
        user = self.get_user(payload.user_id)
        message = await channel.fetch_message(payload.message_id)
        #await channel.send(str(user)+ "reacted on" + message.content + "witch" + str(payload.emoji))
        logger.debug(str(user)+ "reacted on" + message.content + "witch" + str(payload.emoji))
    # Wenn eine Nachricht gesendet wird
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        logger.info("Nachricht wurde gesendet")
        logger.debug(message)
        logger.debug(message.author)
        user = message.author
        print(user.activities)
        await cmd.command(message)

        ###########
        if message.content.startswith('$thumb'):
            channel = message.channel
            await channel.send('Send me \N{THUMBS UP SIGN} reaction')

            def check(reaction, user):
                return user == message.author and str(reaction.emoji) == '\N{THUMBS UP SIGN}'

            try:
                reaction, user = await self.wait_for('reaction_add', timeout=45.0, check=check)  # client -> self
            except asyncio.TimeoutError:
                await channel.send('\N{THUMBS DOWN SIGN}')
            else:
                await channel.send('\N{THUMBS UP SIGN}')

        ###########
        if message.content.startswith('$guess'):
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send('Oops. It is actually {}.'.format(answer))

    # Wenn eine Nachricht bearbeitet wird
    async def on_message_edit(self, before, after):
        logger.info("Nachricht wurde bearbeitet")
        msg = '**{0.author}** edited their message:\n{0.content} -> {1.content} \n in {0.channel.mention}'
        # await before.channel.send(format.format(before, after))
        await before.guild.get_member(272086128830447620).send(msg.format(before, after))

    # Wenn eine Nachricht gelöscht wird
    async def on_meggage_delete(self, message):
        logger.info("Nachricht wurde entfernt")
        msg = '{0.author} has deleted the message: \n {0.content}'
        await message.guild.get_member(272086128830447620).send(msg.format(message))

    # Wenn ein Member den Server joint
    async def on_member_join(self, member):
        logger.info("Member ist gejoint")
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Willkommen {0.mention}'.format(member)
            await guild.system_channel.send(to_send)

    # Wenn ein Member den Server verlässt
    async def on_member_remove(self, member):
        logger.info("Member ist geleavt")

    #   print('' + member.name)

    # Wenn ein Member das Profil updated, Wenn min. einer der folgenden Dinge sich geändert haben:
    # Status, Aktivität, Nickname, Rollen
    async def on_member_update(self, before, after):
        logger.info("Member Update")
        logger.debug(str(before.joined_at))
        logger.debug(str(before.activites))
        logger.debug(str(before.guild))
        logger.debug(str(before.nick))
        logger.debug(str(before.mobile_status))
        logger.debug(str(before.desktop_status))
        logger.debug(str(before.web_status))
        logger.debug(str(before.roles))
        logger.debug(str(before.avatar))



    #   print(before)
    #   print("to")
    #   print(after)

    # Wenn ein Member eins der folgenden updatet: Avatar, Username, Diskriminator
    async def on_user_update(self, befor, after):
        logger.info("User Update")

    #   print(befor)

    #
    async def on_voice_state_update(self, member, before, after):
        logger.info("Voice state Update")
    #  print('Voice state update')


def client_run():
    client = MyClient()
    client.run(SECRETS.TOKEN)
    return client
