from __future__ import print_function
import sys

num_cases = int(sys.stdin.readline())
test_cases = []
for i in range(num_cases):
    test_cases.append(sys.stdin.readline())
    
test_cases = [int(i) for i in test_cases]
max_N = max(test_cases)

def summation(num):
    return (num * (num + 1)) / 2 
    
for i in range(num_cases):
    mult_3 = test_cases[i] - 1
    mult_5 = test_cases[i] - 1
    mult_15 = test_cases[i] - 1
    
    while (mult_3 % 3 != 0 and mult_5 != 0 and mult_15 != 0):
        if mult_3 % 3 != 0:
            mult_3 = mult_3 - 1
        if mult_5 % 5 != 0:
            mult_5 = mult_5 - 1
        if mult_15 % 15 != 0:
            mult_15 = mult_15 - 1
  
    result = (3 * summation(mult_3 / 3) + 5 * summation(mult_5 / 5)) - (15 * summation(mult_15 / 15))      
    print result