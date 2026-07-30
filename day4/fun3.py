a = 10
b = 10


def dodaj():
    a = 7  # zmienne lokalne, widoczne tylko wewnątrz funkcji
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # dziła na globalnych


def dodaj3():
    global a
    a = 7  # zmieniamy zawartość globalnej a
    b = 90
    print(a + b)


def dodaj4():
    a = 10
    b = 9
    c = a + b  # lokalne
    print(c)


print(f"Zmienna a z góry(globalna) {a}")  # Zmienna a z góry(globalna) 10
dodaj()  # 15
print(f"Zmienna a z góry(globalna) {a}")  # Zmienna a z góry(globalna) 10
dodaj2()  # 20
print(f"Zmienna a z góry(globalna) {a}")  # Zmienna a z góry(globalna) 10
dodaj3()  # 97
print(f"Zmienna a z góry(globalna) {a}")  # Zmienna a z góry(globalna) 7
dodaj2()  # 17
print(f"Zmienna a z góry(globalna) {a}")  # Zmienna a z góry(globalna) 7
dodaj4()  # 19
# print(c)  # NameError: name 'c' is not defined
