def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def buha(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

if __name__ == '__main__':
    # a = [5, 5, 2, 1, 9, 1, 5, 10]
    # print(a)
    # print(list(dedupe(a)))

    a = [
        {'x': 2, 'y': 3},
        {'x': 1, 'y': 4},
        {'x': 2, 'y': 3},
        {'x': 2, 'y': 3},
        {'x': 10, 'y': 15},
    ]
    print(a)
    print(list(buha(a, key=lambda a: (a['x'],a['y']))))