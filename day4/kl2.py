class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    # dopisac metody wypisz_wiek() wypisz_wrost()
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu.")

    def powitanie(self):
        print(f"NAzywam się: {self.imie}")
        # self - przechowuje obiekt

    def ruszaj(self):

        if self.plec == "m":
            print("Ruszyłem w drogę")
        else:
            print("Ruszyłam w drogę")

    def __str__(self) -> str:
        return f"{self.imie=}, {self.wiek=} {self.plec=} {self.wzrost=}"


# cz1 = Human()
# TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'

cz1 = Human("Radek", 45, 189, "m")
print(cz1)
# self.imie='Radek', self.wiek=45 self.plec='m' self.wzrost=189
cz1.wypisz_wzrost()
cz1.wypisz_wiek()
# Mam 189 cm wzrostu.
# Mam 45 lat.
