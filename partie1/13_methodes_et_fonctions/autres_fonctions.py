"""Voici quelques fonctions utiles"""

print(len("Python")) # dans le cas d'une str, len() renvoie le nombre de caractères dans la str (espaces compris)
print(len([1, 2, 3])) # dans le cadre d'une liste, len() renvoie le nombre d'éléments dans la liste

print(round(4.2)) # renvoie l'entier le plus proche --> 4
print(round(4.5)) # --> 4
print(round(4.51)) # --> 5

print(min([12, 43, 65])) # min() renvoie la valeur la plus petite dans une liste de nombres
print(max([12, 43, 65])) # min() renvoie la valeur la plus grande dans une liste de nombres
print(min(["Julien", "Thomas", "Christophe"])) # dans le cas de str, min() renvoie le premier placé dans l'alphabet
print(max(["Julien", "Thomas", "Christophe"])) # dans le cas de str, max() renvoie le dernier placé dans l'alphabet

print(sum([10, 15, 20 + 8], 3 * 2)) # sum() renvoie la somme des deux paramètres passés

print(range(5)) # objet de type range allant de 0 à 4 (5 nombres)
print(range(2, 5)) # renvoie un objet de type range allant de 2 à 4 (deuxième paramètre exclusif)