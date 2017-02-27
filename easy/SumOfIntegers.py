import sys

fileName="Practice\\sumOfInteger.txt"
sum=0
with open(fileName) as fileLines:
    lines=fileLines.readlines()

for l in lines:
    if not (l.isspace()):
        sum+=int(l)
print(sum)
