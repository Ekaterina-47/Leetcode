#function:
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    for i in t:
        if i in s:
            s = s.replace(i, "", 1)
        else:
            return False
    return True

# tests:
print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram("ab", "a"))
print(isAnagram("aa", "a"))


