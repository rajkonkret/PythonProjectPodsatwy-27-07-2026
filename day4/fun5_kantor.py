# stworzyc funkcję kantor
# ma mieć dwie wew funkcje: eur, usd
# w zależności od parametru(kantor) (if) zwróci jedną z funkcji (adres)
# przekazanie kwoty do funkcji usd, eur

def kantor(waluta):
    print("Otwieram kantor")

    def usd():
        pass

    def eur():
        pass

    if waluta == "eur":
        return eur  # zwracamy adres
    else:
        return usd
