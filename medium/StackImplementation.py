"""
https://www.codeeval.com/open_challenges/9/
"""
file="Practice\\stack.txt"

with open(file) as fileLines:
    for line in fileLines:
        output=""
        #convert the line of strings to a 'list'
        lineList=list(line.strip().split(" "))
        x=1
        while x<= len(lineList):
            output+=str(lineList[-1*x])+" "
            x+=2
        print(output.strip())
