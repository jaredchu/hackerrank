from collections import Counter
import math

n = int(input().strip())
arr = map(int, input().strip().split(" "))

sorted_arr = sorted(arr)
counted = Counter(sorted_arr)

mean = sum(sorted_arr) / n

if n % 2 is 0:
    median = (sorted_arr[int((n / 2) - 1)] + sorted_arr[int(n / 2)])/2
else:
    median = sorted_arr[int(math.ceil(n / 2))]

max_occur = 0
mode = 0
for i in sorted_arr:
    if counted[i] > max_occur:
        max_occur = counted[i]
        mode = i

print(mean)
print(median)
print(mode)
