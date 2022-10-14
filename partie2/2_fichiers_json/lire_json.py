#FICHIER.JSON

import json

chemin = "/home/teste/Documents/Docstring/formation/partie2/fichiers_json/fichier.json"

# La méthode load() permet d'écrire dans un fichier json (préciser quoi écrire et dans quel fichier)
with open(chemin, "r") as f:
    liste_nombres = json.load(f)
    print(type(liste_nombres))
    print(liste_nombres)