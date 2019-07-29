def greedy(n ,k, d):
    num = 0  # 加油次数
    for i in range(k):
        if d[i] > n:
            print('no solution')
            return

    i, s = 0, 0
    while i <= k:
        s += d[i]
        if s >= n:
            s = d[i]
            num += 1
        i += 1

    print(num)

if __name__ == '__main__':
    n = 100  # 加满油可行驶的距离
    k = 5  # 加油站数量
    d = [50, 80, 39, 60, 40, 32]  # 加油站之间的距离
    greedy(n, k, d)
