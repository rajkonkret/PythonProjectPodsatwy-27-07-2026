# funkcja lambda
# skrócony zapis funkcji
# lambda zawsze zwraca wynik - return
# funkcja anonimowa

def odejmij(a, b):
    return a - b


print(odejmij(6, 90))  # -84

odejmij2 = lambda a, b: a - b  # return
print(odejmij2(7, 9))  # -2

# przerobic na lambdę
# def oblicz_vat(kwota, vat=23):
#     return kwota * (100 + vat) / 100

oblicz_vat = lambda kwota, vat=23: kwota * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 15))  # 1150.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie danych
lista = [1, 2, 14, 24, 50, 67, 80, 100, 200, 500]

# stworzyc listę z elementów tej listy pomnożene * 2

l1 = []
for i in lista:
    l1.append(i * 2)
print(l1)
# [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

l2 = [i * 2 for i in lista]
print(l2)


# [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

def zmien(x):
    return x * 2


l3 = []
for i in lista:
    l3.append(zmien(i))
print(l3)
# [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

# map() - wykonuje funkcje na kolejnych argumentach kolekcji
# funkcje wyższego rzędu - jako argument przyjmuje inna funkcje

print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

# lambda jako funkcja anonimowa
# deklaracja w miejscu wykonania
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map(): [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 8, lista))}")
# Zastosowanie map(): [4, 8, 56, 96, 200, 268, 320, 400, 800, 2000]
# Zastosowanie map(): [8, 16, 112, 192, 400, 536, 640, 800, 1600, 4000]

# filtrowanie danych
l4 = []
for i in lista:
    if i < 3:
        l4.append(i)
print(l4)  # [1, 2]

# filter()
print(f"Zastosowanie filteR(): {list(filter(lambda x: x < 3, lista))}")
print(f"Zastosowanie filteR(): {list(filter(lambda x: x < 10, lista))}")
print(f"Zastosowanie filteR(): {list(filter(lambda x: x < 100, lista))}")
print(f"Zastosowanie filteR(): {list(filter(lambda x: x > 200, lista))}")  # Zastosowanie filteR(): [500]

# wieksze od, 3 mniejsze od 100
print(f"Zastosowanie filteR(): {list(filter(lambda x: x > 3 and x < 100, lista))}")  # Zastosowanie filteR(): [500]
print(f"Zastosowanie filteR(): {list(filter(lambda x: 3 < x < 100, lista))}")  # Zastosowanie filteR(): [500]
# reduce()
