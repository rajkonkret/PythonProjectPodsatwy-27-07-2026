# kolekcje

# lista - pozwala przechowywac dowolną ilośc danych, rónego typu na raz w jednej liście
# zachowuje kolejnośc przy dodawaniu elementów

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# dodawanie elemntów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Anna")
lista.append("Darek")
lista.append("Kasia")
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Darek', 'Kasia']

# długość listy
print(len(lista))  # 6 elementów

# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Darek', 'Kasia']
#    0         1        2        3       4         5

print(lista[2])  # Zenek
print(lista[4])  # Darek

# print(lista[10]) # IndexError: list index out of range

print(lista[5])  # Kasia
print(lista[len(lista) - 1])  # Kasia
print(lista[-1])  # Kasia
print(lista[-2])  # Darek

# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Darek', 'Kasia']
#    0         1        2        3       4         5
#    -6        -5       -4       -3      -2        -1


# slicowanie - fragment listy
print(lista[0:3])  # ['Radek', 'Tomek', 'Zenek'] bez indeksu 3
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']

print(lista[2:])  # ['Zenek', 'Anna', 'Darek', 'Kasia'] włącznie z ostatnim
print(lista[2:5])  # ['Zenek', 'Anna', 'Darek']

print(lista[2:10])  # ['Zenek', 'Anna', 'Darek', 'Kasia']

print(lista[15:20])  # [] - pusta lista

print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Anna', 'Darek', 'Kasia']

# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Darek', 'Kasia']
#    0         1        2        3       4         5
#    -6        -5       -4       -3      -2        -1

a = None
b = None
print(lista[a:b])
# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Darek', 'Kasia']

print(lista[-2:0])  # [], [4:0]
print(lista[-2:-2])  # [], [4:4]
print(lista[0:-2])  # [0:4] # ['Radek', 'Tomek', 'Zenek', 'Anna'] [-6:-2]

# 0 do 14
lista_15 = list(range(15))  # od 0 do 14
print(lista_15)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[::2])  # [start:stop:krok], [0, 2, 4, 6, 8, 10, 12, 14]
print(lista_15[::3])  # [start:stop:krok], [0, 3, 6, 9, 12]

print(lista_15[::-1])  # odwrotna kolejność
# [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(list(range(5, 15, 2)))  # [5, 7, 9, 11, 13] (start, stop, krok)

lista1 = [1, 2, 3]
lista2 = [7, 8, 9]
print(lista1 + lista2)  # [1, 2, 3, 7, 8, 9]
# lista1.append(list(range(5, 9)))
# print(lista1) # [1, 2, 3, [5, 6, 7, 8]]
lista1.extend(list(range(5, 9)))
print(lista1)  # [1, 2, 3, 5, 6, 7, 8]

# python nie ma typu danych tablica (array)
tablice = [[1, 2], [3, 4]]
print(tablice)  # [[1, 2], [3, 4]]
# numpy - biblioteka do pracy z tablicami/macierzami

print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Anna', 'Darek', 'Kasia']

lista[2] = "Alicja"
print(lista)
# ['Radek', 'Tomek', 'Alicja', 'Anna', 'Darek', 'Kasia']

# dopisanie eleemntu we wskazanym miejscu (indeksie)
lista.insert(1, "Ola")
print(lista)
# ['Radek', 'Ola', 'Tomek', 'Alicja', 'Anna', 'Darek', 'Kasia']

# sprawdzenie indexu
print(lista.index("Darek"))  # indeks numer 5

# usnięcie elementu z listy,  pierwszy napotkany
lista.remove("Tomek")
print(lista)
# ['Radek', 'Ola', 'Alicja', 'Anna', 'Darek', 'Kasia']

# dodac do listy (taki element jak juz jest)
# usunąć taki element

lista.append("Anna")
print(lista)
# ['Radek', 'Ola', 'Alicja', 'Anna', 'Darek', 'Kasia', 'Anna']

lista.remove("Anna")
print(lista)
# ['Radek', 'Ola', 'Alicja', 'Darek', 'Kasia', 'Anna']
