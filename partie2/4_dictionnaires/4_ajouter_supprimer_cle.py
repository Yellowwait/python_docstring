"""Voici comment ajouter et supprimer une clé dans un dictionnaire"""

# Pour ajouter une clé
dico = {
    "prenom": "Paul",
    "profession": "Ingénieur",
    "ville": "Paris"
}

dico["age"] = 30 # Si la clé n'existe pas déjà elle est créée. ATTENTION, si elle existe déjà, elle est écrasée par la nouvelle
print(dico)

# Supprimer une clé avec del
# del dico["nom"] # renvoie une erreur car la clé n'existe pas 

if "nom" in dico:
    del dico["nom"] # ne revoie pas d'erreur car n'essaie pas de supprimer pas la clé si elle n'existe pas

# Pour supprimer une clé et récupérer sa valeur on utilise pop
d = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}

item = d.pop('knights') # 'lumberjack'
print(d)
print(item)

# popitem() supprime le dernier élément et renvoie un tuple contenant sa clé et sa valeur
item2 = d.popitem()
print(item2)

# clear() permet de vider le dictionnaire
d.clear()
print(d)