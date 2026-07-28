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
