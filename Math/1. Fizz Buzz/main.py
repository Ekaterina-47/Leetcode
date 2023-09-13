# function
def fizzBuzz(n):
    s = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            s.append("FizzBuzz")
        elif i % 3 == 0:
            s.append("Fizz")
        elif i % 5 == 0:
            s.append("Buzz")
        else:
            s.append(str(i))
    return s

# tests:
print(fizzBuzz(3))
print(fizzBuzz(5))
print(fizzBuzz(15))
