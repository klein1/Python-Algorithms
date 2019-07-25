i = 1

def move(n, mfrom, mto):
    global i
    print("第%d步：将%d号盘子从%s -> %s" % (i, n, mfrom, mto))
    i += 1

def hanoi(n, A, B, C):
    if n == 1:
        move(1, A, C)
    else:
        hanoi(n - 1, A, C, B)
        move(n, A, C)
        hanoi(n - 1, B, A , C)


n = 2
hanoi(n, 'A', 'B', 'C')
