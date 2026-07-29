# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce

# csv - dane oddzilone znakiem podziału ,;tab|

import csv

row = ['radek', 'coe', "3", 0]
columns = ['name', 'branch', 'year', 'cgpa']

filename = 'records.csv'

# newline="" obejscie problemu pustych linii
with open(filename, "w", newline="") as csv_f:
    csv_writer = csv.writer(csv_f)
    csv_writer.writerow(columns)
    csv_writer.writerow(row)

dict_name = dict(zip(columns, row))
print(dict_name)
print(type(dict_name))
# {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': 0}
# <class 'dict'>

filename = 'records_dict.csv'

with open(filename, "w", newline="") as csv_f:
    # csv_writer = csv.DictWriter(csv_f, fieldnames=columns)
    csv_writer = csv.DictWriter(csv_f, fieldnames=dict_name.keys())
    csv_writer.writeheader()
    csv_writer.writerow(dict_name)

products = [
    {'sku': 1, 'exp_date': 'today', "price": 200},
    {'sku': 2, 'exp_date': 'today', "price": 300},
    {'sku': 3, 'exp_date': 'today', "price": 200},
    {'sku': 4, 'exp_date': 'tomorrow', "price": 400},
    {'sku': 5, 'exp_date': 'today', "price": 250},
    {'sku': 6, 'exp_date': 'today', "price": 1200},
    {'sku': 7, 'exp_date': 'tomorrow', "price": 800},
    {'sku': 8, 'exp_date': 'today', "price": 200.99},
]

# filename = "records_discount.csv"
filename = "records_discount_semicolon.csv"
list_products = [key for key in products[0]]
print(list_products)

with open(filename, "w", newline="") as csv_f:
    # csv_writer = csv.DictWriter(csv_f, fieldnames=columns)
    # csv_writer = csv.DictWriter(csv_f, fieldnames=products[0].keys())
    csv_writer = csv.DictWriter(csv_f, fieldnames=products[0].keys(), delimiter=";")
    csv_writer.writeheader()
    csv_writer.writerows(products)  # writerows - dla listy słowników
