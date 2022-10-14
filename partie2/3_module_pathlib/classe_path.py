"""
En important l'objet (classe) Path depuis le module pathlib, on a accès à un certain nombre de méthodes nous permettant d'effectuer des actions facilement, notamment des
chemins couramment utilisés
"""

from pathlib import Path

user_file = Path.home() # renvoie le chemin du dossier utilisateur
print(user_file) # /home/teste
print(type(user_file)) # <class 'pathlib.PosixPath'> --> type de l'objet

cur_dir = Path.cwd() # renvoie le chemin du dossier courant
print(cur_dir) # /home/teste/Documents/Docstring/python_docstring
print(type(cur_dir)) # <class 'pathlib.PosixPath'>

print(cur_dir.parent) # renvoie le chemin du dossier parent