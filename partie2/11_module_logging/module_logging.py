"""Le module logging permet d'afficher des message d'avertissement ou d'erreur de manière plus avancée qu'avec un print. Il est dédié à ce type d'opérations.
Il existe 5 niveaux de messages à afficher.
"""

import logging

# Du moins au plus important
logging.debug("Permet de savoir ce que retourne notre script : la fonction a bien été exécutée !")
logging.info("À destination de l'utilisateur : message d'information générale.")
logging.warning("Avertissement : ne fait pas planter le script, pas le résulat escompté mais pas d'erreur critique.")
logging.error("Opération échouée mais le script continue de fonctionner.")
logging.critical("Erreur critique : le script ne fonctionne plus")