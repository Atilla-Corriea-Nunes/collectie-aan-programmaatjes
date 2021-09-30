import random
counter = 1
def generateCards(deck, cardtypes):
    completeddeck = []
    for currentcard in deck:
        for currenttype in cardtypes:
            completeddeck.append(currentcard + " " + currenttype)
    completeddeck.append("Joker")
    completeddeck.append("Joker")
    random.shuffle(completeddeck)
    return [completeddeck[7:], completeddeck[:7]]
h = generateCards({"schoppen", "harten", "klaveren","ruiten"}, ["2","3","4","5","6","7","8","9","10","A","B","Q","K"])
for x in h[1]:
    print("Kaart "+ str(counter) + ": "+ str(x))
    counter = int(counter) + 1
print(h[0])