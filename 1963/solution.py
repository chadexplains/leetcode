class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod = 10**9 + 7
        max_num = (1 << p) - 1
        num_pairs = (max_num - 1) // 2
        product = max_num * (max_num - 1) % mod
        power = pow(product, num_pairs, mod)
        return power * (max_num % mod) % mod