# Enter your code here. Read input from STDIN. Print output to STDOUT
numtestcases = int(input())


for i in range(numtestcases):
    # get input
    word = input()
    # Separating odd and even index elements 
    print(word[::2], word[1::2])