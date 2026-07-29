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

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'utf-8',
# 'confidence': 0.8340298507462687,
# 'language': 'pl',
# 'mime_type': 'text/plain'}
encoding = result['encoding']
print("Kodowanie:", encoding)
confidence = result['confidence']
print("Trafność:", confidence)
# Kodowanie: utf-8
# Trafność: 0.8963380281690141

print(50 * "-")
print(raw_data.decode(encoding=encoding))
# --------------------------------------------------
# Powitanie
# Jeszcze jedno
# Dodane
# Dodane
# Dśąćodane
# Jeszcze jedno
# ctrl shift f - wyszukiwanie w projekcie
