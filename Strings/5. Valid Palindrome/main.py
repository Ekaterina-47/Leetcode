# Является ли фраза палиндромом - если после преобразования прописных букв в строчные и удаления небуквенн0-цифровых символов
# она читается задом наперёд

def isPalindrome(s):
    s1 = ""
    for i in s:
        if i.isalpha() or i.isdigit():
            s1 += i
    s1 = s1.lower()
    print(s1)
    s2 = ''.join(reversed(s1))
    print(s2)
    if s1 == s2:
        return True
    else:
        return False



print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
print(isPalindrome("0P"))