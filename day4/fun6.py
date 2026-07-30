# napisać funkcję obliczającą średnią
# statistics - funkcje staystyczne np.: Średnia (mean)
import statistics


def srednia(name=None, *cyfry):  # dowolna ilośc elementów przekazanych po pozycji
    print(cyfry)

    count = len(cyfry)

    suma = 0
    suma_p = sum(cyfry)
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
        avg_p = suma_p / count
    except Exception as e:
        print("Bład:", e)
    else:
        print(f"Srednia dla ucznia {name} wynosi: {avg}")
        print(f"Srednia dla ucznia {name} wynosi: {avg_p}")
        print(f"Srednia dla ucznia {name} wynosi:{statistics.mean(cyfry)}")
    finally:
        print("Następny uczeń")


srednia()
srednia(1)
srednia(1, 2)

srednia("Radek", 6, 7, 8, 6, 7, 8, 8, 6)
name, *cyfra = "Radek", 6, 7, 8, 6, 7, 8, 8, 6
