#!/bin/python3

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(' '.join(str(x) for x in list(reversed(arr))))