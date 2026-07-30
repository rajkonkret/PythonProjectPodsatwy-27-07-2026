# funkcja wewnętrzan, zagnieżdzona
# uzywane w dekoratorach

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2 (wew)")

    print(fun2)  # <function fun1.<locals>.fun2 at 0x000001CF18243270>
    # fun2()  # To jest fun2 (wew)
    return fun2  # zwraca adres funkcji, referencja


fun1()  # To jest fun1
# print(fun2)
Xfun = fun1()
print(Xfun)  # <function fun1.<locals>.fun2 at 0x0000023CA3AA3270>
print(type(Xfun))  # <class 'function'>

Xfun()  # To jest fun2 (wew)
Xfun()  # To jest fun2 (wew)
Xfun()  # To jest fun2 (wew)
Xfun()  # To jest fun2 (wew)

czujnik_przod_celcjusz = fun1()
czujnik_przod_celcjusz()
czujnik_przod_celcjusz()
czujnik_przod_celcjusz()
czujnik_przod_celcjusz()
