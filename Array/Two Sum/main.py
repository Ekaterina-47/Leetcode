# function:
def twoSum(nums, target):
    mass = []
    for i in range(0, len(nums)):
        if len(mass) != 0:
            break
        for j in range(1, len(nums)):
            if i != j and nums[i] + nums[j] == target:
                mass.append(i)
                mass.append(j)
                break
    return mass

# tests:
print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
