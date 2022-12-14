"""Voici la syntaxe des annotations de type (à noter qu'elles sont toutes facultatives"""

def add(a: int = 1, b: int = 2) -> int: # les valeurs par défaut s'il y en a sont à noter après le type de variable attendu
    return a + b

"""Un autre exemple plus complexe"""

def foo(a: list[int], b: list[int]) -> list[str]:
    return [1, 2, 3] # VSCode est censé souligner en rouge car le type retourné ne correspond pas au type attendu dans la définition de la fonction

foo()