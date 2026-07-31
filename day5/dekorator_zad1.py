# dekorator - funkcja opakowująca inną funkcję

def dekorator(funk):
    def wew():
        print("Dekorujemy")
        return funk().upper()  # zwracamy wynik funkcji

    return wew  # zwracamy adres funkcji


@dekorator
def hej():
    # print("Hej!!") # zwraca None
    return "Hej!!"


hej()  # Hej!!

# po dodaniu dekoratura
# Dekorujemy
# Hej!!
print(hej())  # HEJ!!
