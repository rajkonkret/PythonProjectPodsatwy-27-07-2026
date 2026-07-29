import pandas

#  pip install pandas

# data = pandas.read_csv('records_discount.csv')
data = pandas.read_csv('records_discount_semicolon.csv', delimiter=";")
print(data)
#    sku  exp_date    price
# 0    1     today   200.00
# 1    2     today   300.00
# 2    3     today   200.00
# 3    4  tomorrow   400.00
# 4    5     today   250.00
# 5    6     today  1200.00
# 6    7  tomorrow   800.00
# 7    8     today   200.99

print(data.columns)
# Index(['sku', 'exp_date', 'price'], dtype='str')

print(data.values)
# [[1 'today' 200.0]
#  [2 'today' 300.0]
#  [3 'today' 200.0]
#  [4 'tomorrow' 400.0]
#  [5 'today' 250.0]
#  [6 'today' 1200.0]
#  [7 'tomorrow' 800.0]
#  [8 'today' 200.99]]

print(data.items)
# <bound method DataFrame.items of    sku  exp_date    price
# 0    1     today   200.00
# 1    2     today   300.00
# 2    3     today   200.00
# 3    4  tomorrow   400.00
# 4    5     today   250.00
# 5    6     today  1200.00
# 6    7  tomorrow   800.00
# 7    8     today   200.99>
