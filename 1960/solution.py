class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod = 10**9 + 7
        max_num = (2**p) - 1
        pairs = (2**(p-1)) - 1
        product = (max_num - 1) % mod
        power = pow(product, pairs, mod)
        return (power * max_num) % mod