import sys
"""
https://www.codeeval.com/open_challenges/96/
"""
"""
for the sake of practice, I have
decided to solve the puzzle using
this method, even though it is
more wordy.
"""
def swapCase(line):
    output=''
    line=line.strip()
    for l in line:
        if l.isalpha():
            if l.islower():
                output+=l.upper()+''
            else:
                output+=l.lower()+''
        else:
            output+=l+''
    return output.strip()



fileName="Practice\\swapCase.txt"
with open(fileName,'r') as fileLines:
    for lines in fileLines:
        #either method works
        #print(swapCase(lines))
        print(lines.swapcase().strip())

