import random
namenlijst = []
completedlist = []
currentpos = 0

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
                if currentlink in currentperson and str("heeft " + currentlink) in completedlist:
                    continue
                else:
                    break
            both = str(currentperson) + " heeft " +currentlink+ " als lootje gekregen!"
            completedlist.append(both)
            currentpos = int(currentpos) + 1
        print(completedlist)
        quit()
