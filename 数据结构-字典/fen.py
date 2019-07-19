from itertools import groupby
from operator import itemgetter

things = [('2012-05-21', 11), ('2012-05-21', 3), ('2012-05-22', 10),
          ('2012-05-22', 4), ('2012-05-22', 22), ('2012-05-23', 33)]
for key, items in groupby(things, itemgetter(0)):
    print(key, items)

