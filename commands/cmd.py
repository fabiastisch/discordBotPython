import myLogger
import data.database as database
from SETTINGS.STATICS import PREFIX

logger = myLogger.getLogger("CMD")

logger.debug("file: CMD")


async def do(message, com):
    s = database.get_command(com)
    await message.channel.send(s.out)


list = database.get_command_list()


def update_list():
    global list
    list = database.get_command_list()


async def command(message):
    logger.info(message.content)
    logger.info("fnc: command")
    msg = message.content

    if msg.startswith(PREFIX):
        msg = msg[len(PREFIX):]

        logger.info("Command: " + msg)

        for i in range(len(list)):
            if list[i][0] == msg:
                logger.info("Ist drin")

                await do(message, msg)
                return
        else:
            logger.info("Command not found")
            await message.channel.send("Command: \"" + msg + "\" not found.", delete_after=10)





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

                if len(cod) == 2:
                    ret = database.insert_command(database.Command(cod[0], cod[1]))
                elif len(cod) == 3:
                    ret = database.insert_command(database.Command(cod[0], cod[1], cod[2]))
                else:
                    await message.channel.send("This is not a valid usage of this command")
                    return
                if ret is False:
                    await message.channel.send("A command with this name already exists")
                else:
                    update_list()
                    await message.channel.send("New command created... Try type {} ".format(PREFIX + cod[0]))
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


'''
cm = cmds()

        for cols in cm:
            if msg == cols[0]:
                logger.debug("fnc: command found")
                await message.channel.send(cols[1])
                return
            else:
                logger.debug("fnc: command not found")'''
