from pathlib import Path

p = Path.home()
p = p / "PathLib" / "readme.txt"
p.write_text("Bonjour") # cette fonction permet d'écrire du texte dans le fichier sélectionné (cette méthode crée en même temps le fichier readme.txt s'il n'existe pas déjà)
p.read_text() # permet de lire le contenu du fichier (ne fonctionne que dans l'interpréteur virtuel Python, pas dans le script directement)