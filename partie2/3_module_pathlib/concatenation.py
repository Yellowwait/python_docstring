"""
Grâce au module pathlib et à la classe Path, il est facile d'effectuer des concaténations sans risquer de se tromper.
"""

from pathlib import Path

user_dir = Path.home() # renvoie le chemin du dossier utilisateur
user_docs = user_dir / "Documents" # on peut concaténer facilement en ajoutant un slash et en précisant le nom d'un dossier entre guillemets
main_file = user_dir / "Documents" / "main.py" # on peut ajouter plusieurs dossiers et/ou fichiers

print(user_docs)
print(type(user_docs)) # <class 'pathlib.PosixPath'> --> l'objet reste de type PosixPat
print(main_file)

"""
Il y a également la méthode joinpath() qui permet d'avoir le même résultat
"""

user_docs2 = user_dir.joinpath("Documents")
main_file2 = user_dir.joinpath("Documents", "main.py")

print(user_docs2)
print(main_file2)

"""Enfin, on peut concaténer toute une liste de dossiers avec joinpath() et l'unpacking avec *"""

home = Path.home()
dossiers = ["Projets", "Django", "blog"]
dossier_blog = home.joinpath(*dossiers) # renvoie /home/teste/Projets/Django/blog