#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    gmail_users = []
    
    for _ in range(N):
        firstName, emailID = input().rstrip().split()
        
        if emailID.endswith("@gmail.com"):
            gmail_users.append(firstName)
    
    for name in sorted(gmail_users):
        print(name)
