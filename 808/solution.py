class Solution:
    def soupServings(self, N: int) -> float:
        if N >= 4800:
            return 1.0
        memo = {}
        def dp(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            memo[(a, b)] = 0.25 * (dp(a-100, b) + dp(a-75, b-25) + dp(a-50, b-50) + dp(a-25, b-75))
            return memo[(a, b)]
        return dp(N, N)