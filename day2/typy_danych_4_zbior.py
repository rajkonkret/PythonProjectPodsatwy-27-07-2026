# zbior (set) - przechowuje unikalne wartości
# nie zachowuje kolejnosci przy dodawaniu elementów
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11, 777]
zbior = set(lista)
print(type(zbior))  # <class 'set'>
print(zbior)  # {33, 66, 777, 11, 44, 22, 55} zmiana kolejnosci

lista_sort = sorted(zbior)
print(lista_sort)  # [11, 22, 33, 44, 55, 66, 777]

# pusty zbiór
zb2 = set()  # tylko i wyłacznie z apomocą słówka set()
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(33)
zbior.add(24)
zbior.add(24)
zbior.add(33)
zbior.add(25)
print(zbior)
# {33, 66, 777, 11, 44, 18, 22, 55, 24, 25}

# usunięcie elementu ze zbioru
zbior.remove(55)  # wartość elementu
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24, 25}
