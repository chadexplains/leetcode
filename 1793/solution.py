def maximumScore(nums: List[int], k: int) -> int:
    left, right = k, k
    n = len(nums)
    res = cur_min = nums[k]
    while left > 0 or right < n - 1:
        if (nums[left - 1] if left else 0) < (nums[right + 1] if right != n - 1 else 0):
            right += 1
        else:
            left -= 1
        cur_min = min(cur_min, nums[left], nums[right])
        res = max(res, cur_min * (right - left + 1))
    return res