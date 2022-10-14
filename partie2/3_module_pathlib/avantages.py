"""
Avant l'apparition de pathlib, il était facile de faire des erreurs lorsqu'on voulait effectuer certaines opérations avec les modules os, shutil ou globe comme :
    - récupérer le chemin d'un dossier parent --> os.path.dirname("/Users/jonathan/main.py") renvoie une str et pas un objet
    - os.path.dirname(os.path.dirname("/Users/jonathan/main.py")) --> pour récupérer le dossier parent du dossier parent (long et illisible)
    - récupérer l'extension d'un fichier --> os.path.splitext("/Users/jonathan/main.py")[1] (l'indice 1 est ce qu'il y a après le point et l'indice 0 ce qu'il y a avant)
Pour palier à cela, on a créé le module PATHLIB qui facilite la tâche
"""

import os

dossier_parent = os.path.dirname("/Users/jonathan/main.py")
dossier_parent_parent = os.path.dirname(os.path.dirname("/Users/jonathan/main.py"))
extension = os.path.splitext("/Users/jonathan/main.py")[1]

print(dossier_parent)
print(dossier_parent_parent)
print(extension)