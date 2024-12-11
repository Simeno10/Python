#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    n = str(bin(n))
    maxi = 0
    count = 0
    for i in range(len(n)):
        if(n[i]=='1'):
            count +=1
        elif(maxi<count):
            maxi = count
            count = 0
        else:
            count = 0
    if(maxi<count):
        maxi = count
    print(maxi)
