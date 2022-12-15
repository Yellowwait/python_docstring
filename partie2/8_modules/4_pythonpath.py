"""Pour savoir quels modules sont disponibles à l'intérieur d'un script, Python va utiliser le PYTHONPATH. C'est une variable contenant des dossiers dans
lesquels Python va chercher des modules. On peut afficher cette variable grâce au module sys."""

import sys
import mon_module # on a créé ce module à cet emplacement "/usr/local/lib/python3.10/dist-packages" avec le terminal
from pprint import pprint

pprint(sys.path)
print(mon_module.a)

"""On retrouve à la première ligne le dossier courant du script exécuté, ce qui permet d'importer des modules se trouvant au même niveau.
Ce sont tous les chemins de dossiers dans lesquels on peut aller chercher des modules. On peut utiliser l'un de ces chemins dans le terminal et créer un
nouveau module dans l'un de ces dossiers et ensuite l'importer dans notre script"""