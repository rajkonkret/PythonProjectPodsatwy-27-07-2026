# działania z plikami
# filehandler

# open()

# context manager
# with - context manager w pythonie

with open("test.log", "w", encoding="utf-8") as file:
    file.write("Powitanie\n")
    file.write("Jeszcze jedno\n")

# file.write("") # ValueError: I/O operation on closed file.

# x tworzy nowy plik gdy plik nie istnieje!!!
# FileExistsError: [Errno 17] File exists: 'test.log'
# with open("test.log", "x", encoding="utf-8") as file:
#     file.write("Powitanie\n")
#     file.write("Jeszcze jedno\n")

# a - append - dołacza dane na końcu
with open("test.log", "a", encoding="utf-8") as file:
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dśąćodane\n")
    file.write("Jeszcze jedno\n")

with open("test.log", "r", encoding="utf-8") as f:
    lines = f.read()

print(lines)
# Powitanie
# Jeszcze jedno
# Dodane
# Dodane
# Jeszcze jedno
