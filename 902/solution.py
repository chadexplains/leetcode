class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n = list(str(n))
        m = len(n)
        k = len(digits)
        dp = [0] * m + [1]
        for i in range(m - 1, -1, -1):
            for j in range(k):
                if digits[j] < n[i]:
                    dp[i] += k ** (m - i - 1)
                elif digits[j] == n[i]:
                    dp[i] += dp[i + 1]
        return dp[0] + sum(k ** i for i in range(1, m))