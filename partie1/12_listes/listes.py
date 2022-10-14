"""Les listes permettent de stocker plusieurs valeurs dans un seul objet. Les listes sont des objets muables, càd qu'ils peuvent
être modifiés. On peut définir une liste vide et ajouter ou retirer des objets de cette liste."""

ma_liste = [250, "Python", True] # pour définir une liste on utilise des crochets. On peut stocker des données de types différents dans une seule liste.

mon_tuple = tuple(ma_liste) # pour transformer une liste en tuple on utilise la fonction tuple()
print(mon_tuple)

# liste avec trois éléments de type str
villes = ['Paris', 'Lille', 'Lyon']

# liste avec cinq éléments de type int
prix = [3, 10, 25, 40, 100]

# liste avec plusieurs éléments de types différents
liste_de_tout_et_rien = [5, 'Docstring', True, 9.5, 4, 'Python', ['autre liste'], False]

# liste qui contient un dictionnaire
adresse = [
    {
        'rue': 'rue du Serpent',
        'numero': 6,
        'ville': 'Lille'
    }
]