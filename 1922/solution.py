class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_count = pow(5, (n + 1) // 2, 1000000007)
        prime_count = pow(4, n // 2, 1000000007)
        return (even_count * prime_count) % 1000000007