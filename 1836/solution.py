def maximumSum(nums):
    n = len(nums)
    left = [0] * n
    right = [0] * n
    left[0] = nums[0]
    right[n-1] = nums[n-1]
    for i in range(1, n):
        left[i] = max(nums[i], left[i-1] + nums[i])
    for i in range(n-2, -1, -1):
        right[i] = max(nums[i], right[i+1] + nums[i])
    max_sum = max(left)
    for i in range(1, n-1):
        max_sum = max(max_sum, left[i-1] + right[i+1])
    kadane_sum = nums[0]
    max_kadane = nums[0]
    for i in range(1, n):
        kadane_sum = max(nums[i], kadane_sum + nums[i])
        max_kadane = max(max_kadane, kadane_sum)
    return max(max_sum, max_kadane)