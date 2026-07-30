# import fun1
#
# fun1.dodaj()

import pakiet

# AttributeError: module 'pakiet' has no attribute 'powitanie'
# pakiet.powitanie()

from pakiet import fun

fun.powitanie()

import pakiet.fun as pk  # jako alias

pk.powitanie()
