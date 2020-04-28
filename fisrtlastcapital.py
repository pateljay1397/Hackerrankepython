# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 17:45:38 2020

@author: patel
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s= s[1].capitalize()
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
