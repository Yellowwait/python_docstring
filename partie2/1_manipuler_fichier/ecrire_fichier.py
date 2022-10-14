chemin = "/home/teste/Documents/Docstring/formation/partie2/manipuler_fichier/fichier.txt"

with open(chemin, "w") as f: # ici on passe le mode d'ouverture en "w" pour write (écrase le contenu précédent lorsqu'on sauvegarde)
    f.write("Bonjour")