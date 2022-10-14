import random

SANTE_JOUEUR = 50
SANTE_ENNEMI = 50
POTIONS = 3
PASSER_TOUR = False

while True:
    # Tour du joueur
    if PASSER_TOUR:
        print("Vous passez votre tour...")
        PASSER_TOUR = False
    else:
        choix_joueur = ""
        while choix_joueur not in ["1", "2"]:
            choix_joueur = input("Souhaitez-vous attaquer (1) ou boire une potion (2) ? ")
        # Attaque
        if choix_joueur == "1":
            attaque_joueur = random.randint(5, 10)
            SANTE_ENNEMI -= attaque_joueur
            print(f"Vous avez infligé {attaque_joueur} points de dégâts à l'ennemi ⚔")
        # Potion
        elif choix_joueur == "2":
            if POTIONS > 0:
                vie_potion = random.randint(15, 50)
                SANTE_JOUEUR += vie_potion
                POTIONS -= 1
                PASSER_TOUR = True
                print(f"La potion vous a ajouté {vie_potion} points de vie ❤")
            else:
                print("Vous n'avez plus de potion...")
                continue

    # Vérification santé ennemi
    if SANTE_ENNEMI <= 0:
        print("GAGNÉ ! Vous avez vaincu l'ennemi 💪")
        break

    # Tour de l'ennemi
    attaque_ennemi = random.randint(5, 15)
    SANTE_JOUEUR -= attaque_ennemi
    print(f"L'ennemi vous a infligé {attaque_ennemi} points de dégâts ⚔")

    # Vérification santé joueur
    if SANTE_JOUEUR <= 0:
        print("PERDU ! L'ennemi vous a vaincu 💀")
        break

    # Stats
    print(f"Il vous reste {SANTE_JOUEUR} points de vie ❤")
    print(f"Il reste {SANTE_ENNEMI} points de vie à l'ennemi 🖤")
    print(f"Il vous reste {POTIONS} 🧪")
    print("-" * 50)

print("Fin du jeu.")