# function:
def intersect(nums1, nums2):
    nums3 = []
    for i in nums1:
        if i in nums2:
            nums2.remove(i)
            nums3.append(i)
    return nums3

# tests:
print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
print(intersect([1, 2, 2, 1], [2, 2]))
print(intersect([1, 2, 2, 1], [2]))
