# {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# json - dane typu klucz - wartosc
# typ wymiany pomiedzy klient server
# odpowiednikiem jsona w pythonie jest słownik
# zawsze podwójne cudzysłowia
# None -> null

# orjson
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(person_dict)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

# zapis danych jako json
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)
# {"name": "Radek", "age": 40, "czy_pali": null}

# zapis danych jako json - beautify
with open('nasze_dane_b.json', "w") as f:
    json.dump(person_dict, f, indent=4)

# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# sortowanie po kluczach
with open('nasze_dane_sorted.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', "r") as file:
    data = json.load(file)

print(data)
print(type(data))
# {'name': 'Radek', 'age': 40, 'czy_pali': None}
# <class 'dict'>
