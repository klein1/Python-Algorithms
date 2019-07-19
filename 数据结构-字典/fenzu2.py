from collections import defaultdict

things = [('2012-05-21', 1), ('2012-05-21', 3), ('2012-05-22', 2),
          ('2012-05-22', 4), ('2012-05-22', 2), ('2012-05-23', 4)]

rows = defaultdict(list)
for row in things:
    rows[row[1]].append(row)

for i, data in rows.items():
    print(i)
    for j in data:
        print(' ', j)