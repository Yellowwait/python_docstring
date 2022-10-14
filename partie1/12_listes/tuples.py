"""De la même manière que les listes, on peut créer des tuples. La seule différence avec les listes c'est que les tuples sont immutables.
Ils ne peuvent donc pas être modifiés. L'avantage avec les tuples c'est qu'ils prennent moins de place en mémoire car moins d'opérations sont possibles.
Si l'on sait que l'on va créer des objets que l'on ne souhaite pas modifier, il est préférable d'utiliser des tuples."""

mon_tuple = (250, "Python", True) # pour créer un tuple, on utilise la même syntaxe que les listes mais avec des parenthèses à la place des crochets

ma_liste = list(mon_tuple) # pour transformer un tuple en liste on utilise la fonction list()
print(ma_liste)

"""Pour créer un tuple qui ne contient qu'un item, il faut le faire suivre d'une virgule, sinon il sera considéré comme le type de donnée entré."""

t = ("spam")
print(type(t)) # class "str"

t2 = ("spam",)
print(type(t2)) # class "tuple"

"""On peut également unpack un tuple, récupérer chaque valeur du tuple dans différentes variables de cette manière. Il faut faire attention cependant
à ce qu'il y ait autant de variables à assigner que de nombre d'objets dans le tuples """

t3 = ("spam", "eggs")
v1, v2 = t3
print(v1) # "spam"
print(v2) # "eggs"

"""Les tuples sont des objets immutables. Cependant, il est tout de même possible de modifier les objets mutables à l'intérieur du tuple"""

t4 = ('spam', 'eggs', [1, 2, 3], 'knights')
# t4[0] = "lumberjack" # renvoie une erreur
t4[2][1] = 5 # change le 2 en 5 car il est dans une liste qui est un objet mutable
print(t4)

"""Il est impossible de supprimer l'un des objets d'un tuple. En revanche il est possible de supprimer un tuple avec l'instruction del """

t5 = ('spam', 'eggs', 'knights', 'lumberjack')

# del t5[0] # renvoie une erreur
del t5 # supprime entièrement le tuple t5