import random

from pyrogram import Client, filters

from config.variabili import chatScommesse
from funzioni import setta_scommessa


@Client.on_message(filters.command(["rune","rune@GestoreScommesseGiochiBot"]) | filters.regex(r"^Rune ๐ฎ$"))
def rune(app, message):
    if message.chat.id not in chatScommesse:
        message.reply("Gruppo non abilitato, contatta @Anatras02 se credi si tratti di un errore")
        return

    simboli = ["๐ฑ", "๐ฅ", "๐ง", "๐"]

    simbolo = random.choice(simboli)

    message.reply(
        f"@{message.from_user.username}, invochi il grande mago di Aci Trezza che controvoglia ti fa la rivelazione: "
        f"la tua runa รจ {simbolo}!"
    )
    setta_scommessa(message.from_user, "Rune", simbolo)


@Client.on_message(filters.command("srune"))
def regolamento_rune(app, message):
    message.reply("""
            ๐โ๐จ <b>4 Rune</b> ๐ฎ: <i>Gioco simile alle carte, ma con meno possibilitร </i>.\n๐ โ <b>perde contro "
            "tutto</b>\n๐ฅ โ <b>batte</b> ๐ฑ\n๐ง โ <b>batte</b> ๐ฅ\n๐ฑ โ <b>batte</b> ๐ง\nSe non specificato <b>BO3 e "
            "sorte</b>
        """)
