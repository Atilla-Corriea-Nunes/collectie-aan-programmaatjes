import random
import string
themissingones = []
password = []
letterslow = string.ascii_lowercase
lettersup = string.ascii_uppercase
digits = string.digits
specialchar = ["@", "#", "$", "%", "&", "_", "?"]
upamount = (random.randint(2, 6))
numamount = (random.randint(4, 7))
for x in range(upamount):
    password.append(random.choice(lettersup))
for x in range (0,8):
    password.append(random.choice(letterslow))
first = password[:3]
last = password[len(password)-1]
middleoflist = list(password[3: len(password)-1:])
for x in range (0,3):
    middleoflist.append(random.choice(specialchar))
for x in range (numamount):
    middleoflist.append(random.choice(digits))    
themissingones = list(first) + list(last)

while (len(middleoflist) < 20):
    middleoflist.append(random.choice(letterslow))
random.shuffle(middleoflist)
random.shuffle(themissingones)
first = themissingones[:3]
finishedPassword = list(first) + list(middleoflist) + list(last)
print("".join(finishedPassword))