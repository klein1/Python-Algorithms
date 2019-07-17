from operator import itemgetter

a = [1, 2, 3]
b = {'a':1,'b':2, 'c':3}

i = itemgetter(1)
print(i(a))  # 2
i = itemgetter('c')
print(i(b))  # (2, 3)
i = itemgetter('b', 'c')
print(i(b))  # 3

rows = [
    {'name': 'CCC', 'id': 1003},
    {'name' : 'BBB', 'id' : 1004},
    {'name': 'EEE', 'id': 1001},
    {'name' : 'DDD', 'id' : 1002},
    {'name': 'AAA', 'id': 1005}
]

rows_by_name = sorted(rows, key=itemgetter('name'))
print(rows_by_name)
rows_by_id = sorted(rows, key=itemgetter('id'))
print(rows_by_id)

print(min(rows, key=itemgetter('id')))
print(max(rows, key=itemgetter('id')))
