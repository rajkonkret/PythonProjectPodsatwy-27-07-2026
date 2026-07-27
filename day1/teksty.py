from pydoc import text

tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>

# teksty są niemutowalne
tekst.upper()  # Return a copy of the string converted to uppercase.
print(tekst)  # Witaj Świecie

# wyswietlanie kopii tekstu
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE
print(tekst)  # Witaj Świecie - oryginał sie nie zmieni!

print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie
print(tekst.title())  # Witaj Świecie

print(tekst)  # Witaj Świecie
print(len(tekst))  # 13 liter len() - długość tekstu

# Witaj Świecie
# 01234556789.... numerowane od zera

print(tekst[1])  # i
print(tekst[3])  # a
print(tekst[6])  # Ś

print(tekst.index("Ś"))  # index  6

# "e"
print(tekst.index("e"))  # index 9, pierwsza od lewej
print(tekst.count("e"))  # występuje 2 razy

# "w"
print(tekst.lower().count("w"))  # występuje 2 razy

# Witaj Świecie
# 01234556789.... numerowane od zera

print(tekst.count("j", 0, 4))  # występuje 0 razy, z prawej strony zbiór otwarty -> 0123
print(tekst.count('a', 3, 4))  # wystapi 1 raz

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usunięcie białych znaków, wiodących i kończących spacji
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

encode_s = tekst.encode("utf-8")
print(encode_s)  # b'Witaj \xc5\x9awiecie'
# \xhh - znak o wartości szesnastkowej
# \xc5\x9a - Ś
# b - typ bajtowy
print(type(encode_s))  # <class 'bytes'>

print(encode_s.decode('utf-8'))  # Witaj Świecie

imie = "Radek"
print(len(imie))  # długosc 5

# Mam na imię ...
print("Mam na imię " + imie + ".")  # Mam na imię Radek.

# f-string, wstrzyknięcie zawartości zmiennej do tekstu
tekst_format = f"Mam na imię {imie} i lubie Pythona."
print(tekst_format)
# Mam na imię Radek i lubie Pythona.

tekst_format = f"\tMam na imię {imie}\n i lubie Pythona.\b"
print(tekst_format)
# "	Mam na imię Radek
#  i lubie Pythona"
# \t tabulator
# \n nowa linia
# \b - backspace
