import random

from pyrogram import Client, filters

from config.variabili import chatScommesse


@Client.on_message(filters.command(["sorte"]) | filters.regex(r"^Sorte 🐉$"))
def sorte(_, message):
    if message.chat.id not in chatScommesse:
        message.reply("Gruppo non abilitato, contatta @Anatras02 se credi si tratti di un errore")
        return

    valori_sorte = ["🐇", "🐓", "🐉"]
    valore_sorte = random.choice(valori_sorte)

    message.reply(
        f"@{message.from_user.username}, dopo la tua (non) meritata vincita decidi di sfidare il Fato, lui dall'alto "
        f"ti fa cadere in testa un animale di buon auspicio: {valore_sorte}!",
        quote=False
    )
