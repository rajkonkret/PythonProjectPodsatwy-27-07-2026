def connect(**opcje):  # dowolna liczba argumentów po nazwie (keywords)
    print(opcje)  # {}
    name = opcje.get('name')
    print(name)


connect()
connect(a=10)
connect(a=10, b=90)  # {'a': 10, 'b': 90}
connect(a=10, b=90, name="Radek")  # {'a': 10, 'b': 90}


def all_args(*args, **kwargs):
    print(args, kwargs)


all_args(1, 2, 3, 4, 5, 6, name="Radek")
all_args(1, 2, )
# (1, 2, 3, 4, 5, 6) {'name': 'Radek'}
# (1, 2) {}
