"""Voici les erreurs courantes à éviter lorsqu'on manipule des dictionnaires"""

# Pour créer ou modifier une clé existante, on ne peut pas utiliser la méthode get()
dico = {"prenom": "Julie"}
dico["nom"] = "Thomas" # OK
dico.get("age") = 25 # ERREUR