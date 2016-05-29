import sys

num_cases = int(sys.stdin.readline())

test_cases = []
for i in range(num_cases):
    test_cases.append(int(sys.stdin.readline()))

def sum_squares(n):
    sum_square = 0
    for i in range(n + 1):
        sum_square = sum_square + (i ** 2)
    return sum_square
    
def square_sum(n):
    square_sum = (((n * (n + 1)) / 2) ** 2)
    return square_sum
    
for i in range(num_cases):
    print abs(sum_squares(test_cases[i]) - square_sum(test_cases[i]))