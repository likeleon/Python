a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])

print(len(c))
print(list(c.keys()))
print(list(c.values()))

c['z'] = 10
c['w'] = 40
del c['x']
print(a)
#del c['y']


#
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)

print(values['x'])
values = values.parents
print(values['x'])
values = values.parents
print(values['x'])


#
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])
