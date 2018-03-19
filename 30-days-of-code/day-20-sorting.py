n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swap_num = 0
for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j+1] = a[j+1], a[j]
            swap_num += 1

print("Array is sorted in {} swaps.".format(swap_num))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
