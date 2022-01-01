#################################
# Etiraf Club Bot #
#################################
# Repo Sahibi - aykhan_s
# Telegram - t.me/aykhan_s
# Support - t.me/RoBotlarimTg
# GitHub - aykhan026
#################################
# Bu repo sıfırdan yığılıb
# Reponu öz adına çıxaran peysərdi...!!!
#################################

import os
import heroku3
from telethon import TelegramClient, events
#
# Telethon
api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")

# Client
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

# Owner
admin_qrup = int(os.environ.get("ADMIN_QRUP"))
etiraf_qrup = int(os.environ.get("ETIRAF_QRUP"))
kanal = os.environ.get("kanal")
log_qrup = int(os.environ.get("LOG_QRUP"))
botad = os.environ.get("BOT_AD")
sahib = int(os.environ.get("SAHIB"))

# Mesajlar
etirafmsg = os.environ.get("etirafmsg")
startmesaj = os.environ.get("startmesaj")
etirafyaz = os.environ.get("etirafyaz")
nosahib = os.environ.get("nosahib")
qrupstart = os.environ.get("qrupstart")
gonderildi = os.environ.get("gonderildi")


# Heroku
heroku_api = "https://api.heroku.com"
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
Heroku = heroku3.from_key(HEROKU_API_KEY)
#