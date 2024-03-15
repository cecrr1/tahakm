#يوسف المبرمج
#@cecrr
from pyrogram import Client, enums
# Requier os Modules 
import os 
# Requier Bot Databesas 
from Utils.databesas import Databesas

class config:
    API_KEY : str = "6821052742:AAGH-" # توكين بوتك
    API_HASH: str = "23757c1adfb5" # ايبي هاش
    API_ID  : int = 846 # ايبي ايدي
    SUDO    : int = 6207674867 # ايدي المطور

# Check Extist 
if not os.path.exists('./.session'): # Check session folder 
    os.mkdir('./.session')  # Create session folder
if not os.path.exists('./data'): # Check data Folder
    os.mkdir('/data') # Create data folder

# Databesas class 
databesas = Databesas()

# Temp Data
temp = {}

# Stary Pyrogram CLient
app = Client(
    name='./.session/rad', 
    api_hash=config.API_HASH, 
    api_id=config.API_ID ,
    bot_token=config.API_KEY, 
    plugins=dict(root="Plugins"),
    parse_mode=enums.ParseMode.DEFAULT
)

