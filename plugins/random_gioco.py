import random
from pyrogram import Client, filters

from config.variabili import chatScommesse


@Client.on_message(filters.command("random") & filters.chat(chatScommesse) | filters.regex(r"^Random ❓$"))
def gioco_random(_, message):
    giochi = [("Carte","/carte"), ("Tiro Con L'Arco","/tca"), ("Freccette","/freccette"), ("Rune","/rune"), ("Dado","/dado")]
    modalita = ["BO3", "Secca"]

    gioco_scelto = random.choice(giochi)

    if gioco_scelto[0] == "Tiro Con L'Arco":
        modalita_scelta = "Secca"
    else:
        modalita_scelta = random.choice(modalita)

    message.reply(
        f"@{message.from_user.username}, sei talmente indeciso da affidare a un computer la tua scelta, immetti i "
        f"dati e pochi secondi dopo esce il risultato: giocherai a **{gioco_scelto[0]} {modalita_scelta}**!\n**Comando:** {gioco_scelto[1]}"
    )
