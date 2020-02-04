import os, sqlite3
import myLogger

logger = myLogger.getLogger("database")
logger.debug("Database")
FILE = 'data/Discord.db'


class Command:
    def __init__(self, name, out, tts, description=None):
        self.name = name
        self.out = out
        self.description = description
        if tts:
            self.tts = 1
        else:
            self.tts = 0

def db_anlegen():
    logger.debug("DB anlegen")
    connection = sqlite3.connect(FILE)
    cursor = connection.cursor()
    # Tabellem erzeugen
    with connection:
        cursor.execute("""
                    CREATE TABLE commands(
                        name text not null, 
                        out text,
                        description text,
                        tts integer 
                    )"""
                       )

    print("Datenbank Discord.db angelegt")


def insert_command(command):
    logger.debug("Insert command")
    connection = sqlite3.connect(FILE)
    cursor = connection.cursor()
    with connection:
        cursor.execute("SELECT name FROM commands WHERE name = :name", {'name': command.name})
        e = cursor.fetchone()
        if e is not None:
            # if e[0] == command.name:
            return False

        cursor.execute("INSERT INTO commands VALUES (:name ,:out, :description, :tts)", {
            'name': command.name, 'out': command.out, 'description': command.description, 'tts': command.tts})


def update_command(command):
    # TODO: adding TTS
    logger.debug("update command")
    connection = sqlite3.connect(FILE)
    cursor = connection.cursor()
    with connection:
        if command.out is not None:
            cursor.execute("""UPDATE command SET out = :out WHERE name = :name""",
                           {'out': command.out, 'name': command.name})
        if command.description is not None:
            cursor.execute("""UPDATE command SET description = :description WHERE name = :name""",
                           {'description': command.description, 'name': command.name})


def get_command(name):
    logger.debug("get command")
    connection = sqlite3.connect(FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM commands WHERE name = :name", {'name': name})
    e = cursor.fetchone()
    connection.close()
    return Command(e[0], e[1], e[2], e[3])


def get_command_list():
    logger.debug("get command List")
    connection = sqlite3.connect(FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM commands ")
    e = cursor.fetchall()
    connection.close()

    print(e)
    return e


def delete_command(name):
    logger.debug("Delete command")
    connection = sqlite3.connect(FILE)
    cursor = connection.cursor()
    with connection:
        cursor.execute("DELETE from commands WHERE name = :name", {'name': name})


if not os.path.exists(FILE):
    print("Datenbank nicht vorhanden . Datenbank wird angelegt.")
    db_anlegen()
