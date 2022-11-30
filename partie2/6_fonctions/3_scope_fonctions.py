"""Ici nous allons voir comment bien définir une fonction au bon endroit"""

# test() # renvoie une erreur car la fonction n'est définie qu'à la ligne 6

# def test():
#     print("Bonjour")

"""Voici un autre exemple"""

def test2():
    affiche_bonjour() # on pourrait penser à une erreur car affiche_bonjour n'est pas encore défini. Mais Python n'exécute pas cette ligne, on ne fait que définir la fonction test2, on ne l'appelle pas. Python stocke en mémoire.

def affiche_bonjour():
    print("Bonjour !")

test2()