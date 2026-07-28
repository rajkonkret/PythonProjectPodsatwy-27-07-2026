# wyjątki - błędy wykonywania programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonProjectPodsatwy-27-07-2026\day2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
# Process finished with exit code 1

# obsługa wyjątków
try:
    # print(5 / 0)
    # int("Q")
    # print(2 + 'Ania')
    # raise KeyError("Błąd kluczy")  # rzuci bład
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie można dzielic przez zero!!!")
except ValueError:
    print("Bład wartości")
except TypeError:
    print("Bład typu")
except Exception as e:
    print("Bład:", e)
else:  # tylko gdy  nie ma błedu
    print("wynik:", wynik)
finally:  # wykona się zawsze
    print("Następne obliczenie")

# print("wynik:", wynik)
print("Dalsza częśc...")
# Nie można dzielic przez zero!!!
# Dalsza częśc...

# Bład: 'Błąd kluczy'
# Dalsza częśc...
