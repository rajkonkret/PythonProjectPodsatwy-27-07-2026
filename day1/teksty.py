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
