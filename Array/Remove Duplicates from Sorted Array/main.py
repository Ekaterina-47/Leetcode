# function:
def removeDuplicates(nums):
    unic = 0
    tek = 1
    for i in range(1, len(nums)):
        if nums[tek] != nums[unic]:
            unic += 1
            nums[unic] = nums[tek]
            tek += 1
        else:
            tek += 1
    k = len(nums[0:unic + 1])
    return k

# tests:
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([1, 1, 2, 3, 4, 4, 4]))
print(removeDuplicates([1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 8, 8, 8, 9]))
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
