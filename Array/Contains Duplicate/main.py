# function:
def containsDuplicate2(nums):
    if len(nums) != len(set(nums)):
        return True
    return False

# tests:
print(containsDuplicate2([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
print(containsDuplicate2([1, 2, 3, 4, 5]))
print(containsDuplicate2([9, 5, 2, 3, 1, 5, 7]))