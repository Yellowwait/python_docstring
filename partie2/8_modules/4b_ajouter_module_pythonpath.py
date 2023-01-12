"""
Pour ajouter un module au PYTHONPATH, on utilise la méthode append(). Le problème est qu'avec cette méthode, on est obliger de le faire pour chaque script
dans lequel on voudra utiliser le module en question
"""

import sys
from pprint import pprint
# sys.path.append("/home/jonathan/Documents/mes_modules")

pprint(sys.path)