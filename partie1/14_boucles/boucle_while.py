from pprint import pprint
import time

"""La boucle while exécute un code tant qu'une condition est True"""

i = 0

while i < 10: # cette boucle va donner le même résultat que celle en for à l'exception qu'on ne crée pas un range dont on ne se sert pas
    print("Bonjour")
    i += 1 # on incrémente de 1 jusqu'à ce que i = 10000

# while i < 10: # ATTENTION : boucle infinie car on incrémente pas i de 1 donc i < 10 = True tout le temps --> PLANTAGE
    # print("Marc")

continuer = "o"

while continuer.lower() == "o": # ici on ne sait pas à l'avance combien de fois va être répétée la boucle
    print("On continue...")
    continuer = input("Voulez-vous continuer ? o/n : ") # input() permet de mettre le script en pause en attendant de savoir si on répète la boucle"""

while True: # ici on souhaite avoir une boucle infinie car on veut que le script tourne en fonc
    print("Sauvegarde en cours...")
    time.sleep(5) # ici on définit un intervalle de temps en secondes, le script va s'exécuter toutes les 10 minutes

print(dir(time))
pprint(dir(time))
help(time.sleep)
