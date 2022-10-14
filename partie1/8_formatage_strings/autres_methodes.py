"""Cette méthode est obsolète mais on la retrouve encore dans de nombreux scripts car elle a longtemps été la manière
privilégiée de formater des str. Elle peut cependant devenir illisible très rapidement car très verbeuse. Elle a également
des problèmes pour afficher les tuples et les dictionnaires."""

prenom = "Jonathan"
age = 30
moyenne = 16.5
phrase = "Bonjour, je m'appelle %s, j'ai %d ans et une moyenne de %f." % (prenom, age, moyenne)

print(phrase)

personne = {
    "nom": "Jonathan",
    "age": 30,
    "ville": "Strasbourg"
}
print("Bonjour {1}, vous avez {2} ans et vous habitez à {0}.".format(personne["ville"], personne["nom"], personne["age"]))
print("Bonjour {nom}, vous avez {age} ans et vous habitez à {ville}.".format(ville=personne["ville"], nom=personne["nom"], age=personne["age"]))
print("Bonjour {nom}, vous avez {age} ans et vous habitez à {ville}.".format(**personne)) # les ** vont "unpack" le dictionnaire et faire correspondre les entrées

