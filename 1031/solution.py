def maxSumTwoNoOverlap(nums: List[int], firstLen: int, secondLen: int) -> int:
    n = len(nums)
    left = [0] * n
    right = [0] * n
    leftMax = 0
    rightMax = 0
    for i in range(n):
        leftMax = max(leftMax + nums[i], nums[i])
        left[i] = max(left[i - 1], leftMax)
        j = n - i - 1
        rightMax = max(rightMax + nums[j], nums[j])
        right[j] = max(right[j + 1], rightMax)
    res = 0
    for i in range(firstLen - 1, n - secondLen):
        res = max(res, left[i] + right[i + 1], left[i - firstLen + 1] + right[i + 1], left[i] + right[i - secondLen + 1])
    return res