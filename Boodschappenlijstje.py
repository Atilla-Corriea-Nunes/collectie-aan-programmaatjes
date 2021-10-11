shoppinglist = {}
x = 0

def addToShoppinglist(currentitem):
        if x == 1:
            pass
        elif currentitem in shoppinglist:
            shoppinglist[currentitem] += 1
        else:
            shoppinglist.update({currentitem : 1})
        
        return shoppinglist



while True:
    item = input("Welk item wilt u aan het boodschappenlijstje toevoegen? ")
    addToShoppinglist(item)    
    leave = input("Wilt u nog een item toevoegen? (Y/N) ")
    if (leave.lower() == "y"):
        continue
    else:
        x = 1
        print(addToShoppinglist(item))
        break
        