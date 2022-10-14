# FICHIER.JSON

import json

chemin = "/home/teste/Documents/Docstring/formation/partie2/fichiers_json/fichier.json"

# La méthode dump() permet d'écrire dans un fichier json (préciser quoi écrire et dans quel fichier)
with open(chemin, "w") as f:
    # json.dump("Bonjour", f)
    # json.dump(list(range(10)), f) --> renvoie une liste de 10 chiffres mais en ligne
    json.dump(list(range(10)), f, indent=4) # --> permet de donner un niveau d'indentation (ici 4 comme Python)