from __future__ import print_function
from curses.ascii import isdigit


a = ""
b = ""

while not a.isdigit():
    a = input("Veuillez entrer un premier nombre : ")
a = int(a)
while not b.isdigit():
    b = input("Veuillez entrer un deuxième nombre : ")
b = int(b)
print("Le résultat de l'addition du nombre " + str(a) + " avec le nombre " + str(b) + " est égal à " + str(a+b))