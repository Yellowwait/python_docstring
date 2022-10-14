"""Les opérateurs d'appartenance permettent de renvoyer un booléen en fonction de si un élément se trouve dans une liste, un tuple, une str etc."""

utilisateurs = ["Paul", "Pierre", "Marie"]
print("Paul" in utilisateurs) # renvoie True
print("Thomas" not in utilisateurs) # renvoie True également

if "Paul" in utilisateurs:
    print("Bonjour Paul, bon retour parmi nous !")

if "Marie" in utilisateurs:
    utilisateurs.remove("Marie") # permet de prévenir les erreurs au cas où l'élément ne serait pas dans la liste

print("Java" in "Javascript") # on peut aussi vérifier qu'une str se trouve dans une autre str