record = '....................100         ........513.25   .......'

print(int(record[20:32]))
print(float(record[40:49]))

SHARES = slice(20, 32)
PRICE = slice(40, 48)

print(int(record[SHARES]))
print(float(record[PRICE]))


#
items = [0, 1, 2, 3, 4, 5, 6]
print(items[2:4])

a = slice(2, 4)
print(items[a])

items[a] = [10,11]
print(items)

del items[a]
print(items)


#
a = slice(10, 40, 2)
print(a.start)
print(a.stop)
print(a.step)


#
s = 'HelloWorld'
a = slice(5, 10, 2)
a.indices(len(s))
print(a)
for i in range(*a.indices(len(s))):
    print(s[i])