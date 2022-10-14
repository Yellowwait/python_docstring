chemin = "/home/teste/Documents/Docstring/formation/partie2/manipuler_fichier/fichier.txt"

# Le mode d'ouverture "a" pour "append" permet d'ajouter du contenu au fichier txt sans écraser le contenu précédent
with open(chemin, "a") as f:
    f.write("\nAu revoir")