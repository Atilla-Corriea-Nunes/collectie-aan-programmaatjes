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
endofthegame = False
hasNumberOrSpecialCardToPlay = False
viercounter = 0
keuzecounter = 0
nextplayerskips = 0

def showDevinfo ():
        print("the list of cards currently playable: "+ ", ".join(thelist))
        print("the pile in the middle of the table: "+ ", ".join(pile))
        print("your current hand: "+ ", ".join(playerhand))
        print("the enemy's current hand: " + ", ".join(aihand))

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
                elif immediatelyplay.lower() == "quit":
                    quit()
                elif immediatelyplay.lower() == "show":
                    showDevinfo()
                    continue
                else:
                    print("oeps, dat snapte ik niet. de correcte inputs zijn ja en nee")
                    continue

def aiDraws():
    pass

def aiTurn():
    global nextcard, endofthegame, aihand, aiSkips, nextplayerskips
    print("De hand van je vijand bestaat uit "+ str(len(aihand)) +" kaarten")
    if len(aihand) == 0:
        endofthegame = True
    if len(pile) != 1:
        if "+2" in pile[-1]:
            print("Je vijand moet 2 kaarten pakken door jou +2 kaart")
            for x in range(0,2):
                nextcard = completeddeck[0]
                del completeddeck[0]
                aihand.append(nextcard)
        elif nextplayerskips > 0:
            print("je vijand moest zijn beurt overslaan door jou sla-beurt-over/omkeer kaart")
            nextplayerskips = int(nextplayerskips) - 1
        elif "neem 4" in pile[-1]:
            print("Je vijand moet 4 kaarten pakken door jou neem 4 kaart")
            for x in range(0,4):
                nextcard = completeddeck[0]
                del completeddeck[0]
                aihand.append(nextcard)




def playerTurn():

    global nextcard, endofthegame
    if len(playerhand) == 0:
        endofthegame = True
    print("Het is jouw beurt, je kaarten zijn: "+ ", ".join(playerhand))
    if not pile:
        nextcard = completeddeck[0]
        del completeddeck[0]
        pile.append(nextcard)
    print("De kaart die boven aan de stapel ligt is "+ pile[-1])
    checkForAllColors()
    checkForAllNumbersAndSpecialCards()
    if canPlayBlue == True or canPlayGreen == True or canPlayYellow == True or canPlayRed == True or hasNumberOrSpecialCardToPlay == True or "Keuzekaart" in pile[-1] or "neem 4" in pile[-1] or "neem 4" in playerhand or "Keuzekaart" in playerhand and not thelist:
        print("Je hebt kaarten die je kan spelen!")

        print("De speelbare kaarten zijn "+ ", ".join(thelist) +". Geef de positie aan van de kaart die je wilt spelen (geteld van links)")
        while True:
            whattoplay = input("")
            if whattoplay.isnumeric() == True and int(whattoplay) > 0 and int(whattoplay) <= len(thelist):
                pile.append(thelist[int(whattoplay) - 1])
                for x in playerhand:
                    if thelist[int(whattoplay) - 1] ==  x:
                        playerhand.remove(x)
                        break
                print("De kaart die boven aan de stapel ligt is "+ pile[-1])
                if "Keuzekaart" in pile[-1]:
                    print("Je hebt zojuist een keuzekaart gespeeld, welke kleur wil je hebben?")
                    while True:
                        chooseColor = input("")
                        if "geel" in chooseColor or "groen" in chooseColor or "rood" in chooseColor or "blauw" in chooseColor:
                            pile.remove[-1]
                            pile.append("Keuzekaart "+ str(chooseColor))
                            print("De kaart die boven aan de stapel ligt is "+ pile[-1])
                break
            elif whattoplay.lower() == "quit":
                quit()
            elif whattoplay.lower() == "show":
                showDevinfo()
                continue
            else:
                print("Vul een geldig nummer van de positie die u heeft")
                continue
    print("Dat was het eidne van jouw beurt, het is nu de beurt van je vijand")
    print("")


def aiChecksForBlue():
    global canPlayBlue
    if "blauw" in pile[-1]:
        for x in aihand:
            if "blauw" in x:
                thelist.append(x)
        if thelist:
            canPlayBlue = True

def aiChecksForRed():
    global canPlayRed
    if "rood" in pile[-1]:
        for x in aihand:
            if 'blauw' in x:
                thelist.append(x)
        if thelist:
            canPlayRed = True

def aiChecksForGreen():
    global canPlayGreen
    if "groen" in pile[-1]:
        for x in aihand:
            if "groen" in x:
                thelist.append(x)
        if thelist:
            canPlayGreen = True

def aiChecksForYellow():
    global canPlayYellow
    if "yellow" in pile[-1]:
        for x in aihand:
            if "groen" in x:
                thelist.append(x)
        if thelist:
            canPlayYellow = True

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

def checkForAllNumbersAndSpecialCards():
    global playerhand, hasNumberOrSpecialCardToPlay, viercounter, keuzecounter
    for x in playerhand:
        if "sla-beurt-over" in x and "sla-beurt-over" in pile[-1] or "+2" in x and "+2" in pile[-1] or "omkeer" in x and "omkeer" in pile[-1] or "1" in x and "1" in pile[-1] or "2" in x and "2" in pile[-1] or "3" in x and "3" in pile[-1] or "4" in x and "4" in pile[-1] or "5" in x and "5" in pile[-1] or "6" in x and "6" in pile[-1] or "7" in x and "7" in pile[-1] or "8" in x and "8" in pile[-1] or "8" in x and "8" in pile[-1] or "9" in x and "9" in pile[-1] or "0" in x and "0" in pile[-1]:
            thelist.append(x)
            hasNumberOrSpecialCardToPlay = True

def aiChecksForAllColors():
    aiChecksForBlue()
    aiChecksForGreen()
    aiChecksForGreen()
    aiChecksForRed()
    
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
            elif choosecolor.lower() == "quit":
                quit()
            elif choosecolor.lower() == "show":
                showDevinfo()
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
                thelist.append("neem 4")
                break
            elif choosecolor.lower() == "quit":
                quit()
            elif choosecolor.lower() == "show":
                showDevinfo()
                continue
            else:
                print("oeps, dat snapte ik niet. de correcte inputs zijn rood, blauw, geel en groen ")
                continue
    elif canPlayBlue == False and canPlayRed == False and canPlayGreen == False and canPlayYellow == False and hasNumberOrSpecialCardToPlay == False:
        playerDraws()


completedeck = generateCards({"geel", "groen", "rood","blauw"}, ["0","1","2","3","4","5","6","7","8","9","+2","omkeer","sla-beurt-over"])
completedeck += generateCards({"geel", "groen", "rood","blauw"}, ["1","2","3","4","5","6","7","8","9","+2","omkeer","sla-beurt-over"])

playerhand = (completeddeck[0:7])
aihand = (completeddeck[7:14])
del completeddeck[:14]
while True:
    playerTurn()
    canPlayBlue = False
    canPlayGreen = False
    canPlayYellow = False
    canPlayRed = False
    playerSkips = False
    thelist = []
    hasNumberOrSpecialCardToPlay = False
    aiTurn()
    aiSkips = False
    if endofthegame == True:
        print("Dat is het einde van het spel!")
        quit()
        