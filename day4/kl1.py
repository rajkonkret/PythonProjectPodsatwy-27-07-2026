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

    def powitanie(self):
        print(f"NAzywam się: {self.imie}")
        # self - przechowuje obiekt

    def ruszaj(self):

        if self.plec == "m":
            print("Ruszyłem w drogę")
        else:
            print("Ruszyłam w drogę")

    def __str__(self) -> str:
        return f"{self.imie=}, {self.wiek=} {self.plec=}"

    # napisac metode ruszaj()
    # w zależności od płci
    # ruszyłem w drogę
    # ruszyłam w drogę


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

cz2 = Human()
cz2.imie = "Radek"
cz2.wiek = 50
cz2.plec = "m"

print(cz2.imie)  # Radek
print(cz2.wiek)  # 50
print(cz2.plec)  # m

print(cz2)
cz1.powitanie()
cz2.powitanie()
# NAzywam się: Anna
# NAzywam się: Radek

cz1.ruszaj()
cz2.ruszaj()
# Ruszyłam w drogę
# Ruszyłem w drogę

lista = [cz1, cz2]
for i in lista:
    i.ruszaj()
# Ruszyłam w drogę
# Ruszyłem w drogę

print(50 * "-")
print(cz1)
print(cz2)
# po nadpissaniu __str__
# __repr__
# --------------------------------------------------
# self.imie='Anna', self.wiek=34 self.plec='k'
# self.imie='Radek', self.wiek=50 self.plec='m'
