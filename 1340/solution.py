class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1] * n
        indices = sorted(range(n), key=lambda i: arr[i], reverse=True)
        def dfs(i):
            if dp[i] != 1:
                return dp[i]
            res = 1
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                res = max(res, 1 + dfs(j))
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break
                res = max(res, 1 + dfs(j))
            dp[i] = res
            return res
        for i in indices:
            dfs(i)
        return max(dp)