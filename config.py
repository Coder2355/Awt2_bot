import os

TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID", "21740783")
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH", "a5dc7fec8302615f5b441ec5e238cd46")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7496680438:AAHyEZDGnIoARpfywrzQOhB27un9pja49p4")

#port to run web server
PORT = int(os.getenv('PORT', "8080"))

if not all([TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_BOT_TOKEN]):
    raise ValueError("Please set the TELEGRAM_API_ID, TELEGRAM_API_HASH, and TELEGRAM_BOT_TOKEN environment variables")
