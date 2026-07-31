url = "https://api.nbp.pl/api/exchangerates/rates/A/eur/"

# nazwe walute, kurs waluty
import requests

response = requests.get(url)
data = response.json()

print(data)
print(type(data))
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
# 'rates': [{'no': '147/A/NBP/2026', 'effectiveDate': '2026-07-31', 'mid': 4.3128}]}
# <class 'dict'>

print('Waluta:', data['currency'])  # Waluta: euro
print("Kurs:", data['rates'])  # [{'no': '147/A/NBP/2026', 'effectiveDate': '2026-07-31', 'mid': 4.3128}]
print("Kurs:", data['rates'][0])  # {'no': '147/A/NBP/2026', 'effectiveDate': '2026-07-31', 'mid': 4.3128}
print("Kurs:", data['rates'][0]['mid'])  # Kurs: 4.3128
print("Kurs:", type(data['rates'][0]['mid']))  # Kurs: <class 'float'>
