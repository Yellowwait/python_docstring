import random

a = random.randint(0, 100)
b = random.randint(0, 100)

if a > b:
    print("Le nombre a est plus grand que le nombre b.")
elif b > a:
    print("Le nombre b est plus grand que le nombre a.")
else:
    print("Le nombre a et le nombre b sont égaux.")

print(f"Le nombre a était : {a}")
print(f"Le nombre b était : {b}")