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
print("Imię pacjenta:", data['name'])
print("Wiek pacjenta:", data['age'])
# Imię pacjenta: Radek
# Wiek pacjenta: 40

# zamiana słownika na json (tekst)
json_text = json.dumps(data)
print(json_text)  # {"name": "Radek", "age": 40, "czy_pali": null}
print(type(json_text))  # <class 'str'>

# zamiana jsona  słownik
dict_json = json.loads(json_text)
print(dict_json)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(dict_json))  # <class 'dict'>
print("Imię pacjenta:", dict_json['name'])
print("Wiek pacjenta:", dict_json['age'])
# Imię pacjenta: Radek
# Wiek pacjenta: 40
