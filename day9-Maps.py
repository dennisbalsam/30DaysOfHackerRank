
# Enter your code here. Read input from STDIN. Print output to STDOUT
entries = int(input())
phoneBook = {}
for i in range(entries):
    entry = str(input()).split(' ')
    newEntry = {entry[0]: entry[1]}
    phoneBook.update(newEntry)


while True:
    try:
        search = input()
        if search in phoneBook:
            print('{0}={1}'.format(search,phoneBook[search]))
        else:
            print('Not found')
    except:
        break
        