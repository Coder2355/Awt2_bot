import os, time

class Config(object):
    #Audio-_edit_bot client Config 
    API_ID = os.getenv("API_ID", "21740783")
    API_HASH = os.getenv("API_HASH", "a5dc7fec8302615f5b441ec5e238cd46")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7496680438:AAHyEZDGnIoARpfywrzQOhB27un9pja49p4")

    #port to run web server
    PORT = int(os.getenv('PORT', "8080"))

    # database config
    DB_NAME = os.environ.get("DB_NAME","Speedwolf1")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://Speedwolf1:speedwolf24689@cluster0.rgfywsf.mongodb.net/")


    # other configs
    BOT_UPTIME  = time.time()

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))

    
class Txt(object):
    
    START_TXT = """Hello {} 
    
➻ This Is An Advanced Editor bot .
    
➻ Using This Bot you can remove audio and trim videos in the file .
    
➻ the other Amazing features are coming soon.
    
<b>Bot Is Made By @Anime_Warrior_Tamil</b>"""
    
    ABOUT_TXT = f"""<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}>Click here</a>\n○ Channel : @Anime_Warrior_Tamil\n○ Support Group : @+NITVxLchQhYzNGZl</b>", 
    
<b>♻️ Bot Made By :</b> @Anime_Warrior_Tamil"""
    
    PROGRESS_BAR = """\n
<b>📁 Size</b> : {1} | {2}
<b>⏳️ Done</b> : {0}%
<b>🚀 Speed</b> : {3}/s
<b>⏰️ ETA</b> : {4} """

    HELP_TXT = """<b>Hey</b> {}
    
see the command of my bot."""



#This bot was created by Awt botz
