"""Il est possible de continuer l'exécution d'un script même en cas d'erreur. Il existe deux méthodes : LBYL et EAFP"""

liste = [2, 4, "texte", 7]
liste2 = [2, 4, "texte", 7]

"""LBYL (Look Before You Leap) = regarde avant de sauter"""

for i in liste:
    if not str(i).isdigit(): # ici on passe en revue chaque élément de liste et si ça n'est pas un chiffre
        liste.remove(i) # on le retire de la liste

total = sum(liste)
print(total)

"""EAFP (Easier to Ask for Forgiveness than Permission) = plus facile de demander pardon que la permission"""

try:
    total2 = sum(liste2) # ici on tente de faire l'opération et si ça ne fonctionne pas
except:
    total2 = 0 # on renvoie une valeur par défaut

print(total2)