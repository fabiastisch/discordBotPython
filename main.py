import asyncio

import discord

import SECRETS


class MyClient(discord.Client):

    async def on_ready(self):
        print('Eingeloggt als \n' + self.user.name + ' ' + self.user.id.__str__() + '\n -----------')

    async def on_message(self, message):
        if message.content.startswith('!editme'):
            msg = await message.channel.send('10')
            await asyncio.sleep(3.0)
            await msg.edit(content='40')

    async def on_message_edit(self, before, after):
        fmt = '**{0.author}** edited their message:\n{0.content} -> {1.content}'
        await before.channel.send(fmt.format(before, after))

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Willkommen {0.mention}'.format(member)
            await guild.system_channel.send(to_send)


client = MyClient()
client.run(SECRETS.TOKEN)
