"""Les slices permettent de renvoyer des tranches de liste en spécifiant les indices de début, de fin mais également un pas entre ces deux indices"""

liste = ["Utlisateur_01",
         "Utlisateur_02",
         "Utlisateur_03",
         "Utlisateur_04",
         "Utlisateur_05",
         "Utlisateur_06",]

print(liste[0:2]) # l'indice avant le double-point est inclusif, celui d'après est exclusif
print(liste[:-1]) # renvoie toute la liste hormis le dernier élément
print(liste[2:]) # renvoie toute la liste depuis l'indice 2
print(liste[:]) # renvoie toute la liste
print(liste[::2]) # renvoie un élément sur deux en partant du début (le deuxième double-point correspond au pas)
print(liste[::-1]) # renvoie la liste mais dans l'ordre inverse (avec un pas de -1)