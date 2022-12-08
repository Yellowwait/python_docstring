"""
Le passage par référence correspond à l'idée que, lorsqu'on donne une valeur à une fonction, on va donner une référence à l'objet.
"""

# Ici les id affichés seront les mêmes car param et var renvoient au même objet et qu'un int est un objet immuable

def foo(param):
    param = 10
    print(id(param))

var = 5

print(id(var))
foo(var)
print(var) # ici var ne change pas 