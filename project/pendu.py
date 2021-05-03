import random

listeMot = ["alpha", "beta", "delta"]

motChoisi = random.choice(listeMot)
lenMotChoisi = len(motChoisi)
lenLettreTrouve = 0

vies = 7
mot = ""
lettreTrouve = ""

for lettre in motChoisi :
    mot = mot + "_"

while vies > 0 and lenMotChoisi > lenLettreTrouve :
    print("Mot choisi : ", mot)
    lettreUser = input("lettre ? ")

    if lettreUser in motChoisi:
        print("Lettre trouve : \n", lettreUser)
        lettreTrouve = lettreTrouve + lettreUser

        mot = ""
        lenLettreTrouve = 0
        for lettreAdd in motChoisi :
            if lettreAdd in lettreTrouve :
                mot = mot + lettreAdd
                lenLettreTrouve += 1
            else :
                mot = mot + "_"

    else :
        vies -= 1
        print("il te reste : ", vies, " chance de réussir sinon c'est perdu")


if(vies == 0):
    print("Vous n'avez plus de vie, vous avez perdu, le mot était : ", motChoisi)
elif(lenLettreTrouve == lenMotChoisi):
    print("vous avez gagnez bravo !!! le mot était : ", motChoisi)
