# function:
def myAtoi(s):
    s_new = ""
    k = 0
    for i in range(len(s)):
        if k == i and s[k] == " ":
            k += 1
            continue
        elif k == i and (s[k] == "-" or s[k] == "+"):
            s_new += s[k]
        elif not s[i].isdigit():
            break
        else:
            s_new += s[i]
    if s_new == "" or s_new == "+" or s_new == "-":
        s_new += "0"
    s_new = int(s_new)
    if s_new <= -2 ** 31:
        s_new = -2 ** 31
    if s_new >= 2 ** 31 - 1:
        s_new = 2 ** 31 - 1
    return s_new

# tests:
print(myAtoi("42"))
print(myAtoi("   -42"))
print(myAtoi("4193 with words"))