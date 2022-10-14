"""La méthofde zfill() permet de remplir de zéros une str"""

a = "19"
print(a.zfill(4)) # affiche "0019", 4 étant la longueur de la str

for i in range (101):
    print(str(i).zfill(3))