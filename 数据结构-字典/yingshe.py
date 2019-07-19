from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(3)
print(d)

d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(3)
print(d)

print(min((2, 3, 4)))