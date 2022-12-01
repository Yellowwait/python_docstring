"""Les fonctions locals() et globals() permettent d'afficher à n'importe quel endroit l'espace global et local et les objets qu'ils contiennent sous forme de dictionnaire."""

from pprint import pprint

def foo():
    b = 5
    # pprint(locals()) # ici on aura uniquement la variable b puisque à ce niveau, en local il n'y a que la variable b
    # pprint(globals()) # renvoie à nouveau tous les objets de l'espace global
    print(a) # pas dispo en local mais en global donc OK
    c = 12

print(c) # ici c n'existe ni dans l'espace local (qui est le global), ni dans le global donc ERREUR
a = 5
foo()

"""À ce niveau, espace global et local sont les mêmes"""

print(globals() == locals()) # renvoie True
# pprint(globals())
# pprint(locals())

"""Python cherche toujours d'abord une variable dans l'espace local puis après dans l'espace global. C'est pour cette raison qu'une variable définie dans le global est accessible par une fonction en local mais pas l'inverse"""