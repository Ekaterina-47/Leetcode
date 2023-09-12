# Найти первый неповторяющийся символ в строке и вернуть индекс. Если его нет, то -1


# получилось, но очень долго
def firstUniqChar(s):
    s_counts = []
    for i in s:
        count = 0
        for x in s:
            if x == i:
                count += 1
        s_counts.append(count)
    for i in range(0, len(s_counts)):
        if s_counts[i] == 1:
            return i
    return -1


print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("аабб"))


def firstUniqChar1(s):
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


print(firstUniqChar1("leetcode"))
print(firstUniqChar1("loveleetcode"))
print(firstUniqChar1("аабб"))
