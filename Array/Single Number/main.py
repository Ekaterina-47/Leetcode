# function:
def singleNumber(nums):
    unic_nums = list(set(nums))
    for i in unic_nums:
        a = nums.count(i)
        if a == 1:
            return i


# tests:
print(singleNumber([2, 2, 1]))
print(singleNumber([4, 1, 2, 1, 2]))
print(singleNumber([1]))
print((singleNumber([-1, -1, 2, 2, 3, 3, -7])))
