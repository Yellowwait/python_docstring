"""Les méthodes find() et index() permettent de trouver des mots ou des suites de caractères dans une str.
Cependant ces deux méthodes ne fonctionnent pas exactement de la même manière"""

a = "Bonjour le jour"

print(a.find("jour")) # renvoie 3 car la suite de caractères "jour" commence à l'indice 3 (partant de 0)
print(a.index("jour")) # idem pour cette méthode
print(a.rindex("jour")) # cheche depuis la fin de la str et renvoie 11 ici
print(a.rindex("jour")) # idem que rfind()

"""Cependant lorsque la suite de caractère n'est pas trouvée, les deux méthodes vont se comporter différemment"""

print(a.find("soir")) # renvoie -1 pour dire que la suite n'existe pas
print(a.index("soir")) # renvoie une erreur