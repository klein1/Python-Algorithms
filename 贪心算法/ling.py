def main():
    d = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]  # 存储每种硬币的面值
    d_num = []  # 存储每种硬币的数量
    s = 0  # 拥有的零钱总和

    temp = input('请输入每种零钱的数量：')
    d_num0 = temp.split(' ')

    for i in range(0, len(d_num0)):
        d_num.append(int(d_num0[i]))
        s += d[i] * d_num[i]

    sum = float(input('请输入需要找的零钱：'))

    assert s >= sum

    # 从数组中最大面值的元素开始遍历
    i = len(d) - 1
    while i >= 0:
        if sum >= d[i]:
            n = int(sum / d[i])
            if n >= d_num[i]:
                n = d_num[i]
            sum -= n * d[i]
            print('用了%d个%f枚硬币'%(n, d[i]))
        i -= 1

if __name__ == '__main__':
    main()

