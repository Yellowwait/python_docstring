"""Voici comment récupérer les différentes clés et valeurs d'un dictionnaire"""


dico = {
    "prenom": "Paul",
    "profession": "Ingénieur",
    "ville": "Paris"
}

print(type(dico.keys())) # renvoie une liste de toutes les clés
print(type(dico.values())) # renvoie une liste de toutes les valeurs
print(type(dico.items())) # renvoie une liste de tuples contenant séparément chaque clé et la valeur qui lui est associée

for cle in dico:
    print(cle) # par défaut, ne renverra que les clés
    print(dico[cle]) # renvoie la valeur car cle prend successivement la valeur de chaque clé et renvoie la valeur associée

for cle, valeur in dico.items():
    print(f"{cle} : {valeur}")

print(dico.items())