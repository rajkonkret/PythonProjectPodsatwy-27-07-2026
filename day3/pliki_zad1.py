# działania z plikami
# filehandler

# open()

# context manager
# with - context manager w pythonie

with open("test.log", "w") as file:
    file.write("Powitanie\n")
    file.write("Jeszcze jedno\n")

# file.write("") # ValueError: I/O operation on closed file.

# x tworzy nowy plik gdy plik nie istnieje!!!
# FileExistsError: [Errno 17] File exists: 'test.log'
# with open("test.log", "x") as file:
#     file.write("Powitanie\n")
#     file.write("Jeszcze jedno\n")

# a - append - dołacza dane na końcu
with open("test.log", "a") as file:
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Jeszcze jedno\n")

with open("test.log", "r") as f:
    lines = f.read()

print(lines)
# Powitanie
# Jeszcze jedno
# Dodane
# Dodane
# Jeszcze jedno