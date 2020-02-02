import myLogger
from SETTINGS.STATICS import PREFIX

logger = myLogger.getLogger("CMD")

logger.debug("file: CMD")


def cmds():
    logger.info("fnc: cmd")
    return [
        ['help', 'Dir ist nicht mehr zu helfen'],
        ['first', 'Ich war schon lang vor dir hier']
    ]


async def command(message):
    logger.info(message.content)
    logger.info("fnc: command")

    msg = message.content
    cm = cmds()

    if msg.startswith(PREFIX):
        msg = msg[len(PREFIX):]
    else:
        return
    for cols in cm:
        if msg == cols[0]:
            logger.debug("fnc: command found")
            await message.channel.send(cols[1])
            return
        else:
            logger.debug("fnc: command not found")


commands = [
    'help',
    'first', ]
