"""Voici comment récupérer les différentes clés et valeurs d'un dictionnaire"""


dico = {
    "prenom": "Paul",
    "profession": "Ingénieur",
    "ville": "Paris"
}

print(type(dico.keys())) # renvoie une liste de toutes les clés
print(type(dico.values())) # renvoie une liste de toutes les valeurs
print(type(dico.items())) # renvoie une liste de tuples contenant séparément chaque clé et la valeur qui lui est associée

"""Pour les clés"""

for key in dico.keys():
    print(key)

keys = dico.keys()
print(keys)

"""Pour les valeurs"""

for value in dico.values():
    print(value)

values = dico.values()
print(values)

"""On peut également procéder ainsi"""

for cle in dico:
    print(cle) # par défaut, ne renverra que les clés
    print(dico[cle]) # renvoie la valeur car cle prend successivement la valeur de chaque clé et renvoie la valeur associée

"""La méthode items() permet de renvoyer toutes les paires clé/valeur sous forme de tuples individuels"""

for cle, valeur in dico.items():
    print(f"{cle} : {valeur}")

print(dico.items())