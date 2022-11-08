"""Voici un projet de script permettant de trier des fichiers en fonction de leur extension."""

from pathlib import Path

dirs = {".png": "Images",
        ".jpeg": "Images",
        ".jpg": "Images",
        ".gif": "Images",
        ".mp4": "Videos",
        ".mov": "Videos",
        ".zip": "Archives",
        ".pdf": "Documents",
        ".txt": "Documents",
        ".json": "Documents",
        ".mp3": "Musiques",} # on crée un dictionnaire qui mappe les extensions des fichiers avec le dossier dans lequel on veut les ranger

tri_dir = Path.home() / "Téléchargements" # on récupère le chemin du dossier à trier
files = [f for f in tri_dir.iterdir() if f.is_file()] # on récupère tous les fichiers à l'intérieur du dossier_tri grâce à iterdir() et une compréhension de liste
for f in files: # on boucle sur la liste de fichiers pour les déplacer
    output_dir = tri_dir / dirs.get(f.suffix, "Autres") # on concatène le dossier de tri avec le nom de dossier correspondant à chaque extension de dirs ("Autres" si introuvable)
    output_dir.mkdir(exist_ok=True) # on crée le dossier dans lequel on va ranger les fichiers (exist_ok=True pour ne pas renvoyer d'erreur si le dossier existe déjà)
    f.rename(output_dir / f.name) # on renomme le chemin d'origine du fichier avec son nouveau chemin d'accès