# La classe int() sert à convertir des objets en nombres entiers

print(int(5.658)) # renvoie uniquement ce qui se trouve avant le point et n'arrondit pas
print(int(True)) # True(1) et False(0) sont considérés comme une sous-classe des nombres entiers
print(int(1587))
print(int(-25))

# En revanche, ceci ne fonctionne pas

print(int("Bonjour"))
print(int(None))
print(int([1, 2, 3]))