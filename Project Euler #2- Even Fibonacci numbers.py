import sys

num_cases = int(sys.stdin.readline())
test_cases = []
for i in range(num_cases):
    test_cases.append(sys.stdin.readline())
test_cases = [int(i) for i in test_cases]

def fibonacci_even(n):
    i = 1
    j = 2
    seq = [i, j]
    while max(seq) < n:
        i = i + j
        j = i + j
        seq.append(i)
        seq.append(j)
    even_seq = []
    for k in range(len(seq)):
        if seq[k] % 2 == 0:
            even_seq.append(seq[k])
    fib_sum = 0
    fib_sum = [fib_sum + even_seq[i] for i in range(len(even_seq)) if even_seq[i] < n]
    return sum(fib_sum)

for i in range(num_cases):
    print fibonacci_even(test_cases[i])