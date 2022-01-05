from pyrogram import Client, filters, StopPropagation

from config.variabili import chatScommesse

plugins = dict(root="plugins")
app = Client("ScommesseBot", config_file="config/config.ini", plugins=plugins).run()


@app.on_message(group=-1)
def gruppo_non_valido(_, message):
    if message.chat.id not in chatScommesse:
        message.reply("Gruppo non abilitato, contatta @Anatras02 se credi si tratti di un errore")
        raise StopPropagation
