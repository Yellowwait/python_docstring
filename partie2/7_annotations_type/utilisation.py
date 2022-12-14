"""Les annotations de type permettent de préciser quel type de valeur est attendu lors de la définition d'une fonction et ainsi de prévenir les erreurs."""

# def addition(a, b):
#     return a + b

# addition("5", 3) # renvoie une erreur car str + int

def addition_corrige(a:int, b:int) -> int: # ici on précise le type de valeur attendues en arguments mais également le type de l'objet retourné
    return a + b


print(addition_corrige(4, 12))