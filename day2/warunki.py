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

