import random

def blueCalculator(currentblueroll):
    pass

def redCalculator(currentredroll):
    pass

def bothCalculator(currentredroll, currentblueroll):
    pass


counter = 1
red = [-2, "▯", "▯", "▯", "▯", "▯", "▯", "▯", "▯", "▯"]
blue = ["▯", "▯", "▯", "▯", "▯", "▯", "▯", "▯", "▯", -2]
white = ["▯", "▯", "▯", "▯", "▯"]
reddice = [1, 2, 3, 4, 5, 6]
bluedice = [1, 2, 3, 4, 5, 6]
whitedice = [1,1,1,2,2,3]
print("Hallo en welkom bij Dobbel-Trobbel, ik hoop dat je de regels van dit spel kent want ik snap ze alleen maar half dus ik zou het niet kunnen uitleggen.")
while True:
    print("Dit is ronde "+ str(counter))
    print("")
    counter = int(counter) + 1
    redroll = random.choice(reddice)
    blueroll = random.choice(bluedice)
    whiteroll = random.choice(whitedice)

    redcurrentrecent = 1
    bluecurrentrecent = -1
    redrecent = red[redcurrentrecent]
    bluerecent = blue[bluecurrentrecent]

    print(str(bluerecent))
    print(str(redrecent))
    print("Je hebt "+ str(redroll) +" gerolt met je rode dobbelsteen")
    print("Je hebt "+ str(blueroll) +" gerolt met je blauwe dobbelsteen")
    print("Je hebt "+ str(whiteroll) +" gerolt met je witte dobbelsteen")
    print("")
    c1 = int(blueroll) + int(redroll) + int(whiteroll)
    c2 = int(blueroll) + int(redroll) - int(whiteroll)
    c3 = int(blueroll) + int(redroll)
    if (whiteroll > redroll and whiteroll > blueroll):
        c4 = whiteroll
    elif (redroll > whiteroll and redroll > blueroll):
        c4 = redroll
    elif (blueroll > redroll and blueroll > whiteroll):
        c4 = blueroll

    if (blueroll < redroll):
        placewhere = "de blauwe"
    elif (blueroll > redroll):
        placewhere = "de rode"
    else:
        placewhere = ("een van de")

    print("kies welk cijfer je wilt zetten in "+ str(placewhere) +" kolom(men) of typ 'leeg' als je niks in wilt vullen")
    print("Keuze een: "+ str(c1))
    print("Keuze twee: "+ str(c2))
    print("Keuze drie: "+ str(c3))
    print("Keuze vier: "+ str(c4))
    keuzes = [c1, c2, c3, c4]
    print (keuzes)
    bluerollsave = -2
    redrollsave = -2
    while True:
        welkekeuze = input("")

        if (blueroll < redroll and welkekeuze in keuzes and welkekeuze > bluerollsave):
            blueCalculator(blueroll)
        elif (blueroll > redroll and welkekeuze in keuzes and welkekeuze > redrollsave):
            redCalculator(redroll)
        elif (blueroll == redroll and welkekeuze in keuzes and welkekeuze > redrollsave or welkekeuze > bluerollsave):
            bothCalculator(redroll, blueroll)
        elif (welkekeuze.lower() == "leeg"):
            pass
        else:
            print("oeps, er is een fout voorgekomen. check even of het cijfer wel in de lijst past en dat het cijfer een van de keuzes is die je mag maaken")
            continue
    quit()

