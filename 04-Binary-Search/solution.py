#!/bin/python3

import math
import os
import random
import re
import sys


def introTutorial(V, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == V:
            return mid
        elif arr[mid] < V:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
