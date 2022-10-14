"""La méthode split() permet de séparer une string en plusieurs string en fonction des caractères passés en paramètres"""

a = "1, 2, 3, 4, 5"
print(a.split(", ")) # ici on retire chaque virgule + espace pour isoler chaque chiffre dans plusieurs strings
print(", ".join(a.split(", ")))
print(" | ".join(a.split(", ")))

b = ["1", "2", "3"]
print(" | ".join(b)) # la méthode join() permet de relier plusieurs string avec l'élément précisé entre guillemets AVANT la méthode