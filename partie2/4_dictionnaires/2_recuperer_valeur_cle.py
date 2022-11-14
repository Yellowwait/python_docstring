"""Voici comment récupérer la valeur d'une clé dans un dictionnaire"""

dictionnaire1 = {"prenom": "Jonathan",
                 "profession": "Développeur",
                 "ville": "Lyon"}

print(dictionnaire1["prenom"]) # on spécifie la clé pour récupérer la valeur correspondante

# On peut imbriquer plusieurs dictionnaires dans un seul dictionnaire. Ici chaque dictionnaire imbriqué est une valeur du dictionnaire parent et doit donc avoir aussi une clé.
liste_personnes = {
    0: {
        "prenom": "Paul",
        "profession": "Ingénieur",
        "ville": "Paris"
    },
    1: {
        "prenom": "Marc",
        "profession": "Forain",
        "ville": "Strasbourg"
    },
    2: {
        "prenom": "Marie",
        "profession": "Cuisinier",
        "ville": "Lyon"
    }
}

print(liste_personnes[1]["ville"])

# Une autre manière de récupérer une valeur est la méthode get(). Cette méthode ne renverra pas d'erreur si la clé n'existe pas dans le dictionnaire.

print(dictionnaire1.get("age", "La clé spécifiée n'existe pas")) # on peut spécifier un message si la clé n'a pas été trouvée (None par défaut) --> PREFERER CETTE METHODE !