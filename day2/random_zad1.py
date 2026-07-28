import random

# działania na liczbach losowych
"""Return random integer in range [a, b], including both end points.
 """
print(random.randint(1, 100))  # int od 1 do 100

print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # int od 0 do 4

print(random.random())  # 0.16289821245163705 float od 0 do 0.9999999
print(random.random() * 7)  # 1.1609510548715591 float od 0 do 6.99999999

lista = ["Radek", 'Tomek', "Zenek", "Ania", "Kasia"]
print(lista[random.randrange(len(lista))])  # Kasia

print(random.choice(lista))  # Radek, losuje jeden element

lista_kul = list(range(1, 50))
# print(lista_kul)
kula = random.choice(lista_kul)
lista_kul.remove(kula)
print(kula)

print(random.choices(lista_kul, k=6))  # [7, 46, 3, 47, 48, 46], z powtórzeniami
# [15, 44, 45, 41, 18, 35]

print(random.sample(lista_kul, k=6))
print(random.sample(lista_kul, 6))
# [16, 38, 27, 20, 2, 29]
# [28, 35, 12, 20, 29, 39]
# [29, 9, 48, 20, 12, 18]
