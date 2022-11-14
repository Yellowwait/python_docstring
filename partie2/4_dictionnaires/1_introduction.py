"""
Les dictionnaires permettent, comme les listes, de stocker plusieurs valeurs. Mais contrairement aux listes, ils permettent d'accéder aux valeurs grâce à une clé
et non pas grâce à un indice.
"""

# ici les clés sont avant le double-point et les valeurs sont après. Les clés sont UNIQUES, il ne peut y en avoir deux du même nom dans un même dictionnaire
dictionnaire = {"prenom": "Thomas",
                "age": "25",
                "profession": "forain"}

# On peut également stocker plusieurs dictionnaires dans un même dictionnaire
liste_personnes = {
                    "Un": {
                        "prenom": "Paul",
                        "profession": "Ingénieur",
                        "ville": "Paris"
                    },
                    "Deux": {
                        "prenom": "Julie",
                        "profession": "Architecte",
                        "ville": "Marseille"
                    },
                    "Trois": {
                        "prenom": "Pierre",
                        "profession": "Plombier",
                        "ville": "Nantes"
                    }
                  }
print(liste_personnes["Trois"]["ville"])

# Les clés doivent obligatoirement être des objets immuables mais peuvent être de n'importe quel type
d = {
        1: 'one', # int
        'deux': 2 , # str
        (3, 4, 5): 'pas_de_soucis', # tuple
        9.9: 'nine_point_nine' # float
}

# Si l'on crée deux clés identiques, la seconde écrasera la première
d2 = {
        'spam': 'eggs', 
        'knights': 'lumberjack', # 1ère clé 'knights'
        'bacon': 'sausage',
        'knights': 'ham' # 2ème clé 'knights' qui va écraser la première
}

print(d)