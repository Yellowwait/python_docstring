"""
Les callables sont des objets que l'on peut appeler (comme une fonction) ils sont suivis de parenthèses ().
Les modules en revanche ne peuvent pas être appelés (ex : os() ne fonctionne pas), on les importe. On peut vérifier cela grâce
à la fonction callable() qui nous renvoie un booléen en fonction de si oui ou non un objet est callable.
"""

import os
from pprint import pprint

print(callable(pprint)) # renvoie False si on n'a pas importé la fonction pprint depuis le module pprint et True si oui
print(callable(os.name)) # renvoie False car os.name n'est pas callable car c'est un attribut