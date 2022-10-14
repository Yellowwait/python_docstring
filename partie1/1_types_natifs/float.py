print(3.2) # se comporte comme une string contenant un float. La classe float() sert à convertir des objets en nombre décimaux
print(float(3.2))
print(float("12.5"))
print(float(23)) # va transformer en float en ajoutant un .0

"""
Tout nombre avec un point et un chiffre derrière, même 0, est considéré comme un nombre décimal.
On peut le vérifier grâce à cette classe.
"""
print(isinstance(0.0, float))
print(isinstance(0.0, int))

# En revanche, ceci ne fonctionne pas

print(float("Bonjour"))
print(float(None))
print(float([1, 2, 3]))