"""Il est possible de configurer le logger pour n'afficher que certain niveaux de messages.
"""

import logging

# Pour afficher les logs à partir d'un autre niveau (défaut = WARNING), il faut modifier le paramètre level
# Le paramètre format permet de formater le message affiché (par défaut root)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("Permet de savoir ce que retourne notre script : la fonction a bien été exécutée !")
logging.info("À destination de l'utilisateur : message d'information générale.")
logging.warning("Avertissement : ne fait pas planter le script, pas le résulat escompté mais pas d'erreur critique.")
logging.error("Opération échouée mais le script continue de fonctionner.")
logging.critical("Erreur critique : le script ne fonctionne plus")