import json

# with open("erreurs.json", "r") as f:
#     contenu = json.load(f)
#     print(contenu) # json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0) --> lorsque le fichier est vide

with open("erreurs.json", "w") as f:
    json.dump("Pèche", f, ensure_ascii=True) # renvoie "P\u00e8che" si on n'ajoute pas le ensure-ascii:False