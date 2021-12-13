from random import randrange

list_0 = [randrange(0, 401) for i in range(0, 12)]

print(list_0)
print(len(list_0))

list_1 = []
for i in range(1, len(list_0)):
    if list_0[i] > list_0[i-1]:
        list_1.append(list_0[i])
print(list_1)