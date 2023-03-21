class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        for m in range(math.floor(math.log2(n)), 1, -1):
            k = int(n ** (1 / m))
            if k > 1:
                if (k ** (m + 1) - 1) // (k - 1) == n:
                    return str(k)
        return str(n - 1)