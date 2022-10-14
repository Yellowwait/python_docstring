# Pour afficher le type d'un objet, on peut utiliser la fonction type()

d = "patate"
e = 420
f = 69.3
print(type(d)) # renvoie <class 'str'>
print(type(e)) # renvoie <class 'int'>
print(type(f)) # renvoie <class 'float'>

nombre = input("Veuillez entrer un nombre : ") # depuis Python 3, tout ce qui est entré dans une fonction input() est considéré comme un str
print(nombre) # ici on n'aura pas les guillemets et on peut alors penser que c'est un int
print(type(nombre)) # c'est là qu'on voit que nombre est bien un str