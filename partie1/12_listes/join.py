from pprint import pprint

liste = ["Python", "est", "un", "langage", "incroyable."]
resultat = " ".join(liste) # on pourrait vouloir faire liste.join(" ") mais il faut appliquer la méthode join au caractère et non pas à la liste
resultat2 = "\n".join(liste)
resultat3 = "_".join(liste)
print(resultat)
print(resultat2) # équivalent à pprint
print(resultat3) # pour les noms de fichiers