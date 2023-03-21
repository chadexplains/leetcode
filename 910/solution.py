class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        n = len(A)
        ans = A[n-1] - A[0]
        for i in range(n-1):
            a, b = A[i], A[i+1]
            high = max(A[n-1]-K, a+K)
            low = min(A[0]+K, b-K)
            ans = min(ans, high-low)
        return ans