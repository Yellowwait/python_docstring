import random

nombre_mystere = random.randint(0, 101)
nombre_essais = 0
essais_restants = 6
guess = ""

print("*** Le jeu du nombre mystère ***")

while guess != nombre_mystere:
    while 1 < essais_restants <= 6:
        guess = int(input(f"""Il te reste {essais_restants - 1} essais \nDevine le nombre : """))
        essais_restants -= 1
        if guess > nombre_mystere:
            print(f"Le nombre mystère est plus petit que {guess}.")
        elif guess < nombre_mystere:
            print(f"Le nombre mystère est plus grand que {guess}.")
        if essais_restants == 1:
            print(f"Il te reste 1 essai\nDevine le nombre : ")
        elif essais_restants == 0:
            print(f"Dommage ! Le nombre mystère était {nombre_mystere}")
        elif guess == nombre_mystere:
            print(f"Bravo, le nombre était bien {nombre_mystere} !")
            break