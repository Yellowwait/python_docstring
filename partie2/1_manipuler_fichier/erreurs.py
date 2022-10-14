"""
Certaines erreurs arrivent fréquemment, voici les plus courantes :
    - erreur de mode ("r" au lieu de "w" par exemple)
    - oubli de fermeture de fichier avec close()
"""

chemin = "/home/teste/Documents/Docstring/formation/partie2/manipuler_fichier/fichier.txt"

f = open(chemin, "r") # on ouvre le fichier en stockant son contenu dans une variable f
print(f.read()) # on affiche son contenu une première fois
contenu = f.read() # on crée une variable contenant le contenu du fichier
print(contenu) # on affiche le contenu une deuxième fois mais rien ne se passe, juste une ligne vide
f.close() # on ferme le fichier

"""
Il faut imaginer un curseur qui commence au début du fichier, à la première lettre. Une fois le fichier lu, le 
curseur se retrouve à la toute fin du contenu donc lorsqu'on veut l'afficher une deuxième fois, il n'y a plus rien à afficher
donc on voit une ligne vide. Voici comment résoudre le problème (avec la méthode with pour ne pas avoir à faire un close())
"""

with open(chemin, "r") as f:
    print(f.read()) # on affiche le contenu une première fois (curseur à la fin)
    f.seek(0) # on replace le curseur au début (indice 0)
    contenu = f.read(10) # on stocke le contenu dans une variable et on peut préciser où la lecture doit s'arrêter
    print(contenu) # on affiche une nouvelle fois le contenu