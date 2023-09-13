# function:
def countPrimes(n):
    if n == 0 or n == 1:
        return 0
    count = 0
    A = [True]*n
    A[0] = A[1] = False
    for k in range(2, n):
        if A[k]:
            for m in range(2*k, n, k):
                A[m] = False
    for k in range(n):
        if A[k]:
            count += 1
    return count

# tests:
print(countPrimes(10))
print(countPrimes(0))
print(countPrimes(1))
print(countPrimes(3))