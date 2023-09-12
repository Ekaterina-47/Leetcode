# function:
def plusOne(digits):
    N = len(digits)
    if N == 0:
        digits.append(1)
    else:
        digits[-1] += 1
        for i in range(N - 1, -1, -1):
            if digits[i] == 10:
                digits[i] = 0
                if digits[i] != digits[0]:
                    digits[i-1] += 1
                    continue
                else:
                    digits.insert(0, 1)
            break
    return digits

# tests:
print(plusOne([4, 3, 2, 1]))
print(plusOne([9]))
print(plusOne([9, 9]))
print(plusOne([9, 9, 9, 9]))
print(plusOne([9, 9, 8, 9]))
print(plusOne([9, 1, 9, 9]))
print(plusOne([]))
