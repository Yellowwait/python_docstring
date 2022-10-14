"""Les compréhensions de liste permettent d'itérer et de filtrer les éléments grâce à des structures conditionnelles en une seule ligne."""

liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombres_positifs = []

for i in liste: # grâce à cette structure on peut ajouter tous les nombres positifs à la liste nombres_positifs
    if i > 0:
        nombres_positifs.append(i)

print(nombres_positifs)

nombres_negatifs = [i for i in liste if i < 0] # ici en une seule ligne on récupère tous les nombres négatifs
nombres_negatifs_double = [i * 2 for i in liste if i < 0] # ici on peut avoir un double des nombres dans la liste
print(nombres_negatifs)
print(nombres_negatifs_double)