# function:
def rotate(nums, k):
    N = len(nums)
    if k >= N:
        k = k % N
    tmp = nums[N-k:]
    for i in range(N-1-k, -1, -1):
        nums[i+k] = nums[i]
    nums[:k] = tmp
    return nums

# tests:
print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate([1, 2], 3))

