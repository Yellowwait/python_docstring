"""Voici les équivalences entre les modules os et pathlib pour créer des constantes permettant d'accéder à différents dossiers du projet"""

import os

SOURCE_FILE = os.path.realpath(__file__) # renvoie le chemin du fichier courant
SOURCE_DIR = os.path.dirname(SOURCE_FILE) # renvoie le chemin du dossier parent du fichier courant
ROOT_DIR = os.path.dirname(SOURCE_DIR) # renvoie le chemin du dossier parent du dossier parent
DATA_DIR = os.path.join(SOURCE_DIR, "DATA") # permet de concaténer des chemins de dossiers

from pathlib import Path

SOURCE_FILE = Path(__file__).resolve() # renvoie le chemin du fichier courant
SOURCE_DIR = SOURCE_FILE.parent # renvoie le chemin du dossier parent du fichier courant
ROOT_DIR = SOURCE_DIR.parent # renvoie le chemin du dossier parent du dossier parent
DATA_DIR = SOURCE_DIR / "DATA" # permet de concaténer des chemins de dossiers