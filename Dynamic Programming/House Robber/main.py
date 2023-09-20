# function:
def rob(nums):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    currSum = prev1
    for i in range(2, len(nums)):
        currSum = max(nums[i] + prev2, prev1)
        prev2 = prev1
        prev1 = currSum
    return currSum


# tests:
print(rob([1, 2, 3, 1]))
print(rob([2, 7, 9, 3, 1]))
print(rob([7]))