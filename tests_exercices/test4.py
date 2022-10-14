liste = range(10) # on crée une liste de 10 nombres

for i in liste:
    if i % 2 == 1: # si le reste de la division est égal à 1
        continue # on passe
    print(i) # on n'affiche que les nombres dont le reste de la division par 2 est égal à 0 --> nombres pairs