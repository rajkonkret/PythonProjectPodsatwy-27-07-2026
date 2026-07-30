# import fun1
#
# fun1.dodaj()

import pakiet

print(40 * "-")
# AttributeError: module 'pakiet' has no attribute 'powitanie'
# pakiet.powitanie()

from pakiet import fun

fun.powitanie()

import pakiet.fun as pk  # jako alias

pk.powitanie()

# po dodaniu w __init__.py metoda info() jest widoczna
pakiet.info()

# ----------------------------------------
# Cześć
# Cześć
# Numer pakietu: 2.134.56.89
