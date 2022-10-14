"""Les mots-clés any et all permettent respectivement de vérifier si toutes ou au moins une itération d'une compréhension de liste est vraie."""
# files = []

# all([f.endswith(".jpg") for f in files]) # permet de voir si tous les fichiers se terminent par l'extension ".jpg"

notes = [12, 14, 20, 10, 8]
print(any([x > 18 for x in notes])) # permet de vérifier si au moins une des notes est supérieure à 18

print("🍊")