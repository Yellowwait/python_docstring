"""
Les choses se compliquent lorsqu'on utilise des objets muables. Ici on a deux variables de noms différents pointants vers le même objet
"""

def foo(param):
    param.append(1)

var = []

foo(param=var)
print(var) # ici var va être également modifié car var = param et on ajoute 1 dans la liste qui est un objet muable