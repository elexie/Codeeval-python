import sys
file="Practice\\sumOfDigits.txt"
with open(file,'r') as fileLines:
    for line in fileLines:
        sum=0
        for l in line.strip():
            sum+=int(l)
        print(sum)
