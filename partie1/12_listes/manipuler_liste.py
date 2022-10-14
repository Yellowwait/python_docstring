"""Puisque les listes sont muables, il est possible d'ajouter ou de supprimer des éléments grâce à différentes méthodes."""

liste = [1, 2, 3]

# La méthode append() permet d'ajouter un seul élément à la fin d'une liste
liste.append(4)
print(liste)

# La méthode insert() permet d'ajouter un élément à un endroit souhaité en précisant l'indice
liste.insert(0, "Python")
print(liste)

# La méthode extend() permet d'ajouter plusieurs éléments à la fin d'une liste. Il faut cependant ajouter les éléments sous forme de liste
liste.extend([5, 6, 7])
print(liste)

# La méthode remove() permet de retirer l'élément passé en paramètre. Il faut préciser l'élément et PAS l'indice. Ne retire que que la première occurence
liste.remove(5)
print(liste)

# La méthode pop() permet de retirer l'élément passé en paramètre. Il faut préciser l'indice, PAS l'élément
liste.pop(0)
print(liste)

# Pour récupérer un élément d'une liste, on utilise les indices
langages = ["Python", "C++", "Java"]
print(langages[1]) # depuis la gauche on part de 0 donc C++ est l'indice 1
print(langages[-1]) # depuis la droite on part de -1 donc Java est l'indice -1