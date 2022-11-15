from pathlib import Path

chemin = "/home/teste/Documents/Docstring/python_docstring/projets/createur_dossier/dossier_test"

dico = {"Films": ["Le Seigneur des Anneaux",
                  "Harry Potter",
                  "Moon",
                  "Forrest Gump"],
        "Employes": ["Paul",
                     "Pierre",
                     "Marie"],
        "Exercices": ["les_variables",
                      "les_fichiers",
                      "les_boucles"]}

for dossier_principal, sous_dossiers in dico.items(): # ici dossier_principal = Films, Employes, Exercices et sous_dossiers = Le Seigneur Des Anneaux, Harry Potter, etc.
    for dossier in sous_dossiers: # on boucle dans la liste sous_dossiers pour isoler chaque sous-dossier
        chemin_dossier = Path(chemin) / dossier_principal / dossier
        chemin_dossier.mkdir(exist_ok=True, parents=True)