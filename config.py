# Copyright (c) 2022 Itz-fork

import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "19134212"))
    API_HASH = os.environ.get("API_HASH", "0d85b66bf650d9d64ec178e51fa6b2c9")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5467887095:AAF0aAq7sErI1I3prL9-mj8MO9xJRp_aCy8")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1239693367 5588560522 5540091710").split())
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT", "true")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL","-1001657271959")) 
    # DON'T CHANGE THESE 2 VARS
    DOWNLOAD_LOCATION = "./ARKJ_Bots"
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD")
