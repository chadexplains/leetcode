class NumArray:
    
    def __init__(self, nums: List[int]):
        self.dp = [0] * len(nums)
        self.dp[0] = nums[0]
        for i in range(1, len(nums)):
            self.dp[i] = self.dp[i-1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.dp[j]
        else:
            return self.dp[j] - self.dp[i-1]