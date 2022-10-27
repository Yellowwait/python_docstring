"""
Voici les principales informations de fichiers que l'on peut récupérer grâce au module pathlib.
"""

from pathlib import Path

p = Path("/Users/jonathan/Documents/index.html") # Path convertit la str en chemin de dossier
print(p.name) # index.html
print(p.parent) # renvoie le chemin du dossier parent
print(p.parent.joinpath(p.name)) # ici on recrée le chemin entier
print(p.stem) # index
print(p.suffix) # .html
print(p.suffixes) # permet de récupérer les différentes extensions d'un fichier sous forme de liste s'il y en a plusieurs (ex : .tar.gz)
print(p.parts) # renvoie les différentes partie d'un chemin
print(p.exists()) # renvoie un booléen en fonction de si le fichier existe ou non
print(p.is_dir()) # permet de dire s'il s'agit d'un dossier ou non
print(p.is_file()) #  permet de dire s'il s'agit d'un fichier ou non (ici False parce que le fichier n'existe pas dans le disque)