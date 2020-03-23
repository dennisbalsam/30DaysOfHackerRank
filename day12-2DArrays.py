#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    allSums = []

    # loop to go 16 times
    for i in range(len(arr)-2):
        for x in range(len(arr)-2):
            # add the hour glass structure indexes together
            new_sum = sum(arr[i][x:x+3]) + arr[i+1][x+1] + sum(arr[i+2][x:x+3])
            # add sum to array
            allSums.append(new_sum)
    
    # get max sum        
    print(max(allSums))

