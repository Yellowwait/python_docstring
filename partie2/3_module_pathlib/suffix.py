"""La méthode suffix() permet de récupérer l'extension d'un fichier"""

from pathlib import Path

user_dir = Path.home()
main_file = user_dir / "Documents" / "main.py"

print((user_dir / "Documents" / "main.py").suffix) # renvoie l'extension .py
print(user_dir.joinpath("Documents", "main.py").suffix) # même résultat
print(main_file.suffix) # idem
print(user_dir / "Documents" / "main.py".suffix) # renvoie une erreur car les str n'ont pas de méthode suffix