"""Les defaultdict sont des dictionnaires avec des valeurs par défaut. Il n'y a donc jamais de KeyError"""

from collections import defaultdict

langages_programmation = defaultdict(lambda: "Python") # ici lambda permet de définir la valeur par défaut

langages_programmation[".js"] = "JavaScript"
langages_programmation[".php"] = "PHP"

print(langages_programmation[".js"]) # renvoie "JavaScript"
print(langages_programmation[".php"]) # renvoie "PHP"
print(langages_programmation[".json"]) # n'existe pas donc renvoie la valeur par défaut "Python"