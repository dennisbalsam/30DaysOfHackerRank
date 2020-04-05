# Enter your code here. Read input from STDIN. Print output to STDOUT

# inputs are stripped and put into an array in format [day, month, year]

realReturn = str(input()).split(' ')
expectedReturn = str(input()).split(' ')
fine = 0

if realReturn[2] > expectedReturn[2]:
    fine = 10000
elif realReturn[2] == expectedReturn[2]:
    if int(realReturn[1]) > int(expectedReturn[1]):
        fine = (int(realReturn[1]) - int(expectedReturn[1])) * 500
    elif realReturn[1] == expectedReturn[1] and int(realReturn[0]) > int(expectedReturn[0]):
        fine = (int(realReturn[0]) - int(expectedReturn[0])) * 15

print(fine)

