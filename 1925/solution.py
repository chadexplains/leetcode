class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def pow_mod(x, y):
            res = 1
            while y:
                if y & 1:
                    res = res * x % MOD
                x = x * x % MOD
                y >>= 1
            return res
        return pow_mod(5, (n+1)//2)