"""Certaines méthodes, quand bien même elles font muer les objets, ne vont avoir aucun effet sur certains objets : ce sont des objets immuables."""

livre = "le seigneur des anneaux"
livre.title() # la méthode title() met une majuscule à la première lettre de chaque mot
print(livre) # pourtant la str n'est pas modifiée, c'est car les str sont des objets IMMUABLES, une copie est créée mais on affiche l'originale de livre
print("le seigneur des anneaux".title()) # ici une copie modifiée de la str est renvoyée par title() et affiche donc le résultat modifié