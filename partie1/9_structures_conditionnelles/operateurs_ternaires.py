"""Les opérateurs ternaires permettent de simplifier une structure conditionnelle afin de l'écrire sur une seule ligne."""

age = int(input("Entrez votre âge : "))

if age >= 18:
    majeur = True
else:
    majeur = False

# ici on a besoin de 4 lignes de code pour définir si majeur est True ou False alors qu'on peut l'écrire ainsi en une seule ligne

majeur = True if age >= 18 else False

# Cependant cela fonctionne uniquement avec une structure if else et pas avec if elif else