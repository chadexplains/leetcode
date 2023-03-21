class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums) - min(nums)
        if k == 1:
            return self.get_score(nums)
        if k > n // len(set(nums)):
            return -1
        nums.sort()
        dp = [[float('inf')] * (k + 1) for _ in range(1 << n)]
        dp[0][0] = 0
        for mask in range(1 << n):
            if bin(mask).count('1') % (n // k) == 0:
                for j in range(1, k + 1):
                    for i in range(n):
                        if mask & (1 << i):
                            continue
                        for l in range(i + 1, n):
                            if mask & (1 << l):
                                continue
                            if l == i + 1 or nums[l] != nums[l - 1]:
                                dp[mask | (1 << i) | (1 << l)][j] = min(dp[mask | (1 << i) | (1 << l)][j], dp[mask][j - 1] + self.get_score(nums[i:l + 1]))
        return dp[(1 << n) - 1][k]

    def get_score(self, nums: List[int]) -> int:
        return max(nums) - min(nums)