class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors <= 3:
            return primeFactors
        q, r = divmod(primeFactors, 3)
        if r == 0:
            return pow(3, q, 10**9 + 7)
        elif r == 1:
            return pow(3, q - 1, 10**9 + 7) * 4 % (10**9 + 7)
        else:
            return pow(3, q, 10**9 + 7) * 2 % (10**9 + 7)