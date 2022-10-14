from audioop import reverse


employes = ["Carlos", "Max", "Martine", "Patrick", "Alex", "Max"]
chiffres = [23, 5, 41, 999, 78]
resultat = employes.index("Alex")
compte = employes.count("Max")
tri = employes.sort()
employes.sort()
print(employes)
tri2 = sorted(chiffres)
employes.reverse()
print(f"Reverse : {employes}") # renvoie la liste dans l'ordre inverse

print(resultat) # renvoie l'indice de Alex
print(compte) # renvoie le nombre d'occurrences du paramètre passé
print(tri) # renvoie None car la méthode sort() trie directement la liste mais renvoie None dans la variable
print(tri2) # la méthode sorted() permet de renvoyer le résultat du tri à une variable contrairement à sort()