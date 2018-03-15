def rotate_right(a, n):
    return a[-n:] + a[:-n]


def rotate_left(a, n):
    return a[n:] + a[:n]


def array_left_rotation(a, n, k):
    return rotate_left(a, k)


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')