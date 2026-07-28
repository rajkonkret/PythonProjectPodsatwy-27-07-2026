# instrukcja warunkowa
# instrukcje sterowania przepływem programu

# if
# w zależności od warunku wykona jeden lub drugi blok programu
# wyrażenie w warunku musi zwrócic bool

odp = True

if odp: print('test')

if odp:
    # blok programu wykonywany gdy True
    print("Test")

# debugger - narzedzie do wykonywania programu krok po kroku
# pulapka - miejsce zatrzymania programu
odp = False
if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza część programu")  # Dalsza część programu

odp = "Radek"
if odp:
    print("Działa")  # Działa

if odp == "Radek":  # == porównanie
    print("Jestem Radek")
else:
    print("To nie Radek")
# Jestem Radek

odp = "Tomek"
if odp:
    print("Działa")  # Działa

if odp == "Radek":  # == porównanie
    print("Jestem Radek")
else:  # wartosc domyslna, w przeciwnym wypadku
    print("To nie Radek")  # To nie Radek

odp = 0
if odp:
    print("Działa")
else:
    print("Zero -> False")
# Zero -> False

a = "Radek"
# jezeli długosć tekstu jest większa niz 3 wypisac:
# Długość wynosi: ..., więcej niż 3.

if len(a) > 3:
    print(f"Długość wynosi: {len(a)}, więcej niż 3.")

n = len(a)
if n > 3:
    print(f"Długość wynosi: {n}, więcej niż 3.")

# operator morsa, walrus operator
if (n := len(a)) > 3:
    print(f"Długość wynosi: {n}, więcej niż 3.")

# pobrac zarobki
# jesli zarobki mniejsze od 10000 podatek 0
# dla pozostałych podatek 90% (0.9)
# wypisac obliczony podatek

# dodaj podatek 0.2 dla przedziału 10_000 do 39999
# dodaj podatek 0.4 dla przedzialu 40000 do 99999
zarobki = int(input("Podaj zarobki: "))
podatek = 0

# tylko jeden warunek może być spełniony
if zarobki < 10_000:
    podatek = 0
elif zarobki < 40_000:
    podatek = 0.2
elif zarobki < 100_000:
    podatek = 0.4
else:
    podatek = 0.9

print(f"Podatek wynosi: {zarobki * podatek} pln.")
# Podaj zarobki: 125000
# Podatek wynosi: 112500.0 pln.
