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

lista_nazwy = ["Ala", "Tomek", "Zenek", "Basia"]

for p in lista_nazwy:
    print(p)

# Ala
# Tomek
# Zenek
# Basia

for c in lista3:
    if c > 4:
        print(c, "Większe niż 4")
    elif c == 4:
        print(c, "Równa 4")
    else:
        print(c, "Mniejsze niż 4")
    print(c)  # za każdym przejściem pętli

print("Po zakońćzeniu pętli")
# 4 Równa 4
# 4
# 6 Większe niż 4
# 6
# 8 Większe niż 4
# 8
# Po zakońćzeniu pętli

for i in range(-10, 0):
    print(i)

for i in range(-10, 0, 2):
    print(i)

for i in range(10, 0, -2):  # (start, stop, krok)
    print(i)

lista_nazwy = ["Ala", "Tomek", "Zenek", "Basia"]

for o in lista_nazwy:
    print(o)
# Ala
# Tomek
# Zenek
# Basia

# 0 Ala
for i in range(len(lista_nazwy)):
    print(i, lista_nazwy[i])
# 0 Ala
# 1 Tomek
# 2 Zenek
# 3 Basia

for i in lista_nazwy:
    print(lista_nazwy.index(i), i)
# 0 Ala
# 1 Tomek
# 2 Zenek
# 3 Basia

# enumerate() - zwraca numer i element kolekcji
for p in enumerate(lista_nazwy):
    print(p)
# (0, 'Ala')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Basia') -> 3 Basia

a, b = (3, 'Basia')
print(a, b)  # 3 Basia

for i, o in enumerate(lista_nazwy):
    print(i, o)
# 0 Ala
# 1 Tomek
# 2 Zenek
# 3 Basia

for i, o in enumerate(lista_nazwy, start=1):
    print(i, o)
# 1 Ala
# 2 Tomek
# 3 Zenek
# 4 Basia

# imiona = ["Ala", "Tomek", "Zenek", "Basia"]
imiona = ["Ala", "Tomek", "Zenek", "Basia", "Radek"]
wiek = [24, 18, 34, 20]

# Ala 24

# dla różnych długości list
# IndexError: list index out of range
# for i in range(len(imiona)):
#     print(imiona[i], wiek[i])
#
# for i in imiona:
#     print(i, wiek[imiona.index[i]])
# # Ala 24
# # Tomek 18
# # Zenek 34
# # Basia 20

# zip() - łączzy kolekcje
for i in zip(imiona, wiek):
    print(i)
# ('Ala', 24)
# ('Tomek', 18)
# ('Zenek', 34)
# ('Basia', 20)