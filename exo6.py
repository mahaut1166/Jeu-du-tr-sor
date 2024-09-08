def initialiserJoueur():
    import random
    xjoueur = random.randint (1,100)
    yjoueur = random.randint (1,100)
    return (xjoueur,yjoueur)

def initialiserTresor():
    import random
    xtresor = random.randint(1,100)
    ytresor = random.randint (1,100)
    return xtresor,ytresor

def nouvellePosition(xjoueur, yjoueur):
    print(f"Votre position est({xjoueur},{yjoueur})")
    mouvement = str(input("Dans quelle direction veux-tu aller ? Répond par la première lettre de la direction. Ex: je veux aller en haut -> h   "))
    pas = int(input("Entre le nombre de pas que tu veux effectuer "))
    xtmp = xjoueur
    ytmp = yjoueur

    if mouvement == "h":
        yjoueur += pas 
    elif mouvement == "b":
        yjoueur -= pas
    elif mouvement == "g":
        xjoueur -= pas
    elif mouvement == "d":
        xjoueur += pas
    else:
        print("Le type de réponse entrée pour la direction ne correspond pas à ce qui est attendu, veuillez réessayer")
        nouvellePosition(xjoueur,yjoueur)
    return (xjoueur, yjoueur,xtmp,ytmp)

def avancer (xjoueur, yjoueur,xtmp,ytmp):
    if (1 <= xjoueur <= 100)  & (1 <= yjoueur <= 100) :
        return xjoueur,yjoueur
    else:
        if xjoueur < 1:
            n = "à gauche"
        elif xjoueur > 100:
            n = "à droite"
        elif yjoueur > 100:
            n = "en haut"
        elif yjoueur < 1:
            n = "en bas"
        print(f"Vous être trop {n}, vous ne pouvais pas aller dans ce sens choisissez à nouveau")
        xjoueur, yjoueur, xtmp,ytmp = nouvellePosition(xtmp,ytmp)
        avancer(xjoueur,yjoueur,xtmp,ytmp)
    return xjoueur,yjoueur

def distance(xjoueur, yjoueur):
    from math import sqrt
    x = xtresor - xjoueur
    y = ytresor - yjoueur
    dist = sqrt (( x**2)+(y**2))
    return (dist)

def aide(xjoueur,yjoueur):
    if xjoueur == xtresor:
        print("Ton x est juste")
    if yjoueur == ytresor:
        print("Ton y est juste")

def gagner(xdistanceTresor,ydistanceTresor):
    gagner = False
    if xdistanceTresor == 0 & ydistanceTresor == 0:
        gagner = True
    return (gagner)

def alertChemin(adistance,ndistance):
    dist = adistance - ndistance
    if adistance < 0:
        adistance = -adistance
    
    if ndistance <0:
        ndistance = -ndistance

    if dist <= 0:
        chaud = False
    else:
        chaud = True
    return (chaud)

def lancerJeu():
    nbMouvementsMax = int(input("Combien de mouvements au plus veux-tu avoir? "))
    return nbMouvementsMax



# CODE DEROULEMENT JEU #

xjoueur, yjoueur = initialiserJoueur()
xtresor, ytresor = initialiserTresor()
nbMax = lancerJeu()
nbEssai = -1

while nbEssai != nbMax :
    nbEssai += 1
    aDistanceTresor = distance(xjoueur,yjoueur)

    xjoueur,yjoueur,xtmp,ytmp = nouvellePosition(xjoueur,yjoueur)
    avancer(xjoueur,yjoueur,xtmp,ytmp)

    nDistanceTresor = distance(xjoueur,yjoueur)
    if nDistanceTresor == 0 :
        print(f"Tu as gagné !!! Le trésor était sur la case ({xtresor},{ytresor})")
        break

    chaud = alertChemin(aDistanceTresor,nDistanceTresor)
    if chaud==True:
        print("Tu te rapproches")
    else:
        print("Tu t'éloignes")

    aide(xjoueur,yjoueur)

    print(f"Vous avez encore {nbMax-nbEssai} mouvements")

if nbEssai == nbMax:
    print(f"Perdu !!!!! Le trésor était sur la case ({xtresor},{ytresor})")