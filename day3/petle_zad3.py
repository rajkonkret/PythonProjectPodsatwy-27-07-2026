# while - pętla sterowana warunkiem

# pętla nieskończona
# while True:
#     print("Komunikat")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerywa pętle

print(licznik)  # 11
print(50 * "-")

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikt 3 !!!")

# password = input("Podaj hasło:")
# while password != "secret":  # != - rózne
#     password = input("Podaj hasło")
# Podaj hasło:asadasd
# Podaj hasłoaSasasds
# Podaj hasłowqeqweqwwqe
# Podaj hasłosecret

# while (password := input("Podaj hasło:")) != "secret":
#     pass
# Podaj hasło:asasdas
# Podaj hasło:secret

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
# usunąć wszystkie 5 z listy
number_to_remove = 5
while number_to_remove in my_list:
    my_list.remove(number_to_remove)

print(my_list)  # [1, 2, 3, 4, 6]

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
print(dict.fromkeys(my_list))
# {1: None, 5: None, 2: None, 3: None, 4: None, 6: None}
print(list(dict.fromkeys(my_list)))
# [1, 5, 2, 3, 4, 6]
