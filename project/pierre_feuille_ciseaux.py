from random import choice

possibilite = ["Pierre", "Feuille", "Ciseaux"]
scoreA = 0
scoreB = 0
scoreMax = int(input("Quel score max pour un joueur ?"))

while scoreA < scoreMax and scoreB < scoreMax :
    entree = int(input("choississez :\n1 - pierre\n2 - feuille\n3 - ciseau"))
    robot = choice(range(3))

    print("\n{} VS {}".format(possibilite[a], possibilite[b]))    
    if (entree == robot) :
        print ("Egalité")
    elif (a > b and b+1 == a) or (a < b and a+b == 2):
        print("vous gagnez")
        scoreJ1 += 1
    else:
        print("vous perdez")
        scoreJ2 += 1

if(scoreA == scoreMax):
    print("Bravos !!! Vous avez gagnez à ", scoreJ1, " contre ", scoreJ2)

if(scoreB == scoreMax):
    print(":) Vous avez perdu à ", scoreJ1, " contre ", scoreJ2)
