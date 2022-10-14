"""On peut vérifier si une str commence ou se termine par une str donnée.
C'est utile notamment pour vérifier si l'extension d'un fichier est la bonne"""

fichier = "image.jpg"

print(fichier.endswith(".jpg")) # renvoie True
print(fichier.endswith(".mkv")) # renvoie False

print(fichier.startswith("image")) # renvoie True
print(fichier.startswith("video")) # renvoie False
