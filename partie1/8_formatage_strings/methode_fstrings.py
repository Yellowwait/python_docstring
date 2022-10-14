"""Les f-strings permettent de s'affranchir des problèmes de concaténation en Python et notamment
l'addition de str et de int."""

prenom = "Jonathan"
print(f"Bonjour {prenom} !") # pour afficher une f-string il suffit de mettre un f avant l'ouverture des guillemets de la str à afficher

a = 5
b = 10
print(f"Le résultat de la multiplication de {a} par {b} est de {a * b}.") # ici plus besoin de la fonction str() pour convertir les int

# --------------------------

protocole = "https://"
nom_du_site = "Docstring"
extension = "fr"

url = f"{protocole}www.{nom_du_site.lower()}.{extension}"
print(url)

# --------------------------

liste = ["pommes", "poires", "bananes"]
print(f"Voici votre liste de courses : {liste}") # il est possible d'insérer des listes dans les f-string
print(f"Voici votre liste de courses : {', '.join(liste)}") # et même d'écrire du code