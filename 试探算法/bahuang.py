n = 8
x = []  # 遍历过程中的一组解
X = []  # 用来保存所有解

def conflict(k):
    global x

    for i in range(k):
        if x[i] == x[k] or abs(x[i] - x[k]) == abs(i - k):  # 判断不在同一列，且不在同一条斜线上
            return True
    return False

def queens(k):  # 摆放第 k 行
    global n, x, X

    if k >= n:
        X.append(x[:])  # 得到一组解
    else:
        for i in range(n):
            x.append(i)  # 向前试探
            if not conflict(k):  # 剪枝
                queens(k + 1)
            x.pop()  # 回溯

def show(x):
    global n

    for i in range(n):
        print('. '*(x[i]) + 'X ' + '. ' * (n - x[i] - 1))

queens(0)
print(len(X))
print(X[-1], '\n')
show(X[-1])