"""Il existe 3 opérateurs logiques : AND, OR et NOT"""

utilisateur = input("Entrez le nom d'utilisateur : ")
mot_de_passe = input("Entrez le mot de passe : ")

if utilisateur and mot_de_passe == "admin": # Avec AND, il faut que toutes les conditions soient True pour que le code soit exécuté
    print("Accès autorisé !")
else:
    print("Accès refusé !")

a = 5

if a > 2 and a > 10: # Ici les deux conditions doivent être remplies pour exécuter le code
    print("Toutes les conditions sont remplies")

b = 12

if b > 5 and b > 20 or b == 12: # Avec OR, seule une condition remplie suffit pour exécuter le code
    print("L'une ou l'autre des conditions est remplie, c'est OK !")

# --------------------------

"""

TRUE and TRUE = TRUE
TRUE and FALSE = FALSE
FALSE and TRUE = FALSE
FALSE and FALSE = FALSE

TRUE or TRUE = TRUE
TRUE or FALSE = TRUE
FALSE or TRUE = TRUE
FALSE or FALSE = FALSE

"""

# --------------------------

utilisateur2 = input("Veuillez entrer un autre nom d'utilisateur : ")

if not utilisateur2 == "admin": # si utilisateur2 n'est PAS égal à admin exécuter le code
    print("Accès refusé")