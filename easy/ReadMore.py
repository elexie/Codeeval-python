import sys

def parseLines(line):
    length=len(line)
    if(length<=55):
        print(line)
    else:
        line=line[:40].strip()+"...<Read More>"
        print(line)

file="Practice\\readMore.txt"
with open(file,'r') as fileLines:
    for line in fileLines:
        parseLines(line.strip())