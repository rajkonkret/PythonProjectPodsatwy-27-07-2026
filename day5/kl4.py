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


or1 = Ptak("Orzeł", 50)
print(or1)  # <__main__.Ptak object at 0x0000024BDF5D9A90> -> __str__
