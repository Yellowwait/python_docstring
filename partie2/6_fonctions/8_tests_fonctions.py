"""Il n'est pas possible de définir un paramètre sans valeur par défaut après un paramètre avec une valeur par défaut"""

def foo(a=2, b):
    return a + b

foo(4) # renvoie une erreur

"""On peut remédier à ça de 3 manières différentes"""

def foo(a=2, b=2): # ajouter une valeur par défaut à b
def foo(a, b): # supprimer la valeur par défaut de a
def foo(b, a=2): # mettre a après b