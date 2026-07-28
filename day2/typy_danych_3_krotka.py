# krotka (tupla) - kolekcja tylko do odczytu, niemutowalna
# pozwala efektywniej zarzadzać pamięcią
# krotka jako stała  - szczególny przypadek zmiennej

tupla_imiona = "Zenek", "Marek", "Radek", "Ania"
print(type(tupla_imiona))  # <class 'tuple'>
print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')

# tupla_liczby = (43, 55, 22.34, 11, 200)
tupla_liczby = 43, 55, 22.34, 11, 200
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

# tupla jednoelementowa
tupla_jeden = 45,
print(type(tupla_jeden))  # <class 'tuple'>
print(tupla_jeden)  # (45,)

# przy jednoelementowych tuplach PEP8 zaleca nawias
tupla_jeden = (45,)
print(type(tupla_jeden))  # <class 'tuple'>
print(tupla_jeden)  # (45,)

del tupla_jeden  # usunięcie całej tupli
# print(tupla_jeden)  # NameError: name 'tupla_jeden' is not defined

# tupla_liczby[0] = 123 # TypeError: 'tuple' object does not support item assignment

print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')

print(tupla_imiona.index("Radek"))  # indeks 2
print(tupla_imiona.count("Radek"))  # występuje jeden raz

print(len(tupla_imiona))  # liczba elementów: 4
