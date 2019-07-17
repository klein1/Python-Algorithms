price  ={
    'A' : 1899,
    'B' : 999,
    'C' : 3999,
    'D' : 2999,
    'E' : 5000
}

print(price.keys())  # dict_keys(['C', 'B', 'E', 'D', 'A'])
print(price.values())  # dict_values([3999, 999, 5000, 2999, 1899])
print(zip(price.values(), price.keys()))  # <zip object at 0x00000181D2901388>
print(*zip(price.values(), price.keys()))  # (3999, 'C') (999, 'B') (5000, 'E') (2999, 'D') (1899, 'A')

min_price = min(zip(price.values(), price.keys()))
print(min_price)  # (999, 'B')

max_price = max(zip(price.values(), price.keys()))
print(max_price)  # (5000, 'E')

sorted_price = sorted(zip(price.values(), price.keys()))
print(sorted_price)  # [(999, 'B'), (1899, 'A'), (2999, 'D'), (3999, 'C'), (5000, 'E')]

print(min(price))  # A
print(max(price))  # E
print(min(price.values()))  # 999
print(max(price.values()))  # 5000
print(min(price, key=lambda k: price[k]))  # B
print(max(price, key=lambda k: price[k]))  # E