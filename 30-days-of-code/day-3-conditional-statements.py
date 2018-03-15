#!/bin/python3

N = int(input().strip())
if(N%2 is not 0 or 6 <= N <= 20):
    print('Weird')
else:
    print('Not Weird')