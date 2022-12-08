"""L'instruction global permet à une fonction de modifier la valeur d'une variable définie en-dehors de celle-ci. A NE PAS UTILISER."""

def get_comment(note):
    if note > 15:
        commentaire = "Bravo !"
    elif note > 10:
        commentaire = "Peut mieux faire..."
    elif note > 5:
        commentaire = "Attention !"

commentaire = "Tu as tout faux !" # valeur de commentaire "par défaut"
get_comment(20) # ici on pourrait s'attendre à modifier la valeur de commentaire en "Bravo !"
print(commentaire) # en fait on a "Tu as tout faux !" car on a créé une variable commentaire locale à la fonction donc print regarde d'abord dans son propre espace local (= global) où commentaire = "Tu as tout faux"