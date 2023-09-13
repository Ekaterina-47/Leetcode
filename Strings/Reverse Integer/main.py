# function:
def reverse(x):
    x = list(str(x))
    N = len(x)
    for i in range(N // 2):
        x[i], x[N - 1 - i] = x[N - 1 - i], x[i]
    if x[-1] == '-':
        x.insert(0, x.pop())
    s = ""
    for i in x:
        s += i
    x = int(s)
    if x not in range(-2147483648, 2147483647):
        return 0
    return x


# tests:
print(reverse(123))
print(reverse(-123))
print(reverse(1534236469))
