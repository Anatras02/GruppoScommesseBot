import time

from pykeyboard import InlineKeyboard
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton

from config.variabili import chatScommesse, tiratori_petardi
from funzioni import *
from funzioni import giocatore_random


@Client.on_message(
    filters.command(["petardi", "petardi@GestoreScommesseGiochiBot", "botti", "napoletardi", "napolimerda"]) |
    filters.regex(r"^Petardi 💣$")
)
def petardi(_, message):
    if message.chat.id not in chatScommesse:
        message.reply("Gruppo non abilitato, contatta @Anatras02 se credi si tratti di un errore")
        return

    utente = str(message.from_user.id)
    codice = codice_func()

    keyboard = InlineKeyboard(row_width=1)
    keyboard.add(
        InlineKeyboardButton("Lancia 💣", callback_data=f"lancia|{utente}|{codice}"),
        InlineKeyboardButton("Cancella ❌", callback_data=f"cancella|{utente}|{codice}")
    )

    tiratori_petardi[f"{utente}{codice}"] = dict()
    tiratori_petardi[f"{utente}{codice}"]["terminato"] = False
    tiratori_petardi[f"{utente}{codice}"]["risultati"] = []

    message.reply(
        f"{message.from_user.first_name} sei abbastanza na🅱️oletano da rischiare le dita per un po' di divertimento?",
        reply_markup=keyboard,
        quote=False
    )


@Client.on_message(filters.command("spetardi"))
def regolamento_petardi(_, message):
    message.reply(
        '**Petardi 🧨**\n'
        'Le regole sono semplici.\n\n'
        'Si tira a turni.\n(Esempio: hai fatto un tiro,ora aspetti che il compagno faccia anche lui il tiro, e cosi via.)\n\n💣'
        'Si può fare fino a quanti tiri si vuole.\n'
        'Pero c’è il rischio che il petardo scoppi, se il petardo scoppia non si ottiene nessun punto 💣\n\n'
        '❌ Potete fermarvi quando volete per non rischiare che il petardo vi scoppi in mano ❌\n\n'
        '🧨 Vince chi fa più punti o a chi esplode il petardo 🧨\n'
        '⛔️ Se il primo giocatore ad aver tirato perde (e l\'altro è ancora in gioco) l\'altro deve per forza tirare, '
        'se non perde ha vinto altrimenti si andranno a comparare i punteggi ottenuti fino a quel turno\n'
        'Nel caso il secondo giocatore non effettuasse il tiro è come se il petardo fosse esploso e quindi si va in pareggio ⛔\n\n'
        'NB: Rivelate i punti a vinceda dopo che entrambi hanno finito per non avvantaggiare l\'altro concorrente")\n\n'
        'Di default il gioco è modalità SECCA'
    )


