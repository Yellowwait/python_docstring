employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
element = employes.pop(2) # retire l'élément correspondant à l'indice et le stocke
print(element)
print(employes)
employes.clear()
print(employes) # comme sort() ne pas stocker dans une variable car renvoie None sinon

# -----------------------------------------

villes = ["Paris", "Lion", "Marseille", "Paris"]

villes[1] = "Lyon" # on peut rectifier la faut d'orthographe
print(villes)

villes.append("Strasbourg") # va ajouter l'élément à la fin de la liste
print(villes)

del villes[0] # supprime l'élément d'indice 0
print(villes)

for ville in villes:
    print(ville.upper()) # renvoie chaque ville en majuscule

villes_set = set(list(villes))
print(villes_set)