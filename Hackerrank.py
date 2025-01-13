#Write your code here
class Calculator:
    def __init__(self):
        pass
    def power(self,n,p):
        if(n < 0 or p < 0):
            return "n and p should be non-negative"
        sum = 1
        for i in range(p):
            sum = sum * n
        return sum

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
