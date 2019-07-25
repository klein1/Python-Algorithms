def fib_num(n):
    num_list = [0, 1]
    if n <= 1:
        return num_list[n]
    return fib_num(n - 1) + fib_num(n - 2)

n = 10
for i in range(n):
    print(fib_num(i), end=' ')


# def fib_num(n):
#     a, b = 0, 1
#     while n:
#         print(a, end=" ")
#         a, b = b, a + b
#         n -= 1
#
# fib_num(10)