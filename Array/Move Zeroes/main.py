# function:
def moveZeroes(nums):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 0:
            for j in range(i, len(nums) - 1):
                nums[j] = nums[j + 1]
            nums[-1] = 0
    return nums

# tests:
print(moveZeroes([0, 1, 0, 3, 12]))
print(moveZeroes([0]))
