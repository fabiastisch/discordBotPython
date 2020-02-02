import myLogger
import data.database as database
from SETTINGS.STATICS import PREFIX


logger = myLogger.getLogger("CMD")

logger.debug("file: CMD")


async def command(message):
    logger.info(message.content)
    logger.info("fnc: command")
    msg = message.content

    if msg.startswith(PREFIX):
        msg = msg[len(PREFIX):]

        cm = cmds()

        for cols in cm:
            if msg == cols[0]:
                logger.debug("fnc: command found")
                await message.channel.send(cols[1])
                return
            else:
                logger.debug("fnc: command not found")
    else:
        msg = msg.strip()
        msg_upper = msg.upper()
        if msg_upper.startswith("NEW"):
            logger.debug("fnc: NEW")
            msg_upper = msg_upper[3:].strip()
            msg = msg[3:].strip()
            if msg_upper.startswith("COMMAND"):
                logger.debug("fnc: COMMAND")
                msg = msg[7:].strip()
                cod = msg.split()

                logger.info(cod)
                print(len(cod))
                if len(cod) == 2:
                    database.insert_command(database.Command(cod[0], cod[1]))
                elif len(cod) == 3:
                    database.insert_command(database.Command(cod[0], cod[1], cod[2]))

                database.get_command_list()
            else:
                return
        else:
            return


def cmds():
    logger.info("fnc: cmd")
    return [
        ['help', 'Dir ist nicht mehr zu helfen'],
        ['first', 'Ich war schon lang vor dir hier']
    ]
