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
# zarobki = int(input("Podaj zarobki: "))
# podatek = 0
#
# # tylko jeden warunek może być spełniony
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi: {zarobki * podatek} pln.")
# # Podaj zarobki: 125000
# Podatek wynosi: 112500.0 pln.

sum_zam = 150
if sum_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi: {rabat}")  # Rabat wynosi: 25

# operator warunkowe
rabat = 25 if sum_zam > 100 else 0
print(f"Rabat wynosi: {rabat}")  # Rabat wynosi: 25

# napisac test z...
#  trzy pytania
# punktacja za prawidłową odpowiedź

# punkty = 0
#
# odp = input("Podaj imię trenera: ")
# if odp.strip().casefold() == "Radek".casefold():
#     print('Opowiedź prawidłowa')
#     # punkty = punkty + 1
#     punkty += 1
# else:
#     print("Śpisz?!!!")
#
# odp = input("Która drużyna wygrała Mundial 2026: ")
# if odp.strip().casefold() == "Hiszpania".casefold():
#     print('Opowiedź prawidłowa')
#     punkty += 1
# else:
#     print('Sprawdz w internecie')
#
# odp = input("Jaki Król jest na banknocie 200 zł: ")
# if odp.strip().casefold() == "Zygmunt".casefold():
#     print('Opowiedź prawidłowa')
#     punkty += 1
# else:
#     print("Zerknij do portfela.")
#
# print("Punkty:", punkty)
#
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

# zasymulejmy system zbierania logów
# zmienna: typ_sytemu -> console, email, inny
# console: "Stało się coś strasznego!"
# email: "System email"
# -----
# jesli system jest email to:
# do listy błeddó dopisac tłumaczenie błedów
# error_level -> error, medium, inny

lista_b = []
alert_system = "console"
error_level = "error"

if alert_system == "console":
    print("Stało się coś strasznego!")
elif alert_system == 'email':
    print("System email")
    if error_level == "error":
        lista_b.append("Krytyczny")
    elif error_level == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("inny")
else:
    print("Inny system")

print(lista_b)
