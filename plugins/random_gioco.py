import random

from pyrogram import Client, filters

from config.variabili import chatScommesse


@Client.on_message(filters.command("random") | filters.regex(r"^Random ❓$"))
def gioco_random(_, message):
    if message.chat.id not in chatScommesse:
        message.reply("Gruppo non abilitato, contatta @Anatras02 se credi si tratti di un errore")
        return

    giochi = [("Carte", "/carte"), ("Tiro Con L'Arco", "/tca"), ("Freccette", "/freccette"), ("Rune", "/rune"),
              ("Dado", "/dado"), ("Petardi", "/petardi")]
    modalita = ["BO3", "Secca"]

    gioco_scelto = random.choice(giochi)

    if gioco_scelto[0] in ["Tiro Con L'Arco", "Petardi"]:
        modalita_scelta = "Secca"
    else:
        modalita_scelta = random.choice(modalita)

    message.reply(
        f"@{message.from_user.username}, sei talmente indeciso da affidare a un computer la tua scelta, immetti i "
        f"dati e pochi secondi dopo esce il risultato: giocherai a **{gioco_scelto[0]} {modalita_scelta}**!\n**Comando:** {gioco_scelto[1]}"
    )
