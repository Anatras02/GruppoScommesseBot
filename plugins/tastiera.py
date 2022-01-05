from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

from config.variabili import chatScommesse


@Client.on_message(filters.command(["tastiera"]))
def tastiera(app, message):
    if message.chat.id not in chatScommesse:
        message.reply("Gruppo non abilitato, contatta @Anatras02 se credi si tratti di un errore")
        return

    app.send_message(
        message.chat.id,  # Edit this
        "Ecco la tastiera con i giochi!",
        reply_markup=ReplyKeyboardMarkup(
            [
                ["Carte 🃏", "Tiro Con L'Arco 🏹"],
                ["Testa o Croce 🌕", "Dado 🎲"],
                ["Rune 🔮", "Freccette 🎯"],
                ["Petardi (Beta) 💣"],
                ["Random ❓"],
                ["Sorte 🐉", "/gruzzolo 💸"],
                ["Statistiche 📊", "Chiudi ❌"]
            ],
            resize_keyboard=True  # Make the keyboard smaller
        )
    )


@Client.on_message(filters.command(["chiudi"]) | filters.regex(r"^Chiudi ❌$"))
def chiudi(_, message):
    message.reply("Okay, ho chiuso la tastiera!", reply_markup=ReplyKeyboardRemove())
