def longestArithSeqLength(self, A: List[int]) -> int:
    dp = {}
    for i in range(len(A)):
        for j in range(i):
            diff = A[i] - A[j]
            if diff not in dp[j]:
                dp[j][diff] = 1
            dp[i][diff] = dp[j][diff] + 1
        
    return max(max(dp[i].values()) for i in range(len(A))) if A else 0