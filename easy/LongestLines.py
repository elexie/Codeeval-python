import sys

fileName="Practice\\Longestlines.txt"
length=0
temp=length
longest=''
lineIndex=0
with open(fileName,'r') as lines:

    for l in lines:
        temp=len(l)
        if temp>length:
                length=temp
                longest=l
    lineIndex+=1

