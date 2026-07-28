import random

# działania na liczbach losowych
"""Return random integer in range [a, b], including both end points.
 """
print(random.randint(1, 100))  # int od 1 do 100

print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # int od 0 do 4

print(random.random())  # 0.16289821245163705 float od 0 do 0.9999999
print(random.random() * 7)  # 1.1609510548715591 float od 0 do 6.99999999


