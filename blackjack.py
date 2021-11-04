import random
completeddeck = []
dealerhand = []
playerhand = []
dealersvalue = 0
playersvalue = 0
hitorstay = ""
haschosentostay = False
dealerhaschosentostay = False
playerusedace = False
dealerusedace = False
x = 0
y = 0
z = 0



def generateCards(deck, cardtypes):
    global completedeck
    for currentcard in deck:
        for currenttype in cardtypes:
            completeddeck.append(currentcard + " " + currenttype)
    random.shuffle(completeddeck)

def showDevInfo():
    print("your hands current value is: "+ str(playersvalue))
    print("the dealers current value is: "+ str(dealersvalue))
    print("your current hand has the following cards: "+ ", ".join(playerhand))
    print("the dealers current hand has the following cards: "+ ", ".join(dealerhand))

def addCardsToHand(hand):
    for x in range (0,2):
        hand.append(completeddeck[0])
        del completeddeck[0]

def findhandValue(value, hand):
    for x in hand:
        if "king" in x or "queen" in x or "jack" in x or "10" in x:
            value = int(value) + 10
        elif "1" in x:
            value = int(value) + 1
        elif "2" in x:
            value = int(value) + 2
        elif "3" in x:
            value = int(value) + 3
        elif "3" in x:
            value = int(value) + 3
        elif "4" in x:
            value = int(value) + 4
        elif "5" in x:
            value = int(value) + 5
        elif "6" in x:
            value = int(value) + 6
        elif "7" in x:
            value = int(value) + 7
        elif "8" in x:
            value = int(value) + 8
        elif "9" in x:
            value = int(value) + 9
        elif "ace" in x:
            value = int(value) + 11
    return value

def addExtraCard(value, hand):
    if "king" in hand or "queen" in hand or "jack" in hand or "10" in hand:
        value = int(value) + 10
    elif "1" in hand:
        value = int(value) + 1
    elif "2" in hand:
        value = int(value) + 2
    elif "3" in hand:
        value = int(value) + 3
    elif "3" in hand:
        value = int(value) + 3
    elif "4" in hand:
        value = int(value) + 4
    elif "5" in hand:
        value = int(value) + 5
    elif "6" in hand:
        value = int(value) + 6
    elif "7" in hand:
        value = int(value) + 7
    elif "8" in hand:
        value = int(value) + 8
    elif "9" in hand:
        value = int(value) + 9
    elif "ace" in hand:
        value = int(value) + 11
    return value

def checkIfYouHaveAnAce(hand, value):
    global y
    for x in hand:
        if "ace" in x and value > 21:
            y = int(y) + 1
    for x in range (0,y):
        value = int(value) - 10
    return value

def whoWon():
    global playersvalue, playerhand, dealersvalue, dealerhand
    if dealersvalue > playersvalue:
        print("The dealer is closer to 21 than you! you lose...")
        quit()
    elif dealersvalue < playersvalue:
        print("You got closer to 21 than the dealer! you win!")
        quit()
    elif dealersvalue == playersvalue:
        print("Your hand is equal to the dealers hand. Its a tie!")
        quit()

def whatDoesDealerDo():
    global dealersvalue
    if haschosentostay == True:
        print("You decided to stay, the dealer reveals his hand. his cards are " + " and ".join(dealerhand))
        if dealersvalue == 21:
            print("he has a natural! you lose..")
            quit()
        if int(dealersvalue) < 17:
            print("The dealer has less than 17, so he hits")
            dealerhand.append(completeddeck[0])
            del completeddeck[0]
            print("The card he drew was "+ dealerhand[-1])
            dealersvalue = addExtraCard(dealersvalue, dealerhand[-1])
            checkIfDealerWon(dealersvalue)
        else:
            print("The value of the dealers hand adds up to "+ str(dealersvalue) + " so he has to stay")
            whoWon()

def checkIfDealerWon(value):
    global dealerhaschosentostay, dealerusedace, dealersvalue
    if dealersvalue == 21:
        print("The dealer got to 21! You lose...")
        quit()
    elif dealersvalue > 17 and value < 21:
        print("The dealer has reached 17 or higher, he stays.")
        whoWon()
    elif dealersvalue > 21:
        if dealerusedace == False:
            checkIfYouHaveAnAce(dealerhand, dealersvalue)
        if value > 21:
            print("The dealer busted! You win!")
            quit() 
        else:
            print("The dealer went over 21 so he was forced to turn his ace into a 1...")
            dealerusedace = True
            print("He draws another card")
            dealerhand.append(completeddeck[0])
            del completeddeck[0]
            print("The card he drew was "+ dealerhand[-1])
            checkIfDealerWon()
    elif dealersvalue < 17:
        print("The dealer still has less than 17, so he hits")
        dealerhand.append(completeddeck[0])
        del completeddeck[0]
        print("The card he drew was "+ dealerhand[-1])
        dealersvalue = addExtraCard(dealersvalue, dealerhand[-1])   
        checkIfDealerWon(dealersvalue)

def checkIfPlayerWon(value):
    global hitorstay, haschosentostay, playersvalue, playerusedace
    while True:
        if playersvalue == 21:
            print("You got 21! You win!")
            quit()
        elif playersvalue > 21:
            if playerusedace == False:
                playersvalue = checkIfYouHaveAnAce(playerhand, playersvalue)
            if playersvalue > 21:
                print("You busted! You lose...")
                quit()
            else:
                print("You were forced to turn your ace into a 1 since you went over 21...")
                playerusedace = True
                break
        elif playersvalue < 21:
                hitorstay = input("Would you like to hit or stay? The value of your current cards adds up to "+ str(playersvalue)+ " ")
                if hitorstay == "stay":
                    haschosentostay = True
                    break
                elif hitorstay == "hit":
                    playerhand.append(completeddeck[0])
                    del completeddeck[0]
                    print("The dealer gives you a card. The card given is "+ playerhand[-1])
                    playersvalue = addExtraCard(playersvalue, playerhand[-1])
                    continue
                elif hitorstay == "quit":
                    quit()
                elif hitorstay == "show":
                    showDevInfo()
                else:
                    print("Thats an incorrect input, please respond with either hit or stay")
                    


generateCards({"hearts", "clubs", "spades", "diamonds"}, ["ace","2","3","4","5","6","7","8","9","10","jack","queen","king"])
addCardsToHand(playerhand)
addCardsToHand(dealerhand)
dealersvalue = findhandValue(dealersvalue, dealerhand)
playersvalue = findhandValue(playersvalue, playerhand)
print("Welcome to blackjack! The fun gambling game for all ages!")
print("The game will start now!")
print("The dealer gives you your cards. The cards you got this round are "+ " and ".join(playerhand))
print("The dealer reveals one of his cards, the card revealed is "+ "".join(dealerhand[0]))
while True:
    checkIfPlayerWon(playersvalue)
    whatDoesDealerDo()