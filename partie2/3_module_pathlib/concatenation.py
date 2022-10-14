from pathlib import Path

user_dir = Path.home()
user_docs = user_dir / "Documents" # on peut concaténer facilement en ajoutant un slash et en précisant le nom d'un dossier entre guillemets
print(user_docs)
print(type(user_docs)) # <class 'pathlib.PosixPath'> --> l'objet reste de type PosixPath
