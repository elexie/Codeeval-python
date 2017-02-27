import sys
fileName="Practice\\evenNumbers.txt"
with open(fileName,'r') as fileLines:
    for line in fileLines:
        isEven=int(line)%2==0
        if isEven:
            print(1)
        else:
            print(0)