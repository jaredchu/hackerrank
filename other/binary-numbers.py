#!/bin/python3

n = int(input().strip())

chars = list(bin(n).lstrip('0b'))
count = 0
max_count = 0

for i in chars:
    if i is '1':
        count += 1
    else:
        count = 0

    if count > max_count:
        max_count = count

print(max_count)
