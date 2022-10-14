"""Les structures conditionnelles permettent d'exécuter un code en fonction de si une condition est remplie ou non."""

age = int(input("Entrez votre âge : "))

if age < 18: # SI age est strictement inférieur à 18
    print("Vous êtes un enfant !") # on affiche cette phrase
elif age <= 70: # SINON SI age est inférieur ou égal à 70
    print("Vous êtes un adulte !") # on affiche cette autre phrase
else: # SINON, dans tout autre cas de figure
    print("Vous êtes une personne agée !") # on affiche cette phrase