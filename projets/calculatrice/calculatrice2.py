a = b = "" # on déclare deux variables

while not (a.isdigit() and b.isdigit()): # tant que a et b ne sont pas des nombres, on boucle
    a = input("Entrez un premier nombre : ") # on demande deux nombres à l'utilisateur
    b = input("Entrez un deuxième nombre : ")
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides.") # on affiche une phrase si au moins un des deux nombres entrés n'est pas valide

print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}") # on affiche le résultat de l'addition