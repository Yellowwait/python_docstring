"""
Si on définit une fonction exécutant quelque chose, cette ligne sera exécuté à l'import du module. Python met les variables du module en mémoirte
mais si on a un print dans le module, celui-ci sera également exécuté à l'import. La constante __name__ permet de remédier à cela en n'exécutant les lignes
du module seulement si on l'exécute et pas seulement en l'important.

Ici __name__ = utils donc cela signifie qu'on est dans le script et pas dans le module donc on n'exécute pas le print du module
"""

import utils