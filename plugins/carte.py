import random

from pyrogram import Client, filters, StopPropagation

from config.variabili import chatScommesse
from funzioni import setta_scommessa


@Client.on_message(filters.command(["carte","carte@GestoreScommesseGiochiBot"]) | filters.private | filters.regex(r"^Carte π$"))
def carte(_, message):
    if message.chat.id not in chatScommesse:
        message.reply("Gruppo non abilitato, contatta @Anatras02 se credi si tratti di un errore")
        return

    numero = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    seme = ["β£οΈ", "β οΈ", "β¦οΈ", "β₯οΈ"]
    flag = True

    while flag:
        numero1 = random.choice(numero)
        numero2 = random.choice(numero)
        seme1 = random.choice(seme)
        seme2 = random.choice(seme)

        if random.randint(1, 100) <= 2:
            if random.randint(1, 2) == 1:
                carta1 = "Jolly π"
                carta2 = f"{numero2} {seme2}"
            else:
                carta1 = f"{numero1} {seme1}"
                carta2 = "Jolly π"
        else:
            carta1 = f"{numero1} {seme1}"
            carta2 = f"{numero2} {seme2}"

        if carta1 != carta2:
            flag = False

    message.reply(
        f"{message.from_user.username}, mischi per bene il mazzo, improvvisamente sfili dall'alto le prime due carte, "
        f"sono: {carta1} e {carta2}!")
    setta_scommessa(message.from_user, f"Carte", f"{carta1} {carta2}")


@Client.on_message(filters.command("scarte"))
def regolamento_carte(_, message):
    message.reply(
        "πβπ¨ <b>Carte</b> π: <i>Gioco semplice, simile al dado, ma con le carte</i>.\n\nDopo aver <u>eseguito il "
        "comando</u> <b>vengono estratte 2 carte a caso dal mazzo di 52</b>. Tra le due <b>si individua la "
        "migliore</b>, che va <b>contro la migliore dell'avversario</b>.\nChi ha <b>la carta piΓΉ di valore tra le due "
        "vince</b>.\n<i>La scala dei numeri Γ¨ come quella del Poker</i>: A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, "
        "2.\n(In ordine decrescente)\n\n<i>Il valore delle carte non Γ¨ dato solo dal numero, ma anche dal "
        "seme</i>:\nβ₯οΈ>β¦οΈ;\nβ¦οΈ>β£οΈ;\nβ£οΈ>β οΈ;\ndi conseguenza β₯οΈ <b>Γ¨ il seme migliore</b> e β οΈ <b>Γ¨ il seme "
        "peggiore</b>.\n\n<b>Per esempio</b>:\nGiocatore 1 ha 3β₯οΈ e 2β£οΈ; Giocatore 2 ha 2β₯οΈ e 3β¦οΈ\nVince il <b>3β₯οΈ "
        "del Giocatore 1</b> <i>(essendo cuori piΓΉ grande di fiori e quadri, gli altri due semi non vengono "
        "considerati)</i>.\n<b>Oppure:</b> se Giocatore 1 ha 2β₯οΈ e 2β£οΈ, mentre Giocatore 2 ha 2β¦οΈ e 2β₯οΈ, <b>vince il "
        "Giocatore 2</b> siccome <b>quadri Γ¨ piΓΉ grande di fiori</b> <i>(in questo caso i cuori non si considerano, "
        "pur essendo i piΓΉ grandi, perchΓ© in pareggio)</i>.\n\nC'Γ¨ inoltre una <b>bassa probabilitΓ </b> che capiti un "
        "<b>\"π Jolly!\"</b>, nel caso <b>si vince al 100%</b> <i>(a meno che non esca anche "
        "all'avversario)</i>.\nSe non specificato <b>BO3</b>"
    )
