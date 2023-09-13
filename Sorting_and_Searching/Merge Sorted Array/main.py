# function:
def merge(nums1, m, nums2, n):
    i = k = 0
    while i < m and k < n:
        if nums1[i] <= nums2[k]:
            i += 1
        else:
            for a in range(len(nums1)-1, i-1, -1):
                nums1[a] = nums1[a-1]
            nums1[i] = nums2[k]
            k += 1
            i += 1
            m += 1
    while k < n:
        for a in range(len(nums1) - 1, i - 1, -1):
            nums1[a] = nums1[a - 1]
        nums1[i] = nums2[k]
        k += 1
        i += 1
    return nums1


# tests:
print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(merge([1], 1, [], 0))
print(merge([0], 0, [1], 1))
print(merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3))
print(merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3))


