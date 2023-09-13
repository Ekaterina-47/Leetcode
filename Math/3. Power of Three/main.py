# function:
def isPowerOfThree(n):
    a = False
    for i in range(-20, 20):
        if 3**i == n:
            a = True

    if a:
        return True
    else:
        return False



# tests:
print(isPowerOfThree(27))
print(isPowerOfThree(0))
print(isPowerOfThree(-1))