def all_aparam(a, b, /, c=42, d=345):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")


all_aparam(1, 2)
all_aparam(1, 2, 3, 4)
# a=1, b=2
# c=3, d=4

all_aparam(1, 2, c=8)
all_aparam(1, 2, c=8, d=90)


# a=1, b=2
# c=8, d=90

# / oddziela pozyyjne od pozostałych
# all_aparam(a=1, b=2, c=90) # c=90, d=345
# TypeError: all_aparam() got some positional-only arguments passed as keyword arguments: 'a, b'

def all_params_full(name, b, /, c=42, *args, d=67, **kwargs):
    print(f"{name=}, {b=}")
    print(f"{c=}, {d=}")
    print(f"{args=}, {kwargs=}")


all_params_full(1, 2)
all_params_full(1, 2)
all_params_full(1, 2, 3)  # c=3, d=67
all_params_full(1, 2, 3, 4, 5, 6, 7)  # args=(4, 5, 6, 7), kwargs={}
all_params_full(1, 2, 3, 4, 5, 6, 7, d="radek")  # c=3, d='radek'
all_params_full(1, 2, 3, 4, 5, 6, 7, d="radek", name="Tomek")  # args=(4, 5, 6, 7), kwargs={'name': 'Tomek'}
