def get_max(max_list):
    if len(max_list) > 1 and max_list[0] <= max_list[1]:
        return max_list[1]
    else:
        return max_list[0]

def solve(init_list):
    n = len(init_list)
    if n <= 2:
        return get_max(init_list)

    left_list, right_list = init_list[:n//2], init_list[n//2:]
    left_max, right_max = solve(left_list), solve(right_list)
    return get_max([left_max, right_max])

if __name__ == '__main__':
    test_list = [12, 2, 23, 45, 67, 3, 2, 4, 45, 63, 24, 23]
    print(solve(test_list))