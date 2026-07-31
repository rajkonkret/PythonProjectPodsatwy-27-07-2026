class Ptak:
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

    def __str__(self) -> str:
        return f"{self.gatunek} {self.szybkosc}"


or1 = Ptak("Orzeł", 50)
print(or1)  # <__main__.Ptak object at 0x0000024BDF5D9A90> -> __str__ ->   Orzeł 50
or1.latam()  # Tu Orzeł Lecę z szybkością: 50 km/h

kur1 = Ptak("Kura", 0)
print(kur1)  # Kura 0
kur1.latam()  # Tu Kura Lecę z szybkością: 0 km/h
