p = (4, 5, 6)
x, y, z = p
print(x)
print(y)
print(z)

# x, y = p
# print(x, y)

records = [
    ('A', 1, 2),
    ('B', 'hello'),
    ('C', 5, 3)
]

def do_A(x, y):
    print('A', x, y)

def do_B(s):
    print('B', s)

for tag, *args in records:
    if tag == 'A':
        do_A(*args)
    elif tag == 'B':
        do_B(*args)


line = 'www.computer.com/dsffe-3fdcd.d/we/index.html'
domain, *uri, file = line.split('/')
print(domain)
# print(uri)
print(file)

