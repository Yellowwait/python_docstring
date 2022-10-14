"""On peut parfois se retrouver face à des listes à l'intérieur de listes. Il est tout de même possible de récupérer chaque élément."""

liste = ["Python", ["Java", "C++", ["C"]], ["Ruby"]]

print(liste[1][0]) # renvoie "Java"
print(liste[1][-1]) # renvoie ['C'] (la liste)
print(liste[1][-1][0]) # renvoie "C" (l'élément de la liste)
print(liste[0][0]) # renvoie "P" de Python car une str est aussi une liste