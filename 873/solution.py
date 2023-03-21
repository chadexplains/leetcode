def lenLongestFibSubseq(self, A: List[int]) -> int:
    s = set(A)
    dp = {}
    for j in range(len(A)):
        for i in range(j):
            if A[j] - A[i] < A[i] and A[j] - A[i] in s:
                dp[i, j] = dp.get((A[j] - A[i], i), 2) + 1
    return max(dp.values() or [0])