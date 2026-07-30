# funkcja - wydzielony fragment, kodu, można wywołąć w dowolnym momencie
# funkcja musi byc najpierw zadeklarowana
# wywołąnie funkcji uruchamia funkcję

a = 6
b = 8


# deklaracja funkcji
def dodaj():
    print(a + b)


def dodaj2(a, b):  # dwa o bowiązkowe do przekazania argumenty
    print(a + b)  # zmienne lokalne


# ominięcie problemu braku przeciążania funkcji
def odejmij(a, b, c=0):  # argument o wartości domyślnej
    print(a - b - c)


# wywołanie funkcji
dodaj()  # 14
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

# argumenty przekazane po pozycji
dodaj2(4, 9)  # 13

odejmij(1, 2, 3)  # -4
odejmij(1, 2)  # -1

# argumenty po nazwie
odejmij(b=9, a=87)  # 78
odejmij(b=9, a=87, c=90)  # -12

# mieszane
odejmij(1, 2, c=89)  # -90
dodaj2(1, b=90)  # 91

# pozycyjne muszą byc przed nazwanymi
# odejmij(a=10, 1, 2) # SyntaxError: positional argument follows keyword argument
