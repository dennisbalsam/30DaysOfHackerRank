#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    names = []

    for N_itr in range(N):



        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        z = re.search("@gmail.com", emailID)

        if z:
            names.append(firstName)

    
    
    names.sort()
    for name in names:
        print(name)