"Lorsqu'un fichier __init__ est présent dans un package, celui-ci va être exécuté en premier avant l'import des modules du package"

import utils
import sys

utils.users.get_users()


# users.get_users() # ne fonctionne pas car il faudrait importer utils.users