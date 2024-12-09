# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

thisdict = dict()

for i in range(n):
    x = input()
    thisdict[x.split()[0]] = x.split()[1]
#print (thisdict)

y = input()

try:
    while (y):
        if(thisdict.get(y) is not None):
            print(str(y), end="")
            print("=",end="")
            print(thisdict.get(y))
        else:
            print("Not found")
        y = input()
except:
    quit()
