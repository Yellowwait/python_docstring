for note in range(20):
    if note < 3 :
        print("Sans commentaire...")
    elif note >= 3:
        print("Tu n'as rien compris !")
    elif note > 6 :
        print("Il faut tout revoir...")
    elif note > 10 :
        print("Peut mieux faire.")
    elif note > 14 :
        print("Bon travail !")
    elif note >= 18 and note < 20:
        print("Excellent !!")
    elif note == 20:
        print("C'est un sans faute !")

# -------------------

"""for note in range(20):
    if note < 3 :
        print("Sans commentaire...")
    elif note >= 18 and note < 20:
        print("Excellent !!")
    elif note == 20:
        print("C'est un sans faute !")
    elif note > 14 :
        print("Bon travail !")
    elif note > 10 :
        print("Peut mieux faire.")
    elif note > 6 :
        print("Il faut tout revoir...")
    elif note >= 3:
        print("Tu n'as rien compris !")
    note += 1"""