# Il y a certaines particularités en terme de gestion de mémoire en Python. Par exemple le SINGLETON
print(id(True))
a = True
print(id(a)) # les deux id auront le même emplacement car "True" (comme "False" ou "none") est un "singleton", càd un objet unique

# Il y a une autre particularité pour les nombres allant de -5 à 256
b = 256
c = 256
d = 500
e = 500
print(id(b))
print(id(c)) # renvoie le même id car se situe dans la plage -5 à 256
print(id(d))
print(id(e)) # rennvoie deux id différents car en-dehors de la plage

# Une autre exception est les 