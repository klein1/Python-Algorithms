a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'x' : 11,
    'y' : 2,
    'z' : 10
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())

c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)