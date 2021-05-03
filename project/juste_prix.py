import random

prix = random.randint(0,10000)

finie = True
while finie :
    entree = int(input("donnez un prix"))
    if (entree == prix) :
        print ("you win")
        finie = False
    elif (entree > prix) :
        print("moins")
    elif (entree < prix) :
        print("plus")

               
