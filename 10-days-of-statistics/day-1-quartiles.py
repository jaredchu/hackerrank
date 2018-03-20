import math

def get_median(arr):
    n = len(arr)
    if n % 2 is 0:
        median = (arr[int((n / 2) - 1)] + arr[int(n / 2)]) / 2
    else:
        median = arr[int(math.floor(n / 2))]

    return int(median)

n = int(input().strip())
arr = sorted(map(int, input().strip().split(" ")))

median = get_median(arr)
print(get_median(arr[:math.floor(n/2)]))
print(median)

if(n % 2 is 0):
    upper_arr = arr[math.floor(n / 2):]
else:
    upper_arr = arr[math.floor(n / 2) + 1:]
print(get_median(upper_arr))