class Translator:

    def __init__(self):
        self.dizionario = {}

    def printMenu(self):
        print("------------------------------")
        print("   Translator Alien-Italian   ")
        print("------------------------------")
        print("\n1. Aggiungi nuova parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Stampa tutto il dizionario\n"
              "5. Exit\n")


    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(dict, 'r', encoding='utf-8') as f:
            for riga in f:
                parole = riga.strip().split(" ")
                self.dizionario[parole[0]] = parole[1]

    def addDicLine(self, entry):
        campi = entry.split(" ")
        self.dizionario[campi[0]] = campi[1]





    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass