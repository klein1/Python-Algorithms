# 传统方式
numbers = []
for x in range(30):
    if x % 3 == 0:
        numbers.append(x*x)
print(numbers)

# 列表推导式
multiples = [i*i for i in range(30) if i % 3 is 0]
print(multiples)