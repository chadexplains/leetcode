def nextGreaterElement(n):
    nums = list(str(n))
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    if i < 0:
        return -1
    j = len(nums) - 1
    while j > i and nums[j] <= nums[i]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]
    nums[i+1:] = sorted(nums[i+1:])
    res = int(''.join(nums))
    return res if res < 2**31 else -1