from sys import argv
from itertools import cycle

my_list = [1, 7, 'Hello', 'World', 3, 2.5]
c = 0
for el in cycle(my_list):
    if c > int(argv[1]):
        break
    print(el)
    c += 1
