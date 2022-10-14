# Les bool sont considérés comme une sous-classe des int. On peut le vérifier avec cette classe :

print(issubclass(bool, int)) # renvoie True
print(True + 1) # renvoie 2
print(False + 3) # renvoie 3
print("\n")

# Par défaut, chaque objet a une valeur False. On peut le vérifier avec la fonction bool()

print(bool("")) # False tant que la string est vide
print(bool("a")) # True
print(bool(0)) # False tant que égal à 0. True si positif ou négatif
print(bool(2)) # True
print(bool(0.0)) # False
print(bool(-3.5)) # True
print(bool([])) # False tant que la liste est vide
print(bool({})) # False tant que le dictionnaire est vide