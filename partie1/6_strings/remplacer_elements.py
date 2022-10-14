"""# Certaines méthodes permettent de remplacer des éléments d'une string"""

a = "Bonjour, nous sommes le jour"
b = "Coucou coucou"
print(a.replace("jour", "soir")) # replace() permet de remplacer un ou plusieurs caractères par d'autres caractères
print(b.replace(" ", "")) # ici on remplace l'espace par un vide donc on supprime l'espace entre les deux mots
print(b.replace("ou", "a").replace(" ", "")) # on peut aussi enchainer les replace()

c = "  bon  jour  "
print(c.strip())
"""La méthode strip() analyse chaque caractère depuis le début (gauche) et retire ceux qui sont passés en paramètres
puis fait pareil depuis la fin (droite). Dès qu'elle croise un caractère non passé en paramètre, elle s'arrête (espace par défaut).
Puis fait la même chose depuis la droite de la string"""

print(c.strip(" bjor")) # renvoie "n  jou"
print(c.rstrip(" ujor")) # même opération que strip() mais seulement depuis la droite
print(c.lstrip(" ujor")) # même opération que strip() mais seulement depuis la gauche