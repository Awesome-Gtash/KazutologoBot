# Rewrite this config.py.
import json
import os


def get_user_list(config, key):
    with open(f"{os.getcwd()}/Kazutologobot/{config}", "r") as json_file:
        return json.load(json_file)[key]


# Rewrite this config.py.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 1234567  # integer value, dont use ""
    API_HASH = "123458494" # dont remove ""
    TOKEN = ""  # This var used to be API_KEY but it is now TOKEN, adjust accordingly don't remove "".
    OWNER_ID = 5189767566  # If you dont know, your id? Then do /id in your private chat with it or other bot, also an integer & Dont Use ""
    OWNER_USERNAME = "Awesome_MB" # Your Username, Don't add the @
    SUPPORT_CHAT = "Tiger_SupportChat" # Your own group for support, don't add the @
    JOIN_LOGGER = (
        -1001640096539
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001640096539
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    URL = None
    OPTIONAL
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
        WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )


class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True  # Rewrite this config.py.


import json
import os


def get_user_list(config, key):
    with open(f"{os.getcwd()}/Kaxutologobot/{config}", "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 1234567  # integer value, dont use ""
    API_HASH = "12345abcdefg23459" # dont remove ""
    TOKEN = ""  # This var used to be API_KEY but it is now TOKEN, adjust accordingly & dont remove "".
    OWNER_ID = 5189767566  # If you dont know, run the bot and do /id in your private chat with it, also an integer & dont use ""
    OWNER_USERNAME = "Awesome_MB" # Your ID dont add the @
    SUPPORT_CHAT = "Tiger_SupportChat"  # Your own group for support, dont add the @
    JOIN_LOGGER = (
        -1001640096539
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001640096539
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    URL = None

    # OPTIONAL
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
