# napisać funkcję obliczającą średnią

def srednia(*cyfry):  # dowolna ilośc elemntów przekazanych po pozycji
    print(cyfry)

    count = len(cyfry)

    suma = 0
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
    except Exception as e:
        print("Bład:", e)
    else:
        print(f"Srednia ocen: {avg}")
    finally:
        print("Następny uczeń")


srednia()
srednia(1)
srednia(1, 2)
