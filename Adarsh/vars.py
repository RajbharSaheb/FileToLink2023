# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '20389440'))
    API_HASH = str(getenv('API_HASH', 'a1a06a18eb9153e9dbd447cfd5da2457'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', ''))
    name = str(getenv('name', 'xstreamrbbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001930913574'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'rajbharsaheb'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "".format(FQDN)
    else:
        URL = "".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://rajbharneeraj9m:pahadan@pahadan.avpz1pc.mongodb.net/?retryWrites=true&w=majority&appName=pahadan'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'Rajbharbotz'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001787367899")).split())) 
