# funkcje zwracające wynik
# kończy się słówkiem return

a = 9
b = 98


def dodaj():
    return a + b  # zwróć wynik a + b


# funkcja odejmij, z trzema argumentami domyslnymi
def odejmij(a=0, b=0, c=0):
    return a - b - c


print(dodaj())  # 107

wynik = dodaj()
print("Wynik:", wynik)  # Wynik: 107

print(odejmij(1, 2, 3))  # -4
print(odejmij(1, 2, c=3))  # -4
print(odejmij(1, b=2, c=3))  # -4
print(odejmij())  # 0
print(odejmij(a, b))  # -89


def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100


print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
print(oblicz_vat(vat=15, kwota=1000))
# 1230.0
# 1080.0
# 1150.0
