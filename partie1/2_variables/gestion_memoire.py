from re import A


a = 5
b = a

print(id(a)) # la commande fonction id() nous permet de voir quel emplacement en mémoire occupe la variable a
print(id(b)) # a et b on le même emplacement car elles pointent tous les deux vers le même objet (et non pas deux objets de valeur 5)

a = 3

print(id(a)) # ici on voit que l'emplacement n'est plus le même car on a changé la valeur de a et donc le 5 n'est plus gardé en mémoire par le ramasse-miettes