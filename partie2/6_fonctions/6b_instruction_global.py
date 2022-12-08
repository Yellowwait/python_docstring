"""L'instruction global permet à une fonction de modifier la valeur d'une variable définie en-dehors de celle-ci. A NE PAS UTILISER."""

def get_comment(note):
    global commentaire # ici on indique que l'on ne veut pas créer de variable locale mais qu'on veut utiliser la variable globale commentaire (NE PAS FAIRE !!!)
    if note > 15:
        commentaire = "Bravo !"
    elif note > 10:
        commentaire = "Peut mieux faire..."
    elif note > 5:
        commentaire = "Attention !"

commentaire = "Tu as tout faux !" # ici la fonction est impure car on a une fonction qui modifie des variables en-dehors de la fonction
get_comment(20)
print(commentaire)