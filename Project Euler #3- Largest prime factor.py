import sys

T = int(sys.stdin.readline())

test_cases = []
for i in range(T):
    test_cases.append(int(sys.stdin.readline()))
    
# Function to compute largest prime factors
def largest_prime(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
    return max(factors)

for i in range(T):
    print largest_prime(test_cases[i])