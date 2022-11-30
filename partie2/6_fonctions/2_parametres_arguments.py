"""Ici nous allons voir comment passer des paramètres et des arguments à une fonction. Il faut bien faire la différence entre ces deux termes"""

def afficher(message): # lorsqu'on définit une fonction, ce que l'on écrit entre les parenthèses est appelé PARAMETRE
    print(message)

afficher("Bonjour") # au moment de l'appel de la fonction, on passe un ou plusieurs ARGUMENTS à la fonction. Ici l'argument "Bonjour" va être récupérer dans le paramètre message de la fonction afficher

"""Il faut bien faire attention à passer des paramètres aux fonctions qui en attendent sous peine de provoquer une erreur. On dit que le paramètre message est "obligatoire"""

# afficher() # provoque une erreur TypeError

"""Il est possible de définir une valeur par défaut à un paramètre dans l'éventualité ou celui-ci ne serait pas précisé au moment de l'appel de la fonction"""

def afficher_defaut(message="Message par défaut"):
    print(message)

afficher_defaut()
afficher_defaut("Lacoste TN") # ici l'argumebt passé prime sur le message par défaut

"""On peut passer autant de paramètres que l'on veut à une fonction"""

def division(a, b):
    return a / b

print(division(10, 5)) # par défaut, Python assigne les valeurs des arguments dans l'ordre des paramètres tels qu'ils ont été définis dans la fonction au départ
print(division(b=10, a=5)) # il est possible de modifier la valeur des arguments au moment de l'appel de la fonction