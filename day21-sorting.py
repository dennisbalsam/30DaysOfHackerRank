#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numSwaps = 0

for i in range(n):
    numOfSwaps = 0

    for j in range(n-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            numOfSwaps += 1
    
    if numOfSwaps == 0:
        break

    numSwaps += numOfSwaps


print('Array is sorted in {0} swaps.'.format(numSwaps))
print('First Element: {0}'.format(a[0]))
print('Last Element: {0}'.format(a[len(a)-1]))

