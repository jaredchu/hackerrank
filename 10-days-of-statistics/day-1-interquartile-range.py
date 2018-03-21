import math

z = int(input().strip())
a = list(map(int, input().strip().split(" ")))
b = list(map(int, input().strip().split(" ")))

arr = []
y = 0
for i in b:
    for x in range(i):
        arr.append(a[y])
    y += 1
arr = sorted(arr)


def get_median(arr):
    n = len(arr)
    if n % 2 is 0:
        median = (arr[int((n / 2) - 1)] + arr[int(n / 2)]) / 2
    else:
        median = arr[int(math.floor(n / 2))]

    return median


def split_list(arr):
    n = len(arr)
    if n % 2 is 0:
        return arr[:n // 2], arr[n // 2:]
    else:
        return arr[:n // 2], arr[n // 2 + 1:]


lower, upper = split_list(arr)
print(float(get_median(upper) - get_median(lower)))
