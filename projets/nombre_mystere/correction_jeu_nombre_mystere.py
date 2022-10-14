from random import randint

nombre_mystere = randint(0, 100)
essais_restants = 5
nombre_essais = 1

print("*** Le jeu du nombre mystere ***")

while essais_restants > 0:
    print(f"Il te reste {essais_restants} essai{'s' if essais_restants > 1 else ''}.")

    guess = input("Devine le nombre : ")
    if not guess.isdigit():
        print("Merci d'entrer un nombre valide.")
        continue

    guess = int(guess)

    if guess > nombre_mystere:
        print(f"Le nombre mystère est plus petit que {guess}.")
    elif guess < nombre_mystere:
        print(f"Le nombre mystère est plus grand que {guess}.")
    else:
        break

    essais_restants -= 1
    nombre_essais += 1

if essais_restants == 0:
    print("Tu n'as plus d'essai !")
    print(f"Dommage, le nombre mystère était {nombre_mystere}.")
else:
    print(f"Bravo, le nombre mystère était bien {nombre_mystere} !")
    print(f"Tu as trouvé le nombre en {nombre_essais} essai{'s' if nombre_essais > 1 else ''}.")