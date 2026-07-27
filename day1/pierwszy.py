# https://peps.python.org/pep-0008/
# snake_case
# ctrl alt l - formatowanie
import sys

print('Hello World')  # wypisz/wydrukuj
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProjectPodsatwy-27-07-2026> python .\main.py
# Hi, PyCharm

print("Witaj Świecie")
print("radek \"komp\"")  # radek "komp"
print('radek "komp"')  # radek "komp"

# ctrl / - komentarz
# print('Radek")
#   File "C:\Users\CSComarch\PycharmProjects\PythonProjectPodsatwy-27-07-2026\day1\pierwszy.py", line 13
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 13)
#
# Process finished with exit code 1 - program zakonczył się z błedem

print("Dalsza częśc programu")

print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
# ctrl d - powielanie

# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'> string tekstowe

print("38" + "90")  # 3890
print("Radek " + "1")  # Radek 1

print(39 + 90)  # 129
print(type(39))  # <class 'int'>, liczby całkowite

# sys
print(sys.int_info)

# sys.int_info(bits_per_digit=30,
# sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)
