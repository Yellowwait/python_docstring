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
                    {
                        "prenom": "Paul",
                        "profession": "Ingénieur",
                        "ville": "Paris"
                    },
                    {
                        "prenom": "Julie",
                        "profession": "Architecte",
                        "ville": "Marseille"
                    },
                    {
                        "prenom": "Pierre",
                        "profession": "Plombier",
                        "ville": "Nantes"
                    }
                  }
