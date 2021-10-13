import random
counter = 0
global completeddeck
completeddeck = []
playerhand = []
aihand = []
pile = []
thelist = []
canPlayYellow = False
canPlayRed = False
canPlayGreen = False
canPlayBlue = False
colors = ["blauw","rood","groen","geel"]
def generateCards(deck, cardtypes):
    for currentcard in deck:
        for currenttype in cardtypes:
            completeddeck.append(currentcard + " " + currenttype)
    for x in range(0,2):
        completeddeck.append("Keuzekaart")
        completeddeck.append("neem 4")
    random.shuffle(completeddeck)
    return [completeddeck]

def playerDraws():
    global nextcard
    nextcard = completeddeck[0]
    del completeddeck[0]
    print("Je hebt geen kaarten om te spelen dus je pakt eentje van de stapel")
    for x in colors:
        if x in nextcard and x not in pile[-1]:
            print("De kaart die je hebt gepakt van de stapel is "+ str(nextcard) +", die kan je niet spelen")
            playerhand.append(nextcard)
            nextcard = ""
    for x in colors:
        if x in nextcard and x in pile[-1]:
            while True:
                immediatelyplay = input("De kaart die je hebt gepakt van de stapel is "+ str(nextcard) +", je kan die kaart meteen spelen, wil je dat doen? ")
                if immediatelyplay.lower() == "ja":
                    pile.append(nextcard)
                    nextcard = ""
                    print("De kaart die boven aan de stapel ligt is "+ pile[-1])
                    break
                elif immediatelyplay.lower() == "nee":
                    playerhand.append(nextcard)
                    nextcard = ""
                    print("De kaart die boven aan de stapel ligt is "+ pile[-1])
                    break
                else:
                    print("oeps, dat snapte ik niet. de correcte inputs zijn ja en nee")
                    continue

def aiDraws():
    pass

def aiTurn():
    pass

def playerTurn():
    global nextcard
    print("Het is jouw beurt, je kaarten zijn: "+ ", ".join(playerhand))
    nextcard = completeddeck[0]
    del completeddeck[0]
    pile.append(nextcard)
    print("De kaart die boven aan de stapel ligt is "+ pile[-1])
    checkForAllColors()
    if canPlayBlue == True or canPlayGreen == True or canPlayYellow == True or canPlayRed == True or "Keuzekaart" in pile[-1] or "neem 4" in pile[-1]:
        print("Je hebt kaarten die je kan spelen!")
        print("De speelbare kaarten zijn "+ ", ".join(thelist) +". Geef de positie aan van de kaart die je wilt spelen (geteld van links)")
        while True:
            whattoplay = input("")
            if whattoplay.isnumeric() == True and int(whattoplay) > 0 and int(whattoplay) <= len(thelist):
                pile.append(thelist[int(whattoplay) - 1])
                print("De kaart die boven aan de stapel ligt is "+ pile[-1])
                break
            else:
                print("Vul een geldig nummer van de positie die u heeft")
                continue





def checkForBlue():
    global canPlayBlue
    if "blauw" in pile[-1]:
        for x in playerhand:
            if  "blauw" in x:
                thelist.append(x)   
        if thelist:
            canPlayBlue = True
    
def checkForRed():
    global canPlayRed
    if "rood" in pile[-1]:
        for x in playerhand:
            if  "rood" in x:
                thelist.append(x)   
        if thelist:
            canPlayRed = True

def checkForYellow():
    global canPlayYellow
    if "geel" in pile[-1]:
        for x in playerhand:
            if  "geel" in x:
                thelist.append(x)   
        if thelist:
            canPlayYellow = True

def checkForGreen():
    global canPlayGreen
    if "groen" in pile[-1]:
        for x in playerhand:
            if  "groen" in x:
                thelist.append(x)   
        if thelist:
            canPlayGreen = True
    
def checkForAllColors():
    checkForBlue()
    checkForGreen()
    checkForRed()
    checkForYellow()
    if "Keuzekaart" in pile[-1] :
        print("De kaart op het begin van de stapel is een keuzekaart dus jij mag de kleur bepalen")
        while True:
            choosecolor = input("Welke kleur wil je hebben? ")
            if choosecolor.lower() in colors:
                pile.append(choosecolor)
                thelist.append("Keuzekaart")
                break
            else:
                print("oeps, dat snapte ik niet. de correcte inputs zijn rood, blauw, geel en groen ")
                continue
        print(pile[-1])        
    elif "neem 4" in pile[-1]:
        print("De kaart op het begin van de stapel is een neem 4 dus jij mag de kleur bepalen")
        while True:
            choosecolor = input("Welke kleur wil je hebben? ")
            if choosecolor.lower() in colors:
                pile.append(choosecolor)
                thelist.append("neem vier")
                break
            else:
                print("oeps, dat snapte ik niet. de correcte inputs zijn rood, blauw, geel en groen ")
                continue
    elif canPlayBlue == False and canPlayRed == False and canPlayGreen == False and canPlayYellow == False:
        playerDraws()


completedeck = generateCards({"geel", "groen", "rood","blauw"}, ["0","1","2","3","4","5","6","7","8","9","+2","omkeer","sla-beurt-over"])
completedeck += generateCards({"geel", "groen", "rood","blauw"}, ["1","2","3","4","5","6","7","8","9","+2","omkeer","sla-beurt-over"])

playerhand = (completeddeck[0:7])
aihand = (completeddeck[7:14])
del completeddeck[:14]
playerTurn()
aiTurn()