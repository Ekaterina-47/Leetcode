# function:
def isPalindrome(s):
    s1 = ""
    for i in s:
        if i.isalpha() or i.isdigit():
            s1 += i
    s1 = s1.lower()
    s2 = ''.join(reversed(s1))
    if s1 == s2:
        return True
    else:
        return False

# tests:
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
print(isPalindrome("0P"))