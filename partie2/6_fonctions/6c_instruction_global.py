"""Pour ne pas avoir à se servir de global, il suffit d'organiser son code autrement (ne pas définir de valeur par défaut en-dehors de la fonction"""

note = int(input("Note : "))

def get_comment(note):
    if note > 15:
        commentaire = "Bravo !"
    elif note > 10:
        commentaire = "Peut mieux faire..."
    elif note > 5:
        commentaire = "Attention !"
    else:
        commentaire = "Tu as tout faux !" # on supprime la variable globale et on ajoute un else

    return commentaire # on retourne la valeur de commentaire

commentaire = get_comment(note) # on récupère la valeur dans une variable en-dehors de la fonction
print(commentaire)