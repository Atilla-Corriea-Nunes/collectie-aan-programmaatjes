import random
namenlijst = []
completedlist = []
currentpos = 0
x = 0
alreadyused = ""

def addToNamelist():
        if currentitem in namenlijst:
            print('Die naam staat al in de lijst')  
        else: 
            namenlijst.append(currentitem)
            return namenlijst


while True:
    currentitem = input("Welke naam wilt u toevoegen? ")
    if currentitem.lower() == "quit":
        quit()
    addToNamelist()    

    while True:
        leave = input("Wilt u nog een naam toevoegen? (Y/N) ")
        if (leave.lower() == "y" or leave.lower() == "n"):
            break
        else:
            print("ik snapte dat niet, kies tussen y en n")
            continue



    if leave.lower() == "n":
        for y in namenlijst:    
            currentperson = namenlijst[currentpos]
            while True:
                currentlink = random.choice(namenlijst)
                both = str(currentperson) + " heeft " +currentlink+ " als lootje gekregen!"
                string=''.join([str(item) for item in completedlist])
                if x == 0 and currentperson != currentlink:
                    alreadyused = str(alreadyused) + " " + currentlink
                    break
                if x == 0:
                    continue
                elif currentperson == currentlink or currentlink in alreadyused:
                    continue
                else:
                    alreadyused = str(alreadyused) + " " + currentlink
                    break
                
            completedlist.append(both)
            currentpos = int(currentpos) + 1
            x = int(x) + 1
        print(completedlist)
        quit()
