fichier = input("Entrez le chemin du fichier à ouvrir : ")

try:
    with open (fichier, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Le fichier est introuvable.")
except UnicodeDecodeError:
    print("Impossible de lire le fichier.")
else:
    f.close()
finally:
    print("Terminé ✅")