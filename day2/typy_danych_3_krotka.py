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

tup = 1, 2
print(type(tup))  # <class 'tuple'>

# a - pierwszy, b = drugi
a = tup[0]
b = tup[1]
print(a, b)  # 1 2

# rozpakowanie tupli
a, b = tup
print(a, b)  # 1 2

# zamiana miejscami wartości
a, b = b, a
print(a, b)  # 2 1

print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')
# name1, name2, name3
# name1, name2, name3 = tupla_imiona # ValueError: too many values to unpack (expected 3, got 4)
name1, name2, *name3 = tupla_imiona  # * dowolna ilosc elementów
print(name1, name2, name3)  # Zenek Marek ['Radek', 'Ania']

name1, *name2, name3 = tupla_imiona  # * dowolna ilosc elementów
print(name1, name2, name3)  # Zenek ['Marek', 'Radek'] Ania

*name1, name2, name3 = tupla_imiona  # * dowolna ilosc elementów
print(name1, name2, name3)  # ['Zenek', 'Marek'] Radek Ania
