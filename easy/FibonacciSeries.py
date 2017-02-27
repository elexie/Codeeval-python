import sys
def fib(n):
    ans=0
    if n<=2 :
        if n==0 :
            ans=0
        else :
            ans=1
    else :
        ans=fib(n-1)+fib(n-2)

    return ans

filename="practice\\fib.txt"
with open(filename,'r') as test_cases:
    for test in test_cases:
        print(fib(int(test.strip())))
