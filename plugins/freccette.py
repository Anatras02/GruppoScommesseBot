from pyrogram import Client, filters

from config.variabili import chatScommesse
from funzioni import setta_scommessa


@Client.on_message(filters.command(["freccette","freccette@GestoreScommesseGiochiBot"]) & filters.chat(chatScommesse) | filters.regex(r"^Freccette π―$"))
def freccette(app, message):
    if message.chat.id not in chatScommesse:
        message.reply("Gruppo non abilitato, contatta @Anatras02 se credi si tratti di un errore")
        return

    risultato = app.send_dice(message.chat.id, "π―", reply_to_message_id=message.message_id)
    setta_scommessa(message.from_user, f"Freccette", risultato.dice.value)


@Client.on_message(filters.command("sfreccette"))
def regolamento_freccette(_, message):
    message.reply(
        "πβπ¨ <b>Freccette</b> π―: <i>minigioco implementato da Telegram</i>.\nI giocatori <i>a turno tirano la "
        "freccetta</i>. <b>Chi si avvicina di piΓΉ al centro vince il turno</b>.\nSe non specificato <b>BO3</b>"
    )
