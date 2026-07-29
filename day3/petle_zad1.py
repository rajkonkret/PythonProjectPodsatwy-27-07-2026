# pętla - możliwośc wykonania kodu wielokrotnie
# for - pętla iteracyjna

for i in range(5):  # od 0 do 4
    print(i)

for i in range(20):
    pass  # nic nie rób

print(i)  # 19

for i in range(5, 10):
    print(i)
# 5
# 6
# 7
# 8
# 9

for _ in range(10):  # nie ma zmienna
    print("Test podłoga")
    print(_)  # 9

for i in range(5):
    print(i * 2)
    print(i + 2)

print("Wyjscie z pętli")

for i in range(10):
    if i % 2 == 0:
        print(i, "parzysta")

# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# lotto jako pętla
import random

lista_wyl = []

lista_kul = list(range(1, 50))

for _ in range(6):
    kula = random.choice(lista_kul)
    lista_kul.remove(kula)
    print(kula)
    lista_wyl.append(kula)
print(lista_wyl)
# [6, 43, 11, 14, 44, 18]

# parzyste do listy
lista3 = []
for i in range(10):
    if i % 2 == 0:
        lista3.append(i)
print(lista3)

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

# wypisac elementy z listy za pomoca for
for i in range(len(lista3)):  # pod i mamy index
    print(lista3[i])

for c in lista3:  # pod c kolejne elementy z lsity
    print(c)
# 0
# 2
# 4
# 6
# 8
