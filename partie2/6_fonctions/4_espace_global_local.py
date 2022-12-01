"""Ici nous allons voir la différence entre espace global et espace local. Les variables définies à l'intérieur d'une fonction appartiennent uniquement à la fonction"""

a = 5 # ESPACE GLOBAL


def fonction():
    a = 10 # ESPACE LOCAL
    b = 5
    print(a) # ici a = 10

fonction() # même si on appelle la fonction, a gardera sa valeur de l'espace global
print(a) # ici a = 5 car c'est l'espace global
# print(b) # ERREUR car b est définie dans l'espace local de la fonction

"""En revanche une variable définie dans l'espace global peut être accessible à l'intérieur d'une fonction"""

c = 23

def exemple():
    print(c)

exemple() # c = 23 car la variable est définie dans l'espace global et donc accessible par la fonction

"""Il y a toujours, par définition un seul espace global mais on peut créer plusieurs espaces locaux"""