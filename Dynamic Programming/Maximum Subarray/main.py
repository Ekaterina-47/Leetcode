# function:
def maxSubArray(nums):
    currSum = 0  # текущая накопленная сумма
    maxSum = 0  # конечная искомая сумма

    if len(nums) == 1:
        return nums[0]

    for i in range(0, len(nums)):
        if nums[i] > 0:
            break
        elif nums[i] < 0 and i != len(nums) - 1:
            continue
        elif i == len(nums) - 1 and nums[i] < 0:
            maxSum = max(nums)
            return maxSum

    for i in range(0, len(nums)):
        currSum += nums[i]
        if currSum > maxSum:
            maxSum = currSum
            i += 1
        if currSum < 0:
            currSum = 0

    return maxSum


# tests:
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray([1]))
print(maxSubArray([1, 1, 1, 1, -9]))
print(maxSubArray([-1]))
print(maxSubArray([-1, -2, -3, -4, -5]))
print(maxSubArray([5, 4, -1, 7, 8]))
print(maxSubArray([1, 2, -1]))
