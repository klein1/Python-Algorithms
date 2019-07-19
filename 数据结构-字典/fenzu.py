from itertools import groupby
from operator import itemgetter

things = [('2012-05-21', 1), ('2012-05-21', 3), ('2012-05-22', 2),
          ('2012-05-22', 2), ('2012-05-22', 4), ('2012-05-23', 4)]

things.sort(key=itemgetter(1))
for data,items in groupby(things, key=itemgetter(1)):
    print(data)
    for i in items:
        print(' ', i)