import asyncio
import random
import discord

import SECRETS


class MyClient(discord.Client):

    # Wenn der Bot sich einloggen konnte
    async def on_ready(self):
        print('Eingeloggt als \n' + self.user.name + ' ' + self.user.id.__str__() + '\n -----------')

    # Wenn eine Reaktion hinzugefügt wird
    async def on_reaction_add(self, reaction, user):
        print(reaction.emoji + '\n' + user.__str__())

    # Wenn eine Reaktion entfernt wird
    async def on_reaction_remove(self, reaction, user):
        print(reaction.emoji + ' Removed\n' + user.__str__())

    # Wenn eine Nachricht gesendet wird
    async def on_message(self, message):

        if message.author.id == self.user.id:
            return

        # print(message.author.id)
        ###########
        if message.content.startswith('$thumb'):
            channel = message.channel
            await channel.send('Send me that \N{THUMBS UP SIGN} reaction, mate')

            def check(reaction, user):
                return user == message.author and str(reaction.emoji) == '\N{THUMBS UP SIGN}'

            try:
                reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
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
        msg = '**{0.author}** edited their message:\n{0.content} -> {1.content} \n in {0.channel.mention}'
        # await before.channel.send(format.format(before, after))
        await before.guild.get_member(272086128830447620).send(msg.format(before, after))

    # Wenn eine Nachricht gelöscht wird
    async def on_meggage_delete(self, message):
        msg = '{0.author} has deleted the message: \n {0.content}'
        await message.guild.get_member(272086128830447620).send(msg.format(message))

    # Wenn ein Member den Server joint
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Willkommen {0.mention}'.format(member)
            await guild.system_channel.send(to_send)

    # Wenn ein Member den Server verlässt
    async def on_member_remove(self, member):
        print('' + member.name)

    # Wenn ein Member das Profil updated, Wenn min. einer der folgenden Dinge sich geändert haben:
    # Status, Aktivität, Nickname, Rollen
    async def on_member_update(self, before, after):
        print(before)
        print("to")
        print(after)

    # Wenn ein Member eins der folgenden updatet: Avatar, Username, Diskriminator
    async def on_user_update(self, befor, after):
        print(befor)

    #
    async def on_voice_state_update(self, member, before, after):
        print('Voice state update')


client = MyClient()
client.run(SECRETS.TOKEN)
