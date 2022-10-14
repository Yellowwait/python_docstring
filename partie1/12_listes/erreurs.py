"""Voici les erreurs les plus courantes lorsqu'on essaie de récupérer des éléments avec les indices"""

liste = [1, 2, 3, 4, 3]
print(liste(2)) # l'utilisation de parenthèses à la place de crochets est fréquente
liste.remove(0) # avec la méthode remove il faut préciser l'élément à supprimer et non pas son indice (ici 3)
liste.pop(0) # avec la méthode pop() on précise l'indice de l'élément à supprimer
liste.remove(3) # remove() ne supprime que la première instance de l'élément spécifié en paramètre
print(liste)