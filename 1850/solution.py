def getMinSwaps(num: str, k: int) -> int:
    nums = list(map(int, num))
    n = len(nums)
    for i in range(k):
        j = n - 2
        while j >= 0 and nums[j] >= nums[j + 1]:
            j -= 1
        if j == -1:
            break
        l = n - 1
        while nums[l] <= nums[j]:
            l -= 1
        nums[j], nums[l] = nums[l], nums[j]
        nums[j + 1:] = reversed(nums[j + 1:])
    ans = 0
    for i in range(n):
        j = i
        while j < n and nums[j] != int(num[i]):
            j += 1
        ans += j - i
        nums[i:j+1] = [nums[j]] + nums[i:j]
    return ans