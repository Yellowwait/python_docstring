# Voici les erreurs à éviter

75Paris = 1 # ERREUR car ne doit pas commencer par un chiffre
Site-Web = 1 # ERREUR car le tiret (-) n'est pas un caractère autorisé
~lien video = 1 # ERREUR car contient un caractère non autorisé et un espace
True = 1 # ERREUR car True est un mot réservé

# Les voici corrigées mais ne respectant toujours pas les conventions

Paris75 = 1 # /!\ on met le chiffre à la fin mais contient une majuscule au début
Site_Web = 1 # /!\ on remplace le tiret (-) par un underscore (_) mais toujours des majuscules
lienVideo = 1 # /!\ on enlève le caractère non autorisé mais toujours une majuscule
true = 1 # /!\ on enlève la majuscule mais confusion possible avec True

# Les voici respectant les conventions

paris_75 = 1 # OK
site_web = 1 # OK
lien_video = 1 # OK
vrai = 1 # OK

# Dernier point : Python est sensible à la casse donc ces deux variables seront distinctes

prenom = 1
Prenom = 1

# Il convient également d'éviter d'utiliser les accents pour les noms de variables même si cela ne renvoie plus d'erreur depuis Python 3