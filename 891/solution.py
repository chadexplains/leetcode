class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        n = len(A)
        mod = 10**9 + 7
        res = 0
        pow2 = [1]
        for i in range(1, n):
            pow2.append(pow2[-1] * 2 % mod)
        for i in range(n):
            res = (res + (pow2[i] - pow2[n - i - 1]) * A[i]) % mod
        return res