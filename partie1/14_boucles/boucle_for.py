"""La boucle for permet de passer, par exemple, en revue une liste"""

liste = [1, 3, 5, 7, 9]
mot = "Python"

for i in liste:
    print(i)

for letter in mot: # quand on applique la boucle for à une str, elle passe en revue chaque caractère de la str
    print(letter)

for i in range(10000): # en créant une liste de nombres gigantesque avec range() on peut répéter une action un très grand nombre de fois
    print("Olélélolo")