# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for i in range (n):
    x = input()
    print(x[::2], x[1::2])

