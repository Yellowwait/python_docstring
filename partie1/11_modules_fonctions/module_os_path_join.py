import os

chemin = "D:\Docstring"
dossier = os.path.join(chemin, "dossier", "test")
os.makedirs(dossier, exist_ok=True) # le paramètre exist_ok=True permet de ne pas faire planter le script si le chemin existe déjà

if not os.path.exists(dossier): # comme exist_ok=True mais sous forme de structure conditionnelle
    os.makedirs(dossier)

if os.path.exists(dossier): # ici il n'existe pas d'argument comme exist_ok=True, si le dossier existe on le supprime, sinon rien
    os.removedirs(dossier)

# print(dossier)


"""
La fonction os.path.join() va permettre de concaténer un chemin de dossier déjà existant avec un nom de dossier que l'on souhaite créer.
Elle va automatiquement ajouter le séparateur approprié en fonction de l'OS (/ sur MacOS et Linux et \ sur Windows).
Elle ajoute ce séparateur à la fin de chaque élément. Si à la place de "dossier", on avait eu "", le chemin final aurait été D:\Docstring\
NE PAS FAIRE DE CONCATÉNATION = PROBLÈME
"""

"""
La fonction os.makedirs() permet de créer plusieurs dossiers et sous-dossiers qui n'existent pas --> D:\Docstring\dossier\test
La fonction os.mkdir() ne permet de créer qu'un seul dossier à la fois --> D:\Docstring\dossier (erreur s'il y a test en plus)
"""