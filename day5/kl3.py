# hermetyzacja

class Car:
    """
    Klasa opisująca samochód w Pythonie
    """

    def __init__(self, model, year):
        """
        Metoda inicjalizująca - konstruktor
        :param model:
        :param year:
        """

        self.model = model
        self.year = year

        # name mangling
        # pole prywatne
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkośc wynosi: {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmiana_biegu()

    def __zmiana_biegu(self):
        print('Zmiana biegu')


car = Car("Toyota", 2026)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()

# pole oznaczone jako prywatne
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car.__predkosc)  # 50

car.licznik()  # Prędkośc wynosi: 50 km/h
car.__predkosc = 0
car.licznik()  # Prędkośc wynosi: 50 km/h

car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()  # Prędkośc wynosi: 0 km/h

# Prędkośc wynosi: 50 km/h
# Prędkośc wynosi: 50 km/h
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Prędkośc wynosi: 0 km/h

# enkapsulacja - hermetyzowanie (pola prywatne) i wystawienie metod do zapisu i odczytu tzw: gettery, settery
