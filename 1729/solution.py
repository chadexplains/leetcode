def minimumMountainRemovals(nums):
    n = len(nums)
    lis_left = [1] * n
    lis_right = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                lis_left[i] = max(lis_left[i], lis_left[j] + 1)
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[i] > nums[j]:
                lis_right[i] = max(lis_right[i], lis_right[j] + 1)
    max_common = 0
    for i in range(n):
        max_common = max(max_common, lis_left[i] + lis_right[i] - 1)
    return n - max_common