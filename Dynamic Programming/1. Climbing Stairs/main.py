# function:
def climbStairs(n):
    S = [0, 1, 2] + [0] * (n - 2)
    for i in range(3, n + 1):
        S[i] = S[i - 2] + S[i - 1]
    return S[n]

# test:
print(climbStairs(10))
print(climbStairs(2))
print(climbStairs(3))

