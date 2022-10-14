"""
DATA.JSON
On ne peut pas directement ajouter en mode "append" des données dans un fichier .json comme on le ferait dans un .txt.
Il faut d'abord récupérer les données, les modifier puis écraser le fichier initial avec les données modifiées.
"""

import json
"""
# Si l'on procède ainsi, on va simplement coller la deuxième liste à la première, ce qui est faux et on n'a pas la virgule
with open("data.json", "a") as f:
    json.dump([4], f, indent=4)
"""

with open("data.json", "r") as f: # on ouvre le fichier .json en mode lecture
    donnees = json.load(f) # on stocke son contenu dans une variable donnees

donnees.append(4) # on ajoute le chiffre 4 à la liste

with open("data.json", "w") as f: # on ouvre à nouveau le fichier .json mais en mode écriture
    json.dump(donnees, f, indent=4) # on écrase le contenu précédent avec le nouveau contenant le chiffre 4