class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[float('inf')] * n for _ in range(1 << n)]
        for i in range(n):
            dp[0][i] = 0
        for i in range(1, 1 << n):
            for j in range(n):
                for k in range(n):
                    if i & (1 << k):
                        dp[i][j] = min(dp[i][j], dp[i ^ (1 << k)][k] + (nums1[j] ^ nums2[k]))
        return dp[(1 << n) - 1][0]