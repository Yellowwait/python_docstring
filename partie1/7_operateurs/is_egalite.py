"""Il y a une différence entre l'opérateur d'égalité (==) et le mot-clé "is"
L'opérateur d'égalité sert à vérifier l'égalité des VALEURS contenues dans les variables.
Le mot-clé "is" permet de vérifier si deux objets sont les mêmes en mémoire."""

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # renvoie True car a et b contiennent les mêmes valeurs
print(a is b) # renvoie False car a et b sont deux objets différents

print(id(a)) # on peut le vérifier grâce à la méthode id()
print(id(b)) # a et b sont deux objets différents et ont donc deux adresses différentes en mémoire