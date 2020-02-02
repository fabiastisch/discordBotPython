import logging
import sys

logging.basicConfig(filename="logs/log.log", level=logging.INFO)
fh = logging.FileHandler("logs/logme.txt")
form = logging.Formatter('%(name)s - %(levelname)s : %(asctime)s - %(message)s')
fh.setFormatter(form)
logger = logging.getLogger("Bot")
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(form)


def getLogger(name):
    logger = logging.getLogger(name)
    logger.addHandler(fh)
    logger.addHandler(fh)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
