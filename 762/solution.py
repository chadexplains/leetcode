class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        count = 0
        for i in range(L, R + 1):
            if is_prime(bin(i).count('1')):
                count += 1
        return count