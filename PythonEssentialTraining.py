# Python code​​​​​​‌‌​​​‌​‌‌‌‌‌‌​​‌​​​​‌​​​‌ below

def encodeString(stringVal):
    count = 1
    myList = []
    for i in range(len(stringVal)-1):
        if (stringVal[i]==stringVal[i+1]):
            count += 1
        else:
            myList.append((stringVal[i], count))
            count = 1
    myList.append((stringVal[-1], count))
    count = 1
    return myList


def decodeString(encodedList):
    word = ''
    for i in encodedList:
        for j in range (i[1]):
            word+=i[0]
    return word
