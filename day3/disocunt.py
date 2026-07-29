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
