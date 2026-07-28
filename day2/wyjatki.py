# wyjątki - błędy wykonywania programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonProjectPodsatwy-27-07-2026\day2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
# Process finished with exit code 1

# obsługa wyjątków
try:
    print(5 / 0)
except ZeroDivisionError:
    print("Nie można dzielic przez zero!!!")

print("Dalsza częśc...")
# Nie można dzielic przez zero!!!
# Dalsza częśc...