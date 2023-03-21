def beautifulArray(n: int) -> List[int]:
    def helper(nums):
        if len(nums) == 1:
            return nums
        odds = helper(nums[::2])
        evens = helper(nums[1::2])
        return odds + evens
    return helper(list(range(1, n+1)))