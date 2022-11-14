"""Voici comment réassigner une valeur à une clé dans un dictionnaire"""

dico = {
    "prenom": "Paul",
    "profession": "Ingénieur",
    "ville": "Paris" # valeur initiale
}

dico["ville"] = "Strasbourg" # nouvelle valeur
print(dico["ville"])
print(dico.get("profession"))
print(dico.get("age"))