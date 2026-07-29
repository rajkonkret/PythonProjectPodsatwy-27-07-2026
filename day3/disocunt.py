from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2026-07-29

time = datetime.now()
print(time)  # 2026-07-29 14:22:16.484373

print(type(today))  # <class 'datetime.date'>
print(type(time))  # <class 'datetime.datetime'>

print(today.day)  # 29
print(today.weekday())  # 2 - środa
print(today.isoweekday())  # 3 - środa
print(today.year)  # 2026

# formatowanie date
formated_date = datetime.now().strftime("%d/%m/%Y")
print(formated_date)  # 29/07/2026
print(type(formated_date))  # <class 'str'>

# 14:27
# 14:27:34
# 2:27 pm

# Dla daty:
# %Y: Rok z pełną liczbą cyfr, np. "1989", "2023".
# %y: Rok z dwiema ostatnimi cyframi, np. "89", "23".
# %m: Miesiąc z zerem wiodącym, np. "01" do "12".
# %d: Dzień miesiąca z zerem wiodącym, np. "01" do "31".
# %B: Pełna nazwa miesiąca, np. "January", "December".
# %b: Skrócona nazwa miesiąca, np. "Jan", "Dec".
# %A: Pełna nazwa dnia tygodnia, np. "Monday", "Sunday".
# %a: Skrócona nazwa dnia tygodnia, np. "Mon", "Sun".
# Dla czasu:
# %H: Godzina w formacie 24-godzinnym z zerem wiodącym, np. "00" do "23".
# %I: Godzina w formacie 12-godzinnym z zerem wiodącym, np. "01" do "12".
# %p: AM/PM.
# %M: Minuty z zerem wiodącym, np. "00" do "59".
# %S: Sekundy z zerem wiodącym, np. "00" do "59".
# %f: Mikrosekundy, np. "000000" do "999999".

formated_time = datetime.now().strftime("%H:%M")
print(formated_time)  # 14:36
print(type(formated_time))  # <class 'str'>

formated_time_usa = datetime.now().strftime("%I:%M %p")
print(formated_time_usa)  # 02:37 PM
print(formated_time_usa.removeprefix("0"))  # 2:38 PM
print(type(formated_time_usa))  # <class 'str'>

object_data = datetime.now().strptime("29/07/2026", "%d/%m/%Y")
print(object_data)  # 2026-07-29 00:00:00
print(type(object_data))  # <class 'datetime.datetime'>

# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2026-07-30

products = [
    {'sku': 1, 'exp_date': today, "price": 200},
    {'sku': 2, 'exp_date': today, "price": 300},
    {'sku': 3, 'exp_date': today, "price": 200},
    {'sku': 4, 'exp_date': tomorrow, "price": 400},
    {'sku': 5, 'exp_date': today, "price": 250},
    {'sku': 6, 'exp_date': today, "price": 1200},
    {'sku': 7, 'exp_date': tomorrow, "price": 800},
    {'sku': 8, 'exp_date': today, "price": 200.99},
]

for p in products:
    # print(p)  # {'sku': 5, 'exp_date': datetime.date(2026, 7, 29), 'price': 250}
    # print(p['exp_date'])

    # if p['exp_date'] == today:
    #     pass

    if p['exp_date'] != today:
        continue  # konczy bieżące wykonanie pętli, pobiera kolejny eleement

    print(p['price'])
    p['price'] *= 0.8  # price = price * 0.8

    print(f"""
Price for sku: {p['sku']}
is now: {p['price']:.2f}
""")

# Price for sku: 1
# is now: 160.00
#
# 300
#
# Price for sku: 2
# is now: 240.00
#
# 200
#
# Price for sku: 3
# is now: 160.00
#
# 250
#
# Price for sku: 5
# is now: 200.00
#
# 1200
#
# Price for sku: 6
# is now: 960.00
#
# 200.99
#
# Price for sku: 8
# is now: 160.79
