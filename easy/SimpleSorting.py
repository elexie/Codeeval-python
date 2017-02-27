"""
https://www.codeeval.com/open_challenges/91/
"""


def insertionSort(arr):
    arr=[float(s) for s in arr] #convert arr to an array of floats
    toMoveLeft = 0
    j = 0
    for i in range(1, len(arr)):
        toMoveLeft = arr[i]
        j = i
        while (j > 0 and arr[j - 1] > toMoveLeft):
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = toMoveLeft
    return arr


unsorted = ['-13.408', '-21.041', '-35.562', '-38.391', '-56.554',
            '-58.526', '-65.699', '-7.986', '-70.399', '-87.549', '-94.962']

file = open('Practice\simpleSort.txt')
for line in file:
    sorted=insertionSort(line.split()) #list
    converted=[str(s) for s in sorted] #convert the list of floats to a list of strings
    # (otherwise the .join() method would not work)
    print(' '.join(converted))

