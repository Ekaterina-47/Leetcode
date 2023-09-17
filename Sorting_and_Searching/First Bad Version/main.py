# function:
def firstBadVersion(n):
    if isBadVersion(1) == True:
        return 1
    if isBadVersion(1) == True:
        return 2
    left = 1
    right = n
    while right - left >= 2:
        middle = (left + right) // 2
        if isBadVersion(middle) == True:
            right = middle
        else:
            left = middle
    return right
