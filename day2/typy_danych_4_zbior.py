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

# pop()
print(zbior.pop())  # 33 - usunie pierwszy

zmienna = zbior.pop()
print(f"Zmienna: {zmienna}")  # Zmienna: 66
print("Zmienna:", zmienna)  # Zmienna: 66

zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}
print(zbior_2)  # {18, 667, 52, 11, 44, 12.34, 62}
print(type(zbior_2))  # <class 'set'>

# operacje na zbiorach

# suma zbiorów, zwraca nowy zbiór
print(zbior | zbior_2)  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}
print(zbior.union(zbior_2))  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}

# część wspólna zbiorów
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica zbiorów
print(zbior - zbior_2)  # {24, 777, 22, 25}
print(zbior.difference(zbior_2))  # {24, 777, 22, 25}
print(zbior_2.difference(zbior))  # {667, 52, 12.34, 62}

# łączy zbiory, zmienia bazowy!!!
zbior.update(zbior_2)
print(zbior)  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62} zmienił się bazowy zbior!!!


