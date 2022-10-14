liste = ["Thomas", "1", "4", "25", "Paul", "3", "Pierre"]

for element in liste:
    if element.isdigit():
        continue # ici on demande au script de continuer la boucle si la str est uniquement composée de chiffres
    print(element) # si elle tombe sur un élément qui n'est pas que des chiffres, la boucle affiche l'élément

for element in liste:
    if element.isdigit():
        break # ici, dès que la boucle rencontre un élément composée uniquement de chiffres, on lui demande de quitter la boucle
    print(element) # on n'affiche donc que le premier élément