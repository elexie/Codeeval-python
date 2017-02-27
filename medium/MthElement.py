import sys

fileName="Practice\\MthElement.txt"
with open(fileName,'r') as fileLines:
    for line in fileLines:
        lineList=list(line.strip().split(" "))
        index=(int(lineList[-1]))
        if index>1 and index<len(lineList):
            print(lineList[(len(lineList)-1)-index])