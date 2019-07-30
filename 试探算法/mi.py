maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]]

m, n = 8, 10  # 8行10列
entry = (1, 0)  # 迷宫入口
path = [entry]  # 一组解
paths = []  # 保存所有解

# 可以移动的方向
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def conflict(nx, ny):
    global m, n, maze

    if 0<= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
        return False

    return True

def walk(x, y):
    global entry, m, n, maze, path, paths, directions

    if (x, y) != entry and (x % (m - 1) == 0 or y % (n - 1) == 0):  # 找到出口
        paths.append(path[:])  # 得到一组解
    else:
        for d in directions:
            nx, ny = x + d[0], y + d[1]
            path.append((nx, ny))  # 向前试探
            if not conflict(nx, ny):  # 剪枝
                maze[nx][ny] = 2
                walk(nx, ny)
                maze[nx][ny] = 0
            path.pop()  # 回溯

def show(path):
    global maze

    import pprint, copy

    maze2 = copy.deepcopy(maze)

    for p in path:
        maze2[p[0]][p[1]] = 2

    pprint.pprint(maze)
    print()
    pprint.pprint(maze2)

walk(*entry)
print(paths[-1], '\n')
show(paths[-1])
