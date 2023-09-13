# function:
def firstUniqChar(s):
    s = list(s)
    d = {}
    s1 = set(s)
    for i in range(len(s)):
        if s[i] not in d and s[i] in s1:
            d[s[i]] = i
            s1.discard(s[i])
        elif s[i] in d:
            del d[s[i]]
    if len(d) > 0:
        return d[list(d.keys())[0]]
    else:
        return -1

# tests:
print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("аабб"))