@Client.on_callback_query(filters.regex("lancia"))
def lancia_query(app, callback_query):
    frasi_effetto_successo = [
        "Hai lanciato un petardo all'ultimo, non sei morto ma hai fatto saltare **{punti}** dita a {giocatore}",
        "Hai lanciato il petardo ma non è scoppiato, nel dubbio scommetti con dod1c1 il frosciu e vinci "
        "**{punti}**kkk ",
        "Lanci un petardo in un cimitero a Napoli, TwisterHDD e il sindaco ti incominciano ad inseguire.\nPerdi "
        "**{punti}** anni di vita ",
        "Lanci un petardo in taverna, Edo ti muta per **{punti}** giorni",
        "Dopo aver tirato un petardo Edo spaventato esce da dietro un albero avvolto in un impermeabile grigio, "
        "lo apre di scatto e ti mostra il pene, esclami: \"Che bel pisello da **{punti}**cm\"",
        "Lanci un petardo al grido di \"DRICER SEI UN TESTA DI CAZZO\", Dricer arriva e ti rompe **{punti}** "
        "costole",
        "Lanci un petardo ma quest’ultimo non scoppia, dod1c1 deluso ti dissa **{punti}** volte in un freestyle"
    ]

    frasi_effetto_perdita = [
        "Ti scoppia un petardo in mano, perdi tutte le dita della mano!\nSei costretto a scappare in pronto "
        "soccorso",
    ]

    codice = callback_query.data.split("|")[2]
    utente = int(callback_query.data.split("|")[1])
    tag_utente = f"{utente}{codice}"
    try:
        tiratori_petardi[tag_utente]
    except KeyError:
        callback_query.answer("Il bot è stato riavviato mentre giocavi, rilancia il comando /petardi")
        return

    if callback_query.from_user.id != utente:
        callback_query.answer("Eh, volevi!")
        return

    keyboard = InlineKeyboard(row_width=1)
    keyboard.add(
        InlineKeyboardButton("Lancia 💣", callback_data=f"lancia|{utente}|{codice}"),
        InlineKeyboardButton("Termina ❌", callback_data=f"termina|{utente}|{codice}")
    )

    numero_lanci = len(tiratori_petardi[tag_utente]["risultati"])
    if numero_lanci == 1:
        probabilità = 5
    elif numero_lanci == 2:
        probabilità = 7
    elif numero_lanci == 3:
        if random.randint(1, 100) < 20:
            probabilità = 30
        else:
            probabilità = 10
    elif numero_lanci == 4:
        probabilità = 15
    elif numero_lanci == 5:
        probabilità = random.randint(15, 25)
    elif numero_lanci == 6:
        probabilità = random.randint(20, 35)
    elif 6 < numero_lanci <= 10:
        probabilità = random.randint(30, 40)
    elif 10 < numero_lanci < 20:
        probabilità = random.randint(35, 60)
    else:
        probabilità = random.randint(75, 100)

    if not tiratori_petardi[tag_utente]["terminato"] and \
            (not tiratori_petardi[tag_utente]["risultati"] or random.randint(1, 100) >= probabilità):
        numero = random.randint(1, 25)

        giocatore_random_var = giocatore_random(utente, callback_query.message.chat.id, app)
        frase = random.choice(frasi_effetto_successo).format(punti="__[REDACTED]__", giocatore=giocatore_random_var)

        tiratori_petardi[tag_utente]["risultati"].append(numero)

        counter = 1
        tiri = f"{frase}\n\n"
        for _ in tiratori_petardi[tag_utente]["risultati"]:
            tiri += f"**Punteggio {counter}:** [__REDACTED__]\n"
            counter += 1

        try:
            callback_query.edit_message_text(
                tiri,
                reply_markup=keyboard
            )

            time.sleep(0.1)
        except FloodWait:
            callback_query.answer("Sì ma stai calmo dio cane")

    else:
        keyboard = InlineKeyboard(row_width=1)
        keyboard.add(
            InlineKeyboardButton("Mostra Punteggi ✌️", callback_data=f"punteggio|{utente}|{codice}|F"),
        )

        tiratori_petardi[tag_utente]["terminato"] = True

        frase = random.choice(frasi_effetto_perdita)
        frase += f"\n\nIl petardo ti è esploso al turno numero **{numero_lanci + 1}**"
        callback_query.edit_message_text(
            frase,
            reply_markup=keyboard
        )


@Client.on_callback_query(filters.regex("termina"))
def termina_query(app, callback_query):
    codice = callback_query.data.split("|")[2]
    utente = int(callback_query.data.split("|")[1])
    tag_utente = f"{utente}{codice}"

    if callback_query.from_user.id != int(utente):
        callback_query.answer("Non si può più, F!")
        return

    keyboard = InlineKeyboard(row_width=1)
    keyboard.add(
        InlineKeyboardButton("Mostra Punteggi ✌️", callback_data=f"punteggio|{utente}|{codice}|V"),
    )

    numero_lanci = len(tiratori_petardi[tag_utente]["risultati"])
    callback_query.edit_message_text(
        f"Hai deciso di smettere di lanciare petardi al turno {numero_lanci}!\nPremi il tasto sottostante per vedere quanti punti hai fatto",
        reply_markup=keyboard
    )


@Client.on_callback_query(filters.regex("punteggio"))
def punteggio_query(app, callback_query):
    codice = callback_query.data.split("|")[2]
    utente = int(callback_query.data.split("|")[1])
    finito_male = callback_query.data.split("|")[3]
    tag_utente = f"{utente}{codice}"

    try:
        tiratori_petardi[tag_utente]
    except KeyError:
        callback_query.answer("Il bot è stato riavviato mentre giocavi, rilancia il comando /petardi")
        return

    if callback_query.from_user.id != utente:
        callback_query.answer("Eh, volevi!")
        return

    counter = 1
    totale = 0

    tiri = f"Ecco il risultato del tuo divertimento malato {callback_query.from_user.username} 💣\n"
    if finito_male == "F":
        numero_lanci = len(tiratori_petardi[tag_utente]["risultati"])
        tiri += f"__(Anche se il petardo ti è **ESPLOSO** al **turno {numero_lanci + 1}** ti vogliamo bene comunque)__\n\n"

    for punteggio in tiratori_petardi[tag_utente]["risultati"]:
        tiri += f"**Punteggio {counter}:** {punteggio}\n"
        counter += 1
        totale += punteggio

    tiri += f"\n**Totale**: {totale}"

    try:
        callback_query.edit_message_text(tiri)
    except FloodWait:
        callback_query.answer("Sì ma stai calmo dio cane")


@Client.on_callback_query(filters.regex("cancella"))
def cancella_query(app, callback_query):
    utente = callback_query.data.split("|")[1]

    if callback_query.from_user.id != int(utente):
        callback_query.answer("Non si può più, F!")
        return

    callback_query.edit_message_text("Non sei un Na🅱️oletano vero, vergogna!")
