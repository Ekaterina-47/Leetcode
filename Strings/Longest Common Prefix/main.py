# function:
def longestCommonPrefix(strs):
    s = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(s) != 0:
            s = s[: -1]
    if len(s) == 0:
        return ""
    return s

# tests:
print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
