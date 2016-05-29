import sys
import string
from sets import Set

def palindrome(n):
    if str(n)[::-1] == str(n):
        return True
    else:
        return False
    
div_list = []
for i in range(100, 1000):
    for j in range(100, 1000):
        div_list.append(i * j)
        
palindrome_list = []
for i in range(10000, 998002):
    if palindrome(i):
        palindrome_list.append(i)
        
intersect_list = Set(div_list).intersection(Set(palindrome_list))

num_cases = int(sys.stdin.readline())
for i in range(num_cases):
    test = int(sys.stdin.readline())
    max_val = max([i for i in intersect_list if i < test])
    print max_val