"""Pour retourner une valeur avec une fonction, on utilise l'instruction return."""

import os

def retour_cinq():
    return 5 # ici le seul but de la fonction est de retourner 5

a = retour_cinq()
print(a)

def retour_dix():
    return 10
    print("La fonction est terminée") # ici le code est dit "inatteignable" car return met fin à la fonction

"""L'instruction return met également fin à la fonction"""

def verifier_fichier():
    if os.path.exists("fichier.txt"):
        return True
    else: # on peut se passer de cette ligne puisque si la condition est vérifiée, le premier return mettra fin à la fonction
        return False

def verifier_fichier_court():
    if os.path.exists("fichier.txt"):
        return True
    return False

"""On peut encore simplifier puisque return nous renvoie un booléen par défaut"""

def verifier_fichier_plus_court():
    return os.path.exists("fichier.txt")

"""Si on n'utilise pas l'instruction return, une fonction va toujours retourner quelque chose de façon implicite. Il s'agit de l'objet None"""

def test():
    pass

a = test()
print(a) # retourne None