import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('A'), 1)
q.push(Item('B'), 4)
q.push(Item('C'), 5)
q.push(Item('D'), 1)
print(q.pop())
print(q.pop())
print(q.pop())

# a = Item('A')
# b = Item('B')
a = (1, Item('A'))
b = (5, Item('B'))
c = (5, Item('C'))
print(a < b)