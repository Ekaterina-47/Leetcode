# function:
def romanToInt(s):
    a = 0
    for i in range(len(s)):
        if i != len(s) - 1:
            if s[i] == 'I' and s[i+1] == 'V':
                a += 4
                continue
            if s[i] == 'I' and s[i+1] == 'X':
                a += 9
                continue
            if s[i] == 'X' and s[i+1] == 'L':
                a += 40
                continue
            if s[i] == 'X' and s[i+1] == 'C':
                a += 90
                continue
            if s[i] == 'C' and s[i+1] == 'D':
                a += 400
                continue
            if s[i] == 'C' and s[i+1] == 'M':
                a += 900
                continue
        if i != 0:
            if (s[i-1] == 'I' and s[i] == 'V') or (s[i-1] == 'I' and s[i] == 'X') or (s[i-1] == 'X' and s[i] == 'L') \
                    or (s[i-1] == 'X' and s[i] == 'C') or (s[i-1] == 'C' and s[i] == 'D') or (s[i-1] == 'C' and s[i] == 'M'):
                continue
        if s[i] == 'I':
            a += 1
        if s[i] == 'V':
            a += 5
        if s[i] == 'X':
            a += 10
        if s[i] == 'L':
            a += 50
        if s[i] == 'C':
            a += 100
        if s[i] == 'D':
            a += 500
        if s[i] == 'M':
            a += 1000
    return a


# tests:
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))