"""Comme pour les listes, il existe aussi des compréhensions de dictionnaires"""

dico = {
    'spam': 'ham',
    'knights': 'lumberjack',
    'bacon': 'sausage'
}

dico_pluriel = {k:v + "s" for k, v in dico.items()} # k(key) et v(value) à quoi on ajoute "s" pou
print(dico_pluriel)