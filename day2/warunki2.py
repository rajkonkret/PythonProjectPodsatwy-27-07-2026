# od pythona 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania:")

match lang.strip().casefold():
    case "python":
        lista.append("Znam pythona")
    case "java":
        lista.append("Znam jave")
    case "c":
        lista.append("Znam C")
    case _:
        print("Nie znam takiego języka")

print(lista)
# Podaj znany Ci język programowania:java
# ['Znam jave']

lista = [1, 2]
# lista = [1, 2, 3]

match lista:
    case [a, b]:
        print(a, b)
    case [a, b, c]:
        print(a, b, c)
    case _:
        print("inny")
# 1 2
