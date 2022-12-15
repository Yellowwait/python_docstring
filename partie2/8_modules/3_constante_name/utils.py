"""Dans le module __name__ == __main__ et dans le script où l'on import le module, __name__ == nomdumodule"""

def addition(a, b):
    return a + b

if __name__ == "__main__":
    print(addition(4, 5)) # ici __name__ == __main__ donc exécution du code