class Solution:
    def countTriplets(self, A: List[int]) -> int:
        freq = collections.defaultdict(int)
        for a in A:
            freq[a] += 1
        A = list(freq.keys())
        n = len(A)
        dp = [[0] * 64 for _ in range(n)]
        for i in range(n):
            dp[i][A[i]] = freq[A[i]]
        for i in range(n):
            for j in range(64):
                for k in range(n):
                    if j & A[k] == j:
                        dp[i][j] += freq[A[k]] * dp[k][j]
        ans = 0
        for i in range(n):
            for j in range(n):
                if A[i] & A[j] == 0:
                    ans += dp[i][0] * dp[j][0]
        return ans