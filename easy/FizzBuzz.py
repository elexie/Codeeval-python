import sys
"""
https://www.codeeval.com/open_challenges/1/
sample space:
F B
t f: fizz
f t: buzz
f f: i
t t: fizzbuzz
"""
fileName="Practice\\fizzbuzz.txt"

with open(fileName,'r') as fileLines:
    for line in fileLines:
        output=""
        if not line.isspace():
            lineList=line.strip().split(' ') #convert the string of digits to a 'list'
            lineList=list(map(int,lineList)) #convert the 'list of strings' to a 'list of ints'
            limit=lineList[2]+1
            for i in range(1,limit):
                fizz=i%lineList[0]==0
                buzz=i%lineList[1]==0
                if fizz and not buzz:
                    output+="F "
                if buzz and not fizz:
                    output+="B "
                if not fizz and not buzz:
                    output+=str(i)+" "
                if fizz and buzz:
                    output+="FB "
            print(output.strip())
