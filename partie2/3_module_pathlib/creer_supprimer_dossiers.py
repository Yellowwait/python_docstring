from pathlib import Path
import shutil

"""Créer un dossier"""

p = Path.home() # p = ~
p = p / "DossierTest" # on définit un chemin pour le dossier à créer --> p = ~/DossierTest

# p.mkdir() # la méthode mkdir va créer le dossier DossierTest (renvoie une ERREUR si le dossier existe déjà)
# p.mkdir(exist_ok=True) # ce paramètre permet que le script ne renvoie pas d'ERREUR si le dossier existe déjà (mais ne le crée pas une nouvelle fois)

"""Créer une arborescence de dossiers"""

p = p / "1" / "2" / "3" # on définit une arborescense de dossiers --> p = ~/DossierTest/1/2/3
# p.mkdir() # ERREUR car au moins un dossier parent n'existe pas
# p.mkdir(parents=True) # permet de créer l'ensemble de l'arborescence

"""Créer un fichier"""

p = p / "readme.txt" # p = ~/DossierTest/1/2/3/readme.txt
# p.touch() # crée un fichier

"""Supprimer un fichier"""

# p.unlink() # supprime un fichier

"""Supprimer un dossier vide"""

p = p.parent # p = ~/DossierTest/1/2/3
# p.rmdir()

"""Supprimer un dossier non vide : c'est le seul cas de figure où on va être obligé d'utiliser shutil"""

p = p.parent.parent.parent # p = ~/DossierTest
# p.rmdir() # ERREUR car dossier non vide
shutil.rmtree(p) # cette méthode permet de supprimer une hiérarchie de dossiers même si elle n'est pas vide