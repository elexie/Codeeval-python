"""
https://www.codeeval.com/open_challenges/82/

"""


def isArmstrongNumber(line):
    """Determine if armstrong
    number """
    squaredSum = 0
    getNum = 0
    for i in list(line):
        i = i.strip()
        if len(i) > 0:
            getNum = int(line)
            squaredSum += (int(i) ** len(line.strip()))

    print(getNum==squaredSum)


fileName = "Practice/Armstrong.txt"
file = open(fileName, 'r')
for line in file:
    if (len(line)) > 0:
        isArmstrongNumber(line)
