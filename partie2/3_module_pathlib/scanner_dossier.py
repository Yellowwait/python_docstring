"""
Comment récupérer tous les sous-dossiers et les fichiers à l'intérieur d'un dossier également de manière récursive (en boucle). Faire sur l'interpréteur Python.
"""

from pathlib import Path

Path.home().iterdir() # <generator object Path.iterdir at 0x7f6fdb6833e0> --> renvoie un objet generator (sur lequel on peut itérer)

for f in Path.home().iterdir(): # f renvoie à un objet de type Path
    print(f.name) # ici on veut afficher simplement le nom des dossiers/fichiers (après le dernier slash)

"""On peut également faire une compréhension de liste pour avoir directement les éléments qui sont des dossiers ou des fichiers"""

dossiers = [f.name for f in Path.home().iterdir() if f.is_dir()]
fichiers = [f.name for f in Path.home().iterdir() if f.is_file()]