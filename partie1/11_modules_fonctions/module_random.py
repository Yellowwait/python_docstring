"""Pour importer un module, on procède comme ceci"""

import random # on utilise la commande import suivie du nom du module, ici random

r = random.randint(1, 6) # la fonction randint() permet de générer un entier compris entre les deux chiffres passés en paramètres inclus
print(r)

r2 = random.uniform(0, 1) # la fonction uniform() est comme randint() mais renvoie un float
print(r2)

r3 = random.randrange(999) # comme randint() mais avec un seul paramètres (par défaut entre 0 et x exclus)
print(r3)

r4 = random.randrange(0, 101, 10) # randrange() permet de passer un pas en paramètres, ce qui renvoie uniquement des multiples de 10 entre 0 et 100
print(r4)