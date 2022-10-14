import os
import sys
import json

# Les variables globales sont définies par convention en majuscule

CUR_DIR = os.path.dirname(__file__) # permet de récupérer le chemin du dossier parent du fichier courant
LISTE_PATH = os.path.join(CUR_DIR, "liste.json") # on concatène le chemin du dossier parent avec le nom du fichier .json

MENU = """Choisissez parmi les 5 options suivantes :
1 : Ajouter un élément à la liste
2 : Retirer un élément de la liste
3 : Afficher la liste
4 : Vider la liste
5 : Quitter
👉 Votre choix : """

CHOIX_MENU = [str(i) for i in range(1, 6)] # contient les choix que l'utilisateur peut faire, on vérifie que son choix est bien dans la liste

if os.path.exists(LISTE_PATH): # si le chemin vers la liste .json existe
    with open(LISTE_PATH, "r") as f: # on ouvre le fichier et on le stocke dans une variable f
        LISTE = json.load(f) # on lit son contenu et on le stocke dans une variable LISTE
else: # sinon
    LISTE = [] # on génère une liste vide

while True:
    choix_utilisateur = "" # on déclare une variable vide pour boucler au moins une fois dans la boucle du dessous
    while choix_utilisateur not in CHOIX_MENU: # tant que le choix fait par l'utilisateur ne fait pas partie des options de CHOIX_MENU
        choix_utilisateur = input(MENU) # on lui demande de choisir
        if choix_utilisateur not in CHOIX_MENU: # puis on vérifie si le choix qu'il a fait fait partie de CHOIX_MENU
            print("Votre choix ne fait pas partie des options...")
        print("-" * 50)
    
    if choix_utilisateur == "1":
        element = input("Entrez l'élément à ajouter à votre liste de courses : ") # on demande l'élément à ajouter à la liste
        LISTE.append(element) # on l'ajoute à la liste
        print(f"L'élément {element} a bien été ajouté à votre liste !") # on affiche que l'élément a bien été ajouté à la liste
    elif choix_utilisateur == "2":
        element = input("Entrez le nom de l'élément à retirer de votre liste de courses : ") # on demande l'élément à retirer
        if element in LISTE: # on vérifie si l'élément est bien présent dans la liste
            LISTE.remove(element) # si oui, on le retire
            print(f"L'élément {element} a bien été retiré de la liste !") # on affiche qu'il a été retiré
        else: # sinon
            print(f"L'élément {element} ne fait pas partie de la liste !") # on affiche que l'élément n'est pas dans la liste
    elif choix_utilisateur == "3":
        if LISTE: # si la liste n'est pas vide
            print("Voici ce que contient votre liste :")
            for i, element in enumerate(LISTE, 1): # enumerate permet de récupérer les indices et éléments d'une liste, ici on fait démarrer à 1 au lieu de 0
                print(f"{i}. {element}") # ici on affiche l'indice en i et l'élément en element
        else:
            print("Votre liste ne contient aucun élémént !") # on affiche que la liste ne contient rien
    elif choix_utilisateur == "4":
        if LISTE: # si la liste n'est pas vide
            LISTE.clear() # on la vide
            print("Votre liste de courses a été vidée !") # on indique que la liste a été vidée
        else: # si elle est vide
            print("Votre liste ne contient aucun élémént !") # on indique qu'elle ne contient rien
    elif choix_utilisateur == "5":
        with open(LISTE_PATH, "w") as f: # avant de fermer le script, on ouvre à nouveau la liste .json mais en mode ÉCRITURE
            json.dump(LISTE, f, indent=4) # on écrit le contenu de LISTE dans la variable f qu'on indente de 4 pour la lisibilité
        print("À bientôt !")
        sys.exit()
    
    print("-" * 50)