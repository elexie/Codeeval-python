"""
https://www.codeeval.com/open_challenges/8/
"""

import sys

file="Practice//reverseWords.txt"
with open(file,'r') as fileLines:
    for lines in fileLines:
        output=''
        lineList=lines.strip().split(' ')
        for x in range(1,len(lineList)+1):
            output+=lineList[-1*x]+' '
        print(output.strip())
