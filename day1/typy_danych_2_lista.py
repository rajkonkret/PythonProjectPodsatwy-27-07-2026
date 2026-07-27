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

print(lista[2:])  # ['Zenek', 'Anna', 'Darek', 'Kasia']
print(lista[2:5])  # ['Zenek', 'Anna', 'Darek']

print(lista[2:10])  # ['Zenek', 'Anna', 'Darek', 'Kasia']
