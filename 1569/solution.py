class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][i] = 1
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                for k in range(i, j+1):
                    if nums[k] < nums[i]:
                        dp[i][j] += dp[k+1][j] * self.C(j-k+i, j-k)
                        dp[i][j] %= 10**9 + 7
                    elif nums[k] > nums[j]:
                        dp[i][j] += dp[i][k-1] * self.C(j-k+i, i)
                        dp[i][j] %= 10**9 + 7
        return dp[0][n-1]

    def C(self, n: int, m: int) -> int:
        res = 1
        for i in range(1, m+1):
            res = res * (n-i+1) // i
        return res % (10**9 + 7)