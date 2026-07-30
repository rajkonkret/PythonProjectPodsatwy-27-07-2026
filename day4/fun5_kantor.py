# stworzyc funkcję kantor
# ma mieć dwie wew funkcje: eur, usd
# w zależności od parametru(kantor) (if) zwróci jedną z funkcji (adres)
# przekazanie kwoty do funkcji usd, eur

def kantor(waluta):
    print("Otwieram kantor")

    def usd(kwota=0):
        print(f"Wymieniam {kwota} usd na {kwota * 3.80}")

    def eur(kwota=0):
        print(f"Wymieniam {kwota} eur na {kwota * 4.30}")

    if waluta == "eur":
        return eur  # zwracamy adres
    else:
        return usd


kantor_usd = kantor("usd")
kantor_eur = kantor("eur")
# Otwieram kantor
# Otwieram kantor

kantor_eur(100)
kantor_eur(100)
kantor_eur(100)
kantor_eur(100)
kantor_eur(100)
# Wymieniam 100 eur na 430.0
# Wymieniam 100 eur na 430.0
# Wymieniam 100 eur na 430.0
# Wymieniam 100 eur na 430.0
# Wymieniam 100 eur na 430.0

kantor_usd(45)
kantor_usd(45)
kantor_usd(45)
kantor_usd(45)
# Wymieniam 45 usd na 171.0
# Wymieniam 45 usd na 171.0
# Wymieniam 45 usd na 171.0
# Wymieniam 45 usd na 171.0

kantor_eur(23)
# Wymieniam 23 eur na 98.89999999999999
