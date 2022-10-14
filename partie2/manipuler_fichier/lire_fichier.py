chemin = "/home/teste/Documents/Docstring/formation/partie2/manipuler_fichier/fichier.txt"

"""
open() permet d'ouvrir un fichier en lui passant en premier argument le chemin et en deuxième le mode d'ouverture (ici "r" pour "read"). On stocke ensuite
un objet fichier dans la variable f.
"""
f = open(chemin, "r")
print(f) # renvoie un TextIOWrapper qui est un objet permettant de lire le contenu du fichier
f.close() # avec cette méthode il faut s'assurer de fermer le fichier ensuite