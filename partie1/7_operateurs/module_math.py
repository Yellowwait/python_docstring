"""De base, toutes les fonctions mathématiques ne sont pas chargées au lancement de Python. Pour cela, il faut importer un module"""

from cmath import pi
import math

print(math.ceil(4.7)) # renvoie l'entier supérieur --> 5
print(math.exp(2)) # renvoie l'exponentielle de 2 --> 7.38905609893065
print(math.factorial(5)) # renvoie la factorielle de 5 --> 120 (1 * 2 * 3 * 4 * 5)
print(math.floor(4.7)) # renvoie la partie entière --> 4
print(math.isinf(math.inf)) # renvoie True si isinf(x) est infini
print(math.log(2)) # renvoie le logarithme de 2 --> 0.6931471805599453 (inverse de la méthode factorial())
print(math.log(8, 2)) # renvoie le logarithme de 8 en base 2 --> 3.0
print(math.log10(2)) # renvoie le logarithme de 2 en base 10 --> 0.3010299956639812
print(math.pow(2, 3)) # renvoie 2 puissance 3 --> 8.0 (s'écrit aussi 2 ** 3)
print(math.sqrt(16)) # renvoie la racine carrée --> 4.0
print(math.pi) # renvoie le nombre pi --> 3.141592653589793
print(math.e) # renvoie le nombre d'Euler --> 2.718281828459045