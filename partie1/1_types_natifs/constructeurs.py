"""
Python par défaut reconnaît les types de données (avec les guillemets pour les str par exemple).
On peut cependant convertir un type de donnée vers un autre.
"""

print(int("5")) # convertit la str en int
print(str(4)) # convertit le int en str
print(str(True))
print(int(True)) # renvoie 1
print(True)
print(int("Bonjour")) # erreur car impossible de convertir un mot en entier