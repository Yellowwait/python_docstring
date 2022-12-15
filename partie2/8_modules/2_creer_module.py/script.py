"""
En exécutant ce script, on a un dossier __pycache__ qui est créé contenant le fichier mon_module.cpython-310. C'est un fichier compilé utilisé par Python. Il
faut bien faire attention à ne pas nommer un module avec un nom de module déjà existant car on ne pourra plus utiliser les fonctions de ce module. Ex : si
j'appelle mon module random, je ne peux plus utiliser les fonctions du module random de base.
"""

import mon_module
import random
from pprint import pprint

print(mon_module.a)
print(random.randint(1, 5))
pprint(dir(random.uniform))