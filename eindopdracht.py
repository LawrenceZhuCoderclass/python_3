boodschappen =  {"brood": "1,50", "water": "1,00", "fruit": "2,50", "kaas": "1,00€", "melk": "1,00€" }
wagen = {}

def opslaan(bestandsnaam):
    f = open(bestandsnaam,"w")
    f.write( str(wagen) )
    f.close()
    print("wagen opgeslagen")
    menu()
        





a

def kies():
    print ('''
type het product dat je in je mandje wilt doen
type menu om naar het menu te gaan

''')

    print (''' brood: 1,50, water: 1,00, fruit: 2,50, kaas: 1,00, melk: 1,00
''')
    
    toevoegen = input ("")
    for key in boodschappen.keys():
        
        if toevoegen == key:
            print ('''product toegevoegd
''')
            wagen[toevoegen] = boodschappen[toevoegen] 
        
            kies()
        if toevoegen == "menu":
            menu()
        
    




def tonen():
    for key in boodschappen.keys():
        print (key)
 
    menu()
        

def verwijderen():
    print (wagen)
    print ('''

type het product dat je wilt verwijderen uit je wagen
type menu om terug naar het mneu te gaan

''')
    verwijder = input("")
    if verwijder in wagen.keys():
        del wagen[verwijder]

        verwijderen()
    if verwijder == "menu":
        menu()
        
    
        


    
    
    


def menu():
    menuvraag = input ('''
    type tonen om alle producten te zien
    type kiezen om producten in je winkelmandje te doen
    type verwijder om producten uit je winkelmandje te halen
    type opslaan om je lijst op te slaan
    
    
''')

    if menuvraag == "tonen":
        tonen()
    if menuvraag == "kiezen":
        kies()
    if menuvraag == "verwijder":
        verwijderen()
    if menuvraag == "opslaan":
        opslaan("dict.txt")
    else:
        print("kies tonen, kiezen, verwijder of opslaan")
    menu()
        
menu()
    

