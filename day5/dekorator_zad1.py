# dekorator - funkcja opakowująca inną funkcję

def dekorator(funk):
    def wew():
        print("Dekorujemy")
        return funk()  # zwracamy wynik funkcji

    return wew  # zwracamy adres funkcji


@dekorator
def hej():
    print("Hej!!")


hej()  # Hej!!

# po dodaniu dekoratura
# Dekorujemy
# Hej!!
