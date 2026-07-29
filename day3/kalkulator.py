# napisać kalkulator
# while True
# menu z opcjiami
# wyświetlić ładnie wynik -> f-string -> 5 * 8 = 40
# obsłużyc wyjątki
while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)

    odp = input("Podaj wybraną opcję:")
    if odp not in ['1', '2', '3', '4']:
        print("Niedozwolony wybór z menu")
        break
    try:
        a = float(input("podaj pierwszą liczbę:"))
        b = float(input("podaj drugą liczbę:"))

        # match case
        if odp == "1":
            print(f"Dodawanie: {a} + {b} = {a + b}")
        elif odp == "2":
            print(f"Odejmowanie: {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"Mnożenie: {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"Dzielenie: {a} / {b} = {a / b}")
        else:
            print("Brak takiej operacji")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except Exception as e:
        print("Bład:", e)
    finally:
        print("Obliczenia zostały wykonane")

print(50 * "-")
a = float(input("podaj pierwszą liczbę:"))
b = float(input("podaj drugą liczbę:"))
znak = input("Wprowadz znak: (+,-,*,/)")
wyr = f"{a} {znak} {b}"
print(eval(wyr))  # wykonuje dowolne wyrażnie zapisane w stringu

# --------------------------------------------------
# podaj pierwszą liczbę:>? 5
# podaj drugą liczbę:>? 6
# Wprowadz znak: (+,-,*,/)>? +
# 11.0
