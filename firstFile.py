import platform
import sys
from collections import namedtuple
import random as r

tupl = namedtuple('Cars', 'brand, color, speed')
cc = tupl('BMW', 'Yellow', '225')

fruits = ["apple", "banana", 'cherry']
x1, y1, z1 = fruits

a1 = r.randrange(1, 6, 2)

# x2 = input('Type first number: ')
# y2 = input('Type second number: ')
# print('Addition is: ', int(x2) + int(y2))

fruits = ["cherry", "Banana", "apple", "Mango", "kiwi"]
# new_fruits_list = [x for x in fruits if 'a' not in x]
# print(new_fruits_list)

a2 = {"two", "one", 4}
b2 = {"three"}
c2 = a2.union(b2)
a2.update(b2)
# print(c2)
# print(a2)

a3 = {
    "one": [1, 2],
    "two": 2,
    "three": {
        'four': 4
    }
}
# print(a3)
# print(a3['three']['four'])
# for x, y in a3.items():
#     print(x, y)

a4 = 10
b4 = 20
# print(a4, 'is greater than', b4) if a4 > b4 else print(b4, 'is greater than', a4)

# for i in range(2, 10, 3):
#     if i == 8:
#         pass
#     print(i)
# else:
#     print('Finished!')
# print('Anyway!')

a = 0o77
print(a)

