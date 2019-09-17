boodschappen =  {"brood": "1,50", "water": "1,00", "fruit": "2,50", "kaas": "1,00€", "melk": "1,00€" }
wagen = {}

def opslaan():
    f = open("dict.txt","w")
    f.write( str(wagen) )
    f.close()
    print("wagen opgeslagen")
    floep = input ('''
type terug om terug te gaan naar het menu
type kiezen om producten in je wagen te doen
type tonen om de producten te laten zien
type verwijder om producten te verwijderen


''')
    if floep == "kiezen":
        kies()
    if floep == "terug":
        menu()
    if floep == "tonen":
        tonen()
    if floep == "verwijder":
        verwijderen()
    else:
        print ("type kiezen tonen of verwijderen")
        floep = input ('''
type terug om terug te gaan naar het menu
type kiezen om producten in je wagen te doen
type tonen om de producten te laten zien
type verwijder om producten te verwijderen


''')
        







def kies():
    print ('''
type het product dat je in je mandje wilt doen
type terug om terug naar het menu te gaan
type verwijder om producten uit je wagen te verwijderen
type opslaan om je wagen op te slaan

''')

    print (''' brood: 1,50, water: 1,00, fruit: 2,50, kaas: 1,00, melk: 1,00
''')
    
    toevoegen = input ("")
    for key in boodschappen.keys():
        
        if toevoegen == key:
            print ('''product toegevoegd
''')
            wagen[toevoegen] = boodschappen[toevoegen] 
            

    if toevoegen == "opslaan":
        opslaan()
    if toevoegen == "terug":
        menu()
    if toevoegen == "verwijder":
        verwijderen()
    if toevoegen == "tonen":
        tonen()
    else:
        print ("kies opslaan, terug, verwijder of tonen")

    kies()
    




def tonen():
    for key in boodschappen.keys():
        print (key)
    kiezen = input ('''type kiezen om producten in je winkelwagen te doen
of kies terug om naar het menu te gaan
''')
    print(kiezen)
    if kiezen == "kiezen":
        
        kies()
        
    if kiezen == "terug":
        menu()
    if kiezen ==  "verwijder":
        verwijderen()
    if kiezen == "opslaan":
        opslaan()
        
    else:
        kiezen = input ('''
type terug om terug te gaan naar het menu
type kiezen om producten in je wagen te doen
type verwijder om producten te verwijderen
type opslaan om je mandje op te slaan
''')
        

def verwijderen():
    print (wagen)
    print ('''
type terug om terug te gaan naar het menu
type kiezen om producten in je wagen te doen
type tonen om de producten te laten zien
type opslaan om je mandje op te slaan

''')
    verwijderen = input("")
    if verwijderen in wagen.keys():
        del wagen[verwijderen]
    if verwijderen == "opslaan":
        opslaan()
    if verwijderen == "terug":
        menu()
    if verwijderen == "kiezen":
        kiezen()
    if verwijderen == "tonen":
        tonen()
    else:
        print ("kies opslaan, terug, kiezen of tonen")
        
        
    
        


    
    
    


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
        opslaan()
    else:
        print("kies tonen, kiezen, verwijder of opslaan")
    menu()
        
menu()
    

