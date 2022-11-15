from pprint import pprint

with open("/home/teste/Documents/Docstring/python_docstring/projets/organiser_donnees/prenoms.txt", "r") as f: # on ouvre le fichier en mode lecture
    lines = f.read().splitlines() # on n'utilise pas f.readlines() pour ne pas avoir les \n affichés. Ici c'est comme si on faisait un split sur \n donc il n'apparaît pas (crée une liste)

prenoms = [] # on crée une liste vide qui va accueillir chaque prénom individuellement

for line in lines: # on passe en revue chaque ligne de la liste lines
    prenoms.extend(line.split()) # par défaut split() s'effectue sur l'espace et on ajoute tout à la liste prenoms grâce à extend()

prenoms_final = [prenom.strip(",. ") for prenom in prenoms] # on retourne chaque prénom sans ",. " pour chaque prénom de la liste prenoms
# prenoms_final.sort() # on trie les prénoms par ordre alphabétique

with open("/home/teste/Documents/Docstring/python_docstring/projets/organiser_donnees/prenoms.txt", "w") as f: # on ouvre le fichier en mode écriture
    f.write("\n".join(sorted(prenoms_final))) # on écrit la liste de prénoms triés (sort plus haut ou sorted à la fin) et on les joint par un saut de ligne