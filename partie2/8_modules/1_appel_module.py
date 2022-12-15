"""Il est recommandé d'appeler la totalité d'un module plutôt qu'une seule de ses fonctions sous peine d'écraser le nom d'une fonction par une variable."""

from random import uniform
uniform = "Bonjour" # ici on écrase la fonction du module en la remplaçant par une variable. NE PAS FAIRE

from random import * # encore pire car ici on importe toutes les fonctions et classes du module dans l'espace global sans forcément en connaître les noms

import random # meilleure façon de faire, on importe tout le module, pas de confusion possible
