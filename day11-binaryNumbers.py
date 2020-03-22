#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    # get binary version
    n = bin(n)

    # set max 
    consones = 0
    count = 0

    for i in range(len(n)):
        if n[i] == '1':
            count += 1
            consones = max(consones, count)
        

        else:
            count = 0
    
    print(consones)
