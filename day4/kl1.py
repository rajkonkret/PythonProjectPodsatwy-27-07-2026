# klasa - przepis, szablon
# cechy (zmienne)
# metody (funkcje)
# obiekt - instancja klasy
# klasa musi zostac najpierw zadeklarowany
# tworzenie obiektu kalsy uruchamia metodę inicjalizującą (konstruktor) __init__
# __del__ - destruktor
# paradygmanty -> hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# PascalCase, UpperCamelCase
class Human:
    # pass
    """Klasa Human opisująca człowieka w pythonie"""

    imie = ""
    wiek = None
    plec = "k"


cz1 = Human()
print(Human.__doc__)  # Klasa Human opisująca człowieka w pythonie
# cd .. wyjscie do katalogu wyżej
# cd day4 - wejście do katalogu day4
# pydoc -b - serwer dokumentacji
# pydoc -w kl1.py - plik html z dokumentacją

print(cz1.imie)
cz1.imie = "Anna"
cz1.wiek = 34
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Anna
# 34
# k

