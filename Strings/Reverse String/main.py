# function:
def reverseString(s):
    N = len(s)
    for i in range(N // 2):
        s[i], s[N - 1 - i] = s[N - 1 - i], s[i]
    return s

# test:
print(reverseString(["h", "e", "l", "l", "o"]))
