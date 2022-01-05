from pyrogram import Client

plugins = dict(root="plugins")
app = Client("ScommesseBot", config_file="config/config.ini", plugins=plugins).run()



