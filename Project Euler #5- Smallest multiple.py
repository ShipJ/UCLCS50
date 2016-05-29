import sys
from sets import Set

num_cases = int(sys.stdin.readline())

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
    return factors

test_cases = []
for i in range(num_cases):
    test_cases.append(int(sys.stdin.readline()))


for i in range(num_cases):
    distinct = Set([])
    prime_factor = Set([])
    prime_factor_list = []
    
    for j in range(2, test_cases[i] + 1):
        vals = prime_factors(j)
        distinct = distinct.union(vals)
        prime_factor_list.append(vals)
    
    mult_list = []
    for j in distinct:
        list = []
        for k in range(test_cases[i] - 1):
            list.append(prime_factor_list[k].count(j))
        mult_list.append(j ** max(list))
    
    result = 1
    for j in range(len(mult_list)):
        result = result * mult_list[j]
        
    print result