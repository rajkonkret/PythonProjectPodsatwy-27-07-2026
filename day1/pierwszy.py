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

print("38" + "90")  # 3890, konkatenacja, łączenie tekstów
print("Radek " + "1")  # Radek 1

print(39 + 90)  # 129
print(type(39))  # <class 'int'>, liczby całkowite

# sys
print(sys.int_info)

# sys.int_info(bits_per_digit=30,
# sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)

# print("39" + 30)  # TypeError: can only concatenate str (not "int") to str

# rzutowanie typów int(), str()
print(int("39") + 30)  # 69
print("39" + str(30))  # 3930

# zmienna - pudełko, szufladka na dane

name = "Radek"
print(name)  # Radek
print(type(name))  # <class 'str'>

age = 89
print(age)
print(type(age))  # <class 'int'>

# typowanie dynamiczne
age = 'Radek'
print(age)  # Radek
print(type(age))  # <class 'str'>

age = "90"
# print(age + 10)  # TypeError: can only concatenate str (not "int") to str

print(age * 2)  # 9090
print(168 * "70")
# 70707070707070707070707070707070707070707070707070707070707070707070707070707070707070707070707070
# 70707070707070707070707070707070707070707070707070707070707070707070707070707070707070707070707070
# 707070707070707070707070707070707070707070
# 70707070707070707070707070707070707070707070707070707070707070707070707070707070707070707070707070

print(int(168) * int("70"))  # 11760

# podpowiedzi typów
name: str = "Radek"
print(name)
print(type(name))  # <class 'str'>

name = 90
print(name)
print(type(name))  # <class 'int'>

# mypy, pyright, ruff
# pip - menadzer pakietów
# pip install mypy
# cd day1\
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProjectPodsatwy-27-07-2026\day1> mypy .\pierwszy.py
# pierwszy.py:74: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
# pierwszy.py:78: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
# pierwszy.py:91: error: Name "name" already defined on line 65  [no-redef]
# pierwszy.py:95: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 4 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\CSComarch\PycharmProjects\PythonProjectPodsatwy-27-07-2026\day1>
# mypy .\pierwszy.py
