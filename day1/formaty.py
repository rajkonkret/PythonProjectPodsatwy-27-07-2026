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
