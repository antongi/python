from sys import argv
from itertools import count

for i in count(int(argv[1])):
    if i > 10:
        break
    else:
        print(i)
print(i)
