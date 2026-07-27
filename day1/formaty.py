user = "Tomek"  # str
wiek = 45  # int
liczba = 90876545632124678  # int

wersja = 3.9001
print(type(wersja))  # <class 'float'>, liczba zmiennoprzenkowa

print("Witaj %s, masz teraz %d lat." % (user, wiek))
# Witaj Tomek, masz teraz 45 lat.
# %s - str
# %d - digit

# print("Witaj %d, masz teraz %s lat." % (user, wiek))
# TypeError: %d format: a real number is required, not str

# f-string
print(f"Witaj {user}, masz teraz {wiek} lat.")
# Witaj Tomek, masz teraz 45 lat.

# %i, %f

print("Używamy wersji Pythona %i" % 3)  # Używamy wersji Pythona 3
print("Używamy wersji Pythona %f" % 3)  # Używamy wersji Pythona 3.000000
print("Używamy wersji Pythona %.2f" % 3)  # Używamy wersji Pythona 3.00
print("Używamy wersji Pythona %.1f" % 3)  # Używamy wersji Pythona 3.0
print("Używamy wersji Pythona %.0f" % 3.9)  # Używamy wersji Pythona 4 wyswietli zaokrąglone
print("Używamy wersji Pythona %.f" % 3.9)  # Używamy wersji Pythona 4 wyswietli zaokrąglone

x = 3.8769
print(x)  # 3.8769
y = round(x)
print(y)  # 4
print(type(y))  # <class 'int'>

z = round(x, 2)
print(f"{z=}")  # z=3.88
print(type(z))  # <class 'float'>

print(f"Używamy wersji Pythona {wersja}")  # Używamy wersji Pythona 3.9001
print(f"Używamy wersji Pythona {wersja:.2f}")  # Używamy wersji Pythona 3.90
print(f"Używamy wersji Pythona {wersja:.1f}")  # Używamy wersji Pythona 3.9
print(f"Używamy wersji Pythona {wersja:.0f}")  # Używamy wersji Pythona 4
# print(f"Używamy wersji Pythona {wersja:.f}")  # Używamy wersji Pythona 4, ValueError: Format specifier missing precision
