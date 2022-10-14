"""
Cette méthode permet de fermer automatiquement le fichier ensuite et évite d'avoir à utiliser la méthode close()
"""

chemin = "/home/teste/Documents/Docstring/formation/partie2/manipuler_fichier/fichier.txt"

# Avec read(), les retours à la ligne sont interprétés par Python
with open(chemin, "r") as f:
    contenu = f.readlines()
    print(contenu)

"""
Autres méthodes :
    - repr(f.read()) permet de ne pas interpréter les caractères spéciaux (et donc de voir les sauts de ligne sous forme de \n) --> on récupère une str
    - f.readlines permet de récupérer une liste contenant chaque ligne comme élément (avec le saut de ligne non interprété)
    - f.read().splitlines permet de récupérer chaque ligne dans une liste mais les sauts de ligne sont interprétés (sans les \n)
"""