import math

n = int(input().strip())
arr = sorted(map(int, input().strip().split(" ")))

mean = sum(arr) / n
total = 0
for i in arr:
    total += (i - mean) ** 2

print(round(math.sqrt(total / n), 1))
