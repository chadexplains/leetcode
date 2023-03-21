class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        last_occurrence = {}
        prev = 1
        for i in range(n):
            if s[i] not in last_occurrence:
                dp[i+1] = 2*prev
            else:
                j = last_occurrence[s[i]]
                dp[i+1] = 2*prev - dp[j]
            prev = dp[i+1]
            last_occurrence[s[i]] = i
        return (dp[n]-1)%(10**9+7)