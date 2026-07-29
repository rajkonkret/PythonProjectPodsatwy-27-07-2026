# with open("test.log", "r") as f:
#     lines = f.read()
#
# print(lines)
# Powitanie
# Jeszcze jedno
# Dodane
# Dodane
# DĹ›odane
# Jeszcze jedno

import chardet
# pip install chardet

# odczyt binarny - rb
with open('test.log', "rb") as fh:
    raw_data = fh.read()

print(raw_data)
# b'Powitanie\r\nJeszcze jedno\r\nDodane\r\nDodane\r\nD\xc5\x9bodane\r\nJeszcze jedno\r\n'
