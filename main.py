import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        parola = input()
        t.addDicLine(parola.lower())
        print("Parola aggiunta correctamente")
    if int(txtIn) == 2:
        print("Ok, quale parola devo tradurre?")
        parolaAliena = input()
        traduzione = t.dizionario.get(parolaAliena.lower())
        print(traduzione)
        break
    if int(txtIn) == 3:
        break
    if int(txtIn) == 4:
        print("Ok, stampo tutto il dizionario")
        for chiave, valore in t.dizionario.items():
            print(f"{chiave}: {valore}")
        break
    if int(txtIn) == 5:
        print("Exit")
        break