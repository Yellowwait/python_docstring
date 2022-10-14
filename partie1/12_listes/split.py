"""La méthode split() permet de séparer une str sur un ou plusieurs caractère et d'en récupérer une liste."""

courses = "Riz, Pommes, Lait, Salade, Saumon, Beurre" # ici on a une str
courses.split(", ") # ici on choisit les caractères sur lesquels spliter la str
print(courses) # on voit ici que la liste ne change pas car split() ne modifie pas directement la liste
courses_liste = courses.split(", ")
print(courses_liste) # il faut écraser la variable courses ou en créer une nouvelle pour pouvoir afficher la liste splitée
courses_liste2 = courses.split("-")
print(courses_liste2) # si on précise un paramètre qui n'existe pas, split() nous renvoie une liste mais avec un seul élément