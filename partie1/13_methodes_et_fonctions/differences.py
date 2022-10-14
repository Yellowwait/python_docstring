"""Bien que similaires, fonctions et méthodes se différencient. Une méthode est une fonction appartenant à un objet.
Les méthodes, contrairement aux fonctions, font muer les objets dits muables."""

liste = [5, 3, 9, 7, 1]
sorted(liste) #  la FONCTION sorted(liste) n'agit pas directement sur la liste. Elle renvoie une copie triée de la liste sans toucher à la liste d'origine.
print(liste) # on peut le voir ici car liste n'a pas été modifié
liste = sorted(liste) # si on veut modifier la liste d'origine il faut donc l'écraser de cette manière
print(liste)

# ----------------------

liste2 = [8, 2, 6, 4, 10]
liste2.sort() # la MÉTHODE sort() fait muer directement l'objet. Pas besoin de le réassigner à une variable ou d'écraser la précédente
print(liste2)