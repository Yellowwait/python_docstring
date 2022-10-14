"""Il est possible d'écrire une structure for else"""

prenoms = ["Pierre", "Jean", "Patrick", "Marc"]

for prenom in prenoms:
    if prenom == "Patrick":
        print("Patrick a été trouvé !")
        break
else:
    print("Patrick est introuvable !")