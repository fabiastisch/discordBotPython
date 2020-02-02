import myLogger

logger = myLogger.getLogger("Commands")

logger.debug("file: Commands")


def cmds():
    logger.info("fnc: cmd")
    return [
        ['help', 'Dir ist nicht mehr zu helfen'],
        ['first', 'Ich war schon lang vor dir hier'],
    ]
