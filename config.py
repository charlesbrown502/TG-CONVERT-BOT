import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    #AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    BANNED_USER = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    MAX_MESSAGE_LENGTH = 4096
    DB_URI = os.environ.get("DATABASE_URL", "")
