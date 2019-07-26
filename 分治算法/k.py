def partition(seq):
    pi = seq[0]
    lo = [x for x in seq[1:] if x <= pi]
    hi = [x for x in seq[1:] if x > pi]
    return lo, pi, hi

def select(seq, k):
    lo, pi, hi = partition(seq)

    m = len(lo)
    if m == k - 1:
        return pi
    elif m < k - 1:
        return select(hi, k - 1 - m)
    else:
        return select(lo, k)

if __name__ == '__main__':
    test_list = [5, 2, 8, 7, 6, 3, 1, 4, 9, 10, 12, 11]
    print(select(test_list, 7))
    print(select(test_list, 3))
