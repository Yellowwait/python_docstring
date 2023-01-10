"""Pour ajouter un module au PYTHONPATH, on utilise la méthode append()"""
import sys
from pprint import pprint
sys.path.append("/home/jonathan/Documents/mes_modules")
import module_test

pprint(sys.path)