"""La fonction range() renvoie un objet de type range correspondant à une liste de nombres"""

interval = range(10)
print(interval) # range(0, 10)
print(type(interval)) # <class 'range'>

"""Ces méthodes permettent de voir quels sont le début, le pas et la fin du range"""

print(interval.start) # renvoie 0 (par défaut)
print(interval.step) # renvoie 1 (par défaut)
print(interval.stop) # renvoie 10

"""Pour avoir le range sous forme de liste il suffit de procéder ainsi"""

interval = list(interval)
print(interval)