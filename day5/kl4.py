from abc import ABC, abstractmethod


# klasa abstrakcyjna - klasa z której nie można tworzyc obiektów
class Ptak(ABC):
    """
    Klasa Ptak opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca - konstruktor
        :param gatunek:
        :param szybkosc:
        """

        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością:", self.szybkosc, "km/h")

    @abstractmethod  # metoda abstrakcyjna
    def wydaj_odglos(self):
        pass

    def __str__(self) -> str:
        return f"{self.gatunek} {self.szybkosc}"


class Kura(Ptak):
    """
    Klasa Kura, dziedziczy po kalsie Ptak
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # musimy wywołąc super(), super() - klasa nadrzędna

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko ko ko ko ko ko")


class Orzel(Ptak):
    """
    Klasa Orzeł dziedziczy po klasie Ptak
    """

    def wydaj_odglos(self):
        print("Kier kiir kier kir kir")


# nie można tworzyć obiektów klasy abstrakcyjnej
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzeł", 50)
# print(or1)  # <__main__.Ptak object at 0x0000024BDF5D9A90> -> __str__ ->   Orzeł 50
# or1.latam()  # Tu Orzeł Lecę z szybkością: 50 km/h
#
# kur1 = Ptak("Kura", 0)
# print(kur1)  # Kura 0
# kur1.latam()  # Tu Kura Lecę z szybkością: 0 km/h

kur2 = Kura("Kura zielonóżka")
print(kur2)  # Kura zielonóżka 0
kur2.latam()  # Tu Kura zielonóżka Ja nie latam

or2 = Orzel("Bielik", 55)
print(or2)  # Bielik 55
or2.latam()  # Tu Bielik Lecę z szybkością: 55 km/h

kur2.wydaj_odglos()
or2.wydaj_odglos()
# Ko ko ko ko ko ko
# Kier kiir kier kir kir
