# słownik - para klucz : wartosć
# {'user' : 'Radek'}
# klucze nie mogą się powtarzać
# {"firstName":"John", "lastName":"Doe"}
# słownik jest odpowiednikiem jsona

# pusty słownik
dictionary = {}
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dict_1 = dict()
print(dict_1)  # {}
print(type(dict_1))  # <class 'dict'>

# dodanie elementów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}

# dodac klucz wiek
dictionary['wiek'] = 56
print(dictionary)  # {'imie': 'Radek', 'wiek': 56}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 56])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 56)])

# nadpisanie wartości
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 56}

# wypisanie wartości dla klucza
print(dictionary['imie'])  # Tomek

dictionary['imie'] = ["Radek", "Tomek", "Magda"]
print(dictionary)  # {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 56}

# wypisac Tomek
print(dictionary['imie'][1])  # Tomek

print(dictionary['imie'][1].lower())  # tomek
print(dictionary['imie'][::-1])  # ['Magda', 'Tomek', 'Radek']

dictionary_radek = {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 56}
print(dictionary_radek)  # {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 56}

# print(dictionary_radek['Imie'])  # KeyError: 'Imie'
print(dictionary_radek['Imie'.lower()])  # ['Radek', 'Tomek', 'Magda']

print(dictionary_radek.get("Imie"))  # None
print(dictionary_radek.get("Imie", "default"))  # default

print(chr(223))  # ß -> ss
# \xhh - Znak o wartości szesnastkowej (np. \x0A reprezentuje znak nowej linii)
print("\u00DF")  # ß
# \N{name} - Znak Unicode o podanej nazwie
print("\N{LATIN SMALL LETTER SHARP S}")  # ß

name1 = "GROSS"
name2 = "groß"

print(name1.lower() == name2.lower())  # False
"""Return a version of the string suitable for caseless comparisons."""
print(name1.casefold() == name2.casefold())  # True

dictionary.update({'data': "12-12-2060"})
print(dictionary)  # {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 56, 'data': '12-12-2060'}

dict_small = {'x': 20}
dict_small.update([('y', 3), ('z', 8)])
print(dict_small)  # {'x': 20, 'y': 3, 'z': 8}

# input() - możliwośc w prowadzania danych do komputera np.: z klawiatury

# tekst = input("Podaj imię:")
# print(tekst)
# # Podaj imię:Radek
# # Radek

# napisać aplikację kalkulator
# pobrac a od uzytkownika
# pobrac b od uzytkownika
# wypisc wynik dodawania a + b
# a = int(input("podaj a:"))  # zwraca str
# b = input("podaj b:")
# print(int(a) + float(b))
# podaj a:4
# podaj b:5
# 9.0

# napisac program słownik pol-ang
pol_ang = {'pies': "dog", "kot": "cat", "dach": 'roof'}
print("Znam takie słowa:", pol_ang.keys())
odp = input("Podaj słóko do przetłumaczenia: ")
print(f"""
Prawidłowa odpowiedź dla: {odp}
to: {pol_ang.get(odp.strip().casefold(), "Nie ma takiego słowa w słowniku")}
""")
# Znam takie słowa: dict_keys(['pies', 'kot', 'dach'])
# Podaj słóko do przetłumaczenia: pies
#
# Prawidłowa odpowiedź dla: pies
# to: dog