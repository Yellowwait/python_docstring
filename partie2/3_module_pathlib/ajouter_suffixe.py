"""Voici un exemple concret de l'utilisation de pathlib : ajouter un élément entre le nom du fichier et son extension"""

from pathlib import Path

p = Path.home() / "Téléchargements" / "moi-bg.jpg" # chemin vers le fichier à modifier

p.parent / p.stem # PosixPath('/home/teste/Téléchargements/moi-bg')
p.parent / (p.stem + "-highres" + p.suffix) # PosixPath('/home/teste/Téléchargements/moi-bg-highres.jpg')