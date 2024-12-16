#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    maxi = 0
    sumi = 0
    
    for i in range (len(arr)-2):
        for j in range (len(arr)-2):
            sumi = arr[i+1][j+1]+arr[i][j]+arr[i][j+2]+arr[i][j+1]+arr[i+2][j]+arr[i+2][j+2]+arr[i+2][j+1]
            if(sumi > maxi or (i==0 and j==0)):
                maxi = sumi
    print(maxi)
