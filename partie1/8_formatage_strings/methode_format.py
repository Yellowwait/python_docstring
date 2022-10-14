"""Les f-string n'étant disponible que depuis Python 3.6, il faudra utiliser une autre méthode
sur les versions antértieures à la 3.6 : la méthode format"""

age = 30
phrase_fstring = f"J'ai {age} ans." # ici la version f-string
print(phrase_fstring)

phrase_format = "J'ai {} ans." # ici la version format()
print(phrase_format.format(age))

phrase2_format = "J'ai {a} ans." # on peut également ajouter un élément dans les accolades que l'on précisera en paramètre de format()
print(phrase2_format.format(a = 50))

phrase3_format = "J'ai {} ans et non pas {}." # il est possible de passer plusieurs valeurs en paramètres
print(phrase3_format.format(30, 25))

phrase4_format = "J'ai {0}, {0} ce n'est pas très vieux." # on passe l'indice 0 de format() qui est age pour ne pas avoir d'erreur (2 accolades et 1 argument)
print(phrase4_format.format(age))

prenom = "Jonathan"
age2 = 30
phrase5_format = "Je m'appelle {1} et j'ai {0} ans." # on peut inverser les indices : ici age sera affiché avant prenom
print(phrase5_format.format(prenom, age))

# ------------------------------

protocole = "https://"
nom_du_site = "Docstring"
extension = "fr"

url = "{}www.{}.{}".format(protocole, nom_du_site.lower(), extension)
print(url)

url2 = "{protocole}www.{domaine}.{extension}".format(protocole=protocole,
                                                     domaine=nom_du_site.lower(),
                                                     extension="fr")
print(url2)