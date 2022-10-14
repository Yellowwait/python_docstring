import random
from pprint import pprint # on importe uniquement la fonction pprint depuis le module pprint

print(dir(random)) # dir() affiche toutes les fonctions disponibles à l'intérieur d'un module
pprint(dir(random)) # affiche le résultat de dir() mais sous forme de liste (plus lisible)
help(random.randrange ) # donne des détails sur la fonction en paramètres (ne pas ajouter les parenthèses après car on n'appelle pas la fonction)qqqq