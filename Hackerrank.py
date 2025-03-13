def isPrime(x):
    if x < 2:
        return "Not prime"
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return "Not prime"
    return "Prime"
n = int(input())
for i in range (n):
    x = int(input())
    print(isPrime(x))
