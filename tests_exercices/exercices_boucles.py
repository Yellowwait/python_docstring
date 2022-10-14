for i in range(1, 11):
    print(f"Utilisateurs {i}")

# --------------------------------

mot = "Python"
for lettre in reversed(mot):
    print(lettre)

mot2 = "Alcool"
for lettre in mot2[::-1]:
    print(lettre)
# --------------------------------

mot = "Python"
for i in range(len(mot)):
    print(i)

# --------------------------------

nombre = 7

for i in range(11):
    print(f"{i} x {nombre} = {i * nombre}")

# --------------------------------

i = 0

while i < 10:
    pass
    i += 1

print("Sortie de boucle")

# --------------------------------

continuer = "o"

while continuer == "o":
    print("On continue !")
    input("Continuer ? o/n ")