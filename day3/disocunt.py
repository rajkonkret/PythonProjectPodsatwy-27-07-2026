from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2026-07-29

time = datetime.now()
print(time)  # 2026-07-29 14:22:16.484373

print(type(today))  # <class 'datetime.date'>
print(type(time))  # <class 'datetime.datetime'>

print(today.day)  # 29
print(today.year)  # 2026

# formatowanie date
