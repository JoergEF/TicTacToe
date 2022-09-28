# Tic Tac Toe - Ein Konsolen-Spiel
print("Tic Tac Toe, (c) 2022 Jörg Hofmann")
spiel_aktiv = True
spieler_aktuell = " X "
# Spielfeld aufbauen
spielfeld = [" ",
             " 1 ", " 2 ", " 3 ",
             " 4 ", " 5 ", " 6 ",
             " 7 ", " 8 ", " 9 "]

def spielfeld_ausgeben():
    print()
    print(spielfeld[1] + "|" + spielfeld[2] + "|" + spielfeld[3])
    print("---+---+---")
    print(spielfeld[4] + "|" + spielfeld[5] + "|" + spielfeld[6])
    print("---+---+---")
    print(spielfeld[7] + "|" + spielfeld[8] + "|" + spielfeld[9])
    print()

# Eingabe Spielzug
def spielzug_eingabe():
    global spiel_aktiv
    global spieler_aktuell
    while True:
        spielzug = input("<" + spieler_aktuell + "> Bitte Feldnummer oder q eingeben: ")
        if spielzug == 'q':
            spiel_aktiv = False
            return
        try:
            spielzug = int(spielzug)

        except ValueError:
            print("Bitte eine Ziffer zwischen 1 und 9 eingeben")
        else:
            if spielzug >= 1 and spielzug  <= 9:
                if spielfeld[spielzug] == " X " or spielfeld[spielzug] == " O ":
                    print("Feld bereits vergeben, neu wählen")
                else:
                    return spielzug
            else:
                print("Die Ziffer MUSS zwischen 1 und 9 liegen.")
def spieler_wechseln():
    global spieler_aktuell
    if spieler_aktuell == " X ":
        spieler_aktuell = " O "
    else:
        spieler_aktuell = " X "

def kontrolle_gewonnen():
    if spielfeld[1] == spielfeld[2] == spielfeld[3]:
        return spielfeld[1]
    if spielfeld[4] == spielfeld[5] == spielfeld[6]:
        return spielfeld[4]
    if spielfeld[7] == spielfeld[8] == spielfeld[9]:
        return spielfeld[7]
    if spielfeld[1] == spielfeld[4] == spielfeld[7]:
        return spielfeld[1]
    if spielfeld[2] == spielfeld[5] == spielfeld[8]:
        return spielfeld[2]
    if spielfeld[3] == spielfeld[6] == spielfeld[9]:
        return spielfeld[3]
    if spielfeld[1] == spielfeld[5] == spielfeld[9]:
        return spielfeld[1]
    if spielfeld[3] == spielfeld[5] == spielfeld[7]:
        return spielfeld[3]

def kontrolle_unentschieden():
    if (spielfeld[1] == " X " or spielfeld[1] == " O ") \
       and (spielfeld[2] == " X " or spielfeld[2] == " O ") \
       and (spielfeld[3] == " X " or spielfeld[3] == " O ") \
       and (spielfeld[4] == " X " or spielfeld[4] == " O ") \
       and (spielfeld[5] == " X " or spielfeld[5] == " O ") \
       and (spielfeld[6] == " X " or spielfeld[6] == " O ") \
       and (spielfeld[7] == " X " or spielfeld[7] == " O ") \
       and (spielfeld[8] == " X " or spielfeld[8] == " O ") \
       and (spielfeld[9] == " X " or spielfeld[9] == " O "):
        return ("unentschieden")

# main
while spiel_aktiv:
    spielfeld_ausgeben()
    spielzug = spielzug_eingabe()
    if spielzug:
        spielfeld[spielzug] = spieler_aktuell
        spielfeld_ausgeben()
        gewonnen = kontrolle_gewonnen()
        if gewonnen:
            print("Spieler" + gewonnen + "hat gewonnen.")
            spiel_aktiv = False
            break
        unentschieden = kontrolle_unentschieden()
        if unentschieden:
            print("Keiner hat gewonnen.")
            spiel_aktiv = False
            break
        spieler_wechseln()
print()
print("Auf Wiedersehen!")
print()