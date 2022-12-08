"""
Pour remédier à cela on peut par exemple créer une variable à l'intérieur de la fonction
"""

def foo(param):
    param = []
    param.append(4)
    print(param)

var = [1, 2, 3]

print(id(var))
foo(param=var)
print(var) # ici var ne sera 