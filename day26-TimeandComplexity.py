import math

# Enter your code here. Read input from STDIN. Print output to STDOUT


def findPrime(prime):
    for i in range(2,int(math.sqrt(prime) + 1)):
        if prime % i == 0:
            return 'Not prime'
    return 'Prime'


quantity = int(input())

for i in range(quantity):
    num = int(input())

    if num > 1:
        print(findPrime(num))
    
    else:
        print('Not prime')

        
