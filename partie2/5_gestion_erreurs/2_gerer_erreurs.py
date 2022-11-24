"""Voici comment rédiger un bloc try except"""

a = 5
b = 10

try:
    resultat = a / b
except ZeroDivisionError: # on peut spécifier chaque type d'erreur
    print("Division par zéro impossible.")
except TypeError:
    print("La variable n'est pas du bon type.")
except NameError as e:
    print("Erreur :", e)
else: # si aucune erreur n'est levée, on passe dans le else
    print(resultat)
finally: # optionnel mais finally est exécuté quel que soit le résultat
    print("Fin du bloc")