class Solution:
    def smallestFactorization(self, a: int) -> int:
        if a < 2:
            return a
        res = 0
        mul = 1
        for i in range(9, 1, -1):
            while a % i == 0:
                a //= i
                res += mul * i
                mul *= 10
        return res if a == 1 and res < 2**31 else 0